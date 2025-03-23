"""this module is responsible for visualing education themed data"""

import csv
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code
# Define lists to store data
unemployment_rate = {}


FILENAME = "Global_Education.csv"
with open(FILENAME, "r", encoding="latin-1") as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)
    name_of_country = {}

    # Process each row
    for row in reader:
        country_name = row[0]
        code = get_country_code(country_name)
        if code:
            try:
                # Convert data to float and store in dictionaries
                if row[28]:
                    unemployment_rate[code] = float(row[28])
                name_of_country[code] = country_name
            except (ValueError, IndexError):
                print(f"Missing or invalid data for {country_name}")

# Create a world map and add data
wm_style=RS("#4ef542", base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = "A Data Visualization of the Unemployment Rate"
wm.add("Unemployment Rate", unemployment_rate)
wm.render_to_file("Global_education.svg")
