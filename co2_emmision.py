"""This module is responsible for visualizing CO2 emissions"""

import csv
import pygal_maps_world.maps
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from country_codes import get_country_code

# Setting dictionaries to store the dataset
Kilotons_of_C02, Metric_Tons_Per_Capita, name_of_country = {}, {}, {}
# setting a list for the missing countries
missing_countries = []
# Setting the filename
FILENAME = "Carbon_(CO2)_Emissions_by_Country.csv"

# Opening and reading the file properly
with open(FILENAME, "r", encoding="latin-1") as file_obj:
    # Read the file
    reader = csv.reader(file_obj)
    # Skip the header row
    next(reader)

    # Reading the rows of data in the CSV file within the with block
    for row in reader:
        country_name = row[0]
        country_date = row[2]
        if country_date == "01-01-2016":
            code = get_country_code(country_name)
            if code:
                try:
                    Kilotons_of_C02[code] = float(
                        row[3]
                    )  # Fixed incorrect function call
                    Metric_Tons_Per_Capita[code] = float(row[4])  # Ensure it's a number
                    name_of_country[code] = country_name
                except (ValueError, IndexError):
                    print(f"Missing or invalid data for {country_name}")
            else:
                missing_countries.append(country_name)  # Store missing country names

# Print missing country names
print("Countries with missing codes:")
for country in missing_countries:
    print(country)
# First world map for Kilotons_of_C02
wm_style = RS("#4ef542", base_style=LCS)
wm1 = pygal_maps_world.maps.World(style=wm_style)
wm1.title = "CO2 Emissions in Kilotons (2016)"
wm1.add("Kilotons of CO2", Kilotons_of_C02)
wm1.render_to_file("Co2_emissions_kilotons.svg")

# Second world map for Metric Tons Per Capita
wm2 = pygal_maps_world.maps.World()
wm2.title = "CO2 Emissions Per Capita (2016)"
wm2.add("Metric Tons Per Capita", Metric_Tons_Per_Capita)
wm2.render_to_file("Co2_emissions_per_capita.svg")
