"""a Module created to generat the 2-digit country code"""

from pygal_maps_world.i18n import COUNTRIES


# Dictionary for correcting country names
def get_country_code(country_name):
    """Return the pygal 2-digit country code for the country name."""
    name_fixes = {
        "Bolivia": "Bolivia, Plurinational State of",
        "Brunei": "Brunei Darussalam",
        "Democratic Republic of the Congo": "Congo, the Democratic Republic of the",
        "Ivory Coast": "Côte d'Ivoire",
        "Laos": "Lao People's Democratic Republic",
        "Moldova": "Moldova, Republic of",
        "North Korea": "Korea, Democratic People's Republic of",
        "South Korea": "Korea, Republic of",
        "Russia": "Russian Federation",
        "Syria": "Syrian Arab Republic",
        "Tanzania": "Tanzania, United Republic of",
        "Vatican City": "Holy See",
        "Vietnam": "Viet Nam",
        "Republic of the Congo": "Congo",
        "Palestine": "Palestinian Territory",
    }

    # Fix country names
    country_name = name_fixes.get(country_name, country_name)

    # Match with Pygal's country codes
    for code, name in COUNTRIES.items():
        if name.lower() == country_name.lower():
            return code

    return None  # If no match is found
