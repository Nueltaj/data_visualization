"""This is a module that retrieves data from a libary and it's  visualized """

import json
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS ,RotateStyle as RS
from country_codes import get_country_code

FILE_NAME = "world_population.json"
with open(FILE_NAME, "r", encoding="utf-8") as file_obj:
    pop_data = json.load(file_obj)
cc_population = {}
for pop_dict in pop_data:
    country_name = pop_dict["Country"]
    population = int(pop_dict["2022 Population"])
    code = get_country_code(country_name)

    if code:
        cc_population[code] = population
    # grouping the countries together by population
    cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
    for cc, pop in cc_population.items():
        if pop < 10000000:
            cc_pop_1[cc] = pop
        elif pop < 1000000000:
            cc_pop_2[cc] = pop
        else:
            cc_pop_3[cc] = pop




# See how many countries are in each level.
print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))
wm_style = RS('#4ef542', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = "World population in 2020, by Country"
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)
wm.render_to_file("World_population.svg")
