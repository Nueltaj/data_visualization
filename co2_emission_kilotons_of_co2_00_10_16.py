"""This script visualizes CO2 emissions across multiple years (2000, 2010, 2016)"""

import csv
import pygal_maps_world.maps
from country_codes import get_country_code

# Setting dictionaries for each year
Kilotons_2000, Kilotons_2010, Kilotons_2016 = {}, {}, {}

# Setting the filename
FILENAME = "Carbon_(CO2)_Emissions_by_Country.csv"

# Reading the CSV file
with open(FILENAME, "r", encoding="latin-1") as file_obj:
    reader = csv.reader(file_obj)
    next(reader)  # Skip header

    for row in reader:
        country_name = row[0]
        country_date = row[2]  # Date of the emission data
        code = get_country_code(country_name)  # Convert country name to country code

        if code:
            try:
                co2_value = float(row[3])  # Extract CO2 emission value

                # Store values in the correct dictionary based on the year
                if country_date == "01-01-2000":
                    Kilotons_2000[code] = co2_value
                elif country_date == "01-01-2010":
                    Kilotons_2010[code] = co2_value
                elif country_date == "01-01-2016":
                    Kilotons_2016[code] = co2_value

            except (ValueError, IndexError):
                print(f"Missing or invalid data for {country_name} ")


# Function to create world maps
def create_world_map(title, data, filename):
    """a module for creaing svg file of the """
    wm = pygal_maps_world.maps.World()
    wm.title = title
    wm.add("CO₂ Emissions (Kilotons)", data)
    wm.render_to_file(filename)


# Generate world maps for different years
create_world_map("CO₂ Emissions in 2000", Kilotons_2000, "co2_emissions_2000.svg")
create_world_map("CO₂ Emissions in 2010", Kilotons_2010, "co2_emissions_2010.svg")
create_world_map("CO₂ Emissions in 2016", Kilotons_2016, "co2_emissions_2016.svg")

print("World maps for 2000, 2010, and 2016 have been created successfully!")
