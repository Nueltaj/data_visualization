"""this script is created to visualize 10 countries with the highest Co2 emissions"""

import csv
import pygal
from country_codes import get_country_code

# setting filename
FILENAME = "Carbon_(CO2)_Emissions_by_Country.csv"
# initialize the dictionary with the country code as keys and Co2emissions as the values
Co2_emissions = {}
# read the file
with open(FILENAME, "r", encoding="latin-1") as file_obj:
    reader = csv.reader(file_obj)
    # skip the header row
    next(reader)
    #iterate through the data
    for row in reader:
        country_name = row[0]
        country_date = row[2]
        code = get_country_code(country_name)
        if code and country_date == "01-01-2016":
            try:
                Kilotons_of_C02 = float(row[3])
                Co2_emissions[country_name] = Kilotons_of_C02
            except (ValueError, IndexError):
                print(f"missing data or wrong column in {FILENAME}")
        # else:
        #     print(f"no country code generated for {country_name}")
# sorting the emissions in descending order
sorted_co2_emissions = sorted(Co2_emissions.items(), key=lambda x: x[1], reverse=True)
# sorting out the top 10
top_10 = sorted_co2_emissions[:10]
# extracting the data into lists
countries, emissions = zip(*top_10)
# creating a bar chart
barchart = pygal.Bar()
barchart.title = "Top 10 Countries With the Highest co2 Emissions(2016)"
barchart.x_labels = countries
barchart.add("Co2 emissions", emissions)
barchart.render_to_file("top_10_countries_co2_emissions_viz.svg")
