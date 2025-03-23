"""this is a module that displays the GDP of each country"""

import json
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code

# Load GDP data from JSON file
FILENAME = "gdp.json"
with open(FILENAME, "r", encoding="utf-8") as file_obj:
    pop_data = json.load(file_obj)

# Create a dictionary to store GDP data for 2016
country_gdp = {}

# Process the data
for pop_dict in pop_data:
    country_name = pop_dict["Country Name"]
    country_code = pop_dict["Country Code"]
    year = pop_dict["Year"]
    value = pop_dict["Value"]

    if year == "2016":
        code = get_country_code(country_name)
        if code:  # Only add if the country code is valid
            country_gdp[code] = float(value)

# Set up the world map
wm_style = RS("#4ef542", base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = "GDP of the year 2016"
wm.add("2016", country_gdp)  # Add the GDP data
wm.render_to_file("World_GDP.svg")
