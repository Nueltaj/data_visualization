"""this script visualizes the birth rate of various countries"""

import csv
import pygal_maps_world.maps
from country_codes import get_country_code

# Dictionary to store birth rates with country codes as keys
birth_rate = {}
# setting filename
FILENAME = "Global_Education.csv"
# reading the file
with open(FILENAME, "r", encoding="latin-1") as file_obj:
    reader = csv.reader(file_obj)
    next(reader)
    for row in reader:
        country_name = row[0]
        # deriving the country code of the countries
        code = get_country_code(country_name)
        if code:
            try:
                birth_rate[code] = float(row[25])
            except (ValueError, IndexError):
                print("missing data")
        else:
            print(f"the country code can not be generated for {country_name}")


# creating a function for the visualization
def create_world_map(title, data, filename):
    """Create a world map visualization with given title, data, and filename."""
    wm = pygal_maps_world.maps.World()
    wm.title = title
    wm.add("birthrate", data)
    wm.render_to_file(filename)


# creating an instance of the function
create_world_map("The Birth Rate of Male and Female ", birth_rate, "birth_rate.svg")
print("The worldmap has been succesfully visualized")
