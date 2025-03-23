"""this is a module"""

from pygal_maps_world.maps import World
from pygal_maps_world.i18n import COUNTRIES

wm = World()
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
