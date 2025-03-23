"""change country name in a json file"""

import json

# Load the JSON data
FILENAME = "world_population.json"
with open(FILENAME, encoding="utf-8") as file_obj:
    pop_data = json.load(file_obj)

# Modify the data
for pop_dict in pop_data:
    country_name = pop_dict["Country"]
    if country_name == "Venezuela":
        pop_dict["Country"] = "Venezuela, Bolivarian Republic of"

# Save the modified data back to the JSON file
with open(FILENAME, "w", encoding="utf-8") as file_obj:
    json.dump(pop_data, file_obj, indent=4)

print("Data updated successfully!")
