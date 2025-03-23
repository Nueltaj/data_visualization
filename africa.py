"""This module was created to display nigeria on the map"""

import pygal_maps_world.maps

# Create a world map instance
wm = pygal_maps_world.maps.World()
wm.title = "North, South, East ,West and Capital Africa"

# Add data (country codes as keys, values as data)

wm.add("North Africa", ["dz", "eg", "ly", "ma", "sd", "tn", "eh"])
wm.add("South Africa", ["bw", "sz", "ls", "ls", "na", "za"])
wm.add(
    "East Africa",
    [
        "zw",
        "zm",
        "ug",
        "tz",
        "ss",
        "so",
        "sc",
        "sc",
        "rw",
        "mz",
        "mu",
        "mw",
        "mg",
        "ke",
        "et",
        "er",
        "dj",
        "km",
        "bi",
    ],
)
wm.add(
    "west Africa",
    [
        "bj",
        "bf",
        "cv",
        "ci",
        "gm",
        "gh",
        "gn",
        "gw",
        "lr",
        "ml",
        "mr",
        "ne",
        "ng",
        "sn",
        "sl",
        "tg",
    ],
)
wm.add("Capital Africa",["ao","cm","cf","td","cg","cd","gq","ga","st"])

# Render the map to an SVG file
wm.render_to_file("africa_population.svg")
