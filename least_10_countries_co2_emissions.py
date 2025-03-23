"""this script is resonsible for visualing 10 countries with the least co2 emissions"""

import csv
import pygal
from country_codes import get_country_code

# setting filename
FILENAME = "Carbon_(CO2)_Emissions_by_Country.csv"
# opening the file
with open(FILENAME, "r", encoding="latin-1") as file_obj:
    reader = csv.reader(file_obj)
    # skip the header row
    next(reader)
    # initialize a dictionary where the key is the country name and the value is the co2emissions
    Co2_emissions = {}
    # iterate through the rows in the dataset
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
# Sorting the dictionary in ascending order to get the countries with the lowest CO₂ emissions
sorted_Co2_emissions = sorted(Co2_emissions.items(), key=lambda x: x[1])
least_10 = sorted_Co2_emissions[:10]
# extracting data
countries, emissions = zip(*least_10)
# creating a barchart
barchart = pygal.Bar()
# setting a title
barchart.title = "Top 10 Countries With the lowest co2 Emissions(2016)"
# setting a label for the x axis
barchart.x_labels = countries
# y axis
barchart.add("C02_emissions", emissions)
# saving the data visualized in svg format
barchart.render_to_file("least_10_countries_co2_emissions_viz.svg")
