"""display a worldmap ehere the population of the countries did decide the \
    shade of color"""

import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()  # created an instance of the class
wm.title="Populations of counytries in North America "
wm.add("North", {"ca": 34126000, "us": 309349000, "mx": 113423000})
wm.render_to_file("North_america_population.svg")
