"""This script generates a line chart for Co2 emissions through the years of a user country"""

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
    # initialize a dictionary where the key is the country name and the value is years
    # and value is emissions
    Co2_emissions = {}
    # iterate through the rows in the dataset
    for row in reader:
        country_name = row[0]
        country_date = row[2]
        co2_emission = row[3]
        code = get_country_code(country_name)
        if code:
            try:
                year = int(country_date.split("-")[-1])
                co2_emission = float(co2_emission)
                if code not in Co2_emissions:
                    Co2_emissions[code] = {}
                Co2_emissions[code][year] = co2_emission

            except (ValueError, IndexError):
                print(f"missing data in {country_name}")


# setting up the user interface
print(
    "I'm responsible for visualizing Co2 emission trends over the years of a particular country."
)
user_country = (
    input("What country would you like to see it's Co2 trends? ").lower().strip()
)
country_code = get_country_code(user_country)
if country_code in Co2_emissions:
    years = sorted(Co2_emissions[country_code].keys(), reverse=True)
    print(years)
    emissions = [Co2_emissions[country_code][year] for year in years]

    # visualizing data
    linechart = pygal.Line()
    # the title
    linechart.title = f"CO2 Emission Trend of {user_country.title()} Over the Years"
    # x-axis label
    linechart.x_labels = map(str, years)
    # y-axis
    linechart.add("Co2 emissions", emissions)
    # save as svg file
    linechart.render_to_file(f"Co2_trends_{user_country}.svg")
    print(f"Co2 trends of {user_country.title()} has been visualized!!!")

else:
    print(f"{user_country.title()} is not a country name or in the dataset")
