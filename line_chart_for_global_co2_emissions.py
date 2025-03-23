"""This script visualizes global CO2 emissions trends over the years."""

import csv
import pygal
from country_codes import get_country_code

# Setting filename
FILENAME = "Carbon_(CO2)_Emissions_by_Country.csv"

# Opening the file
with open(FILENAME, "r", encoding="latin-1") as file_obj:
    reader = csv.reader(file_obj)
    next(reader)  # Skip header row

    # Dictionary to store emissions by country and year
    global_co2_emissions = {}

    # Read and process data
    for row in reader:
        country_name = row[0]
        country_date = row[2]
        co2_emission = row[3]
        code = get_country_code(country_name)

        if code:
            try:
                # Extract year from date
                year = int(country_date.split("-")[-1])
                # Convert emission to float
                co2_emission = float(co2_emission)

                # Initialize the country entry if not already present
                if code not in global_co2_emissions:
                    global_co2_emissions[code] = {}

                # Store the emission value for the given year
                global_co2_emissions[code][year] = co2_emission

            except (ValueError, IndexError, KeyError):
                print(f"Missing data in {country_name}")

# Initialize totals and years outside the loop
total_emissions_year = {}
years = set()  # Use a set to avoid duplicate years

# Calculate total emissions for each year
for code, emissions in global_co2_emissions.items():
    for year, emission in emissions.items():
        if year not in total_emissions_year:
            total_emissions_year[year] = 0
        total_emissions_year[year] += emission
        years.add(year)  # Add years to the set

# Sort years
sorted_years = sorted(years)

# Prepare emissions for the line chart based on sorted years
emissions_data = [total_emissions_year[year] for year in sorted_years]

# Create line chart
linechart = pygal.Line()
linechart.title = "Global CO2 Emission Trend over the years"
linechart.x_labels = map(str, sorted_years)
linechart.add("CO2 emissions", emissions_data)

# Save visualization
OUTPUT_FILE = "global_CO2_trends_per_year.svg"
linechart.render_to_file(OUTPUT_FILE)
print(
    f"Global CO2 trends over the years have been visualized! (Saved as {OUTPUT_FILE})"
)
