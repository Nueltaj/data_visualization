#using a list comprehension method for every for lopp in the original file
import pygal
from die import Die

# Create a D6.
die = Die()
# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# Analyze the results...
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6", frequencies)
hist.render_to_file("refactored_die_visual.svg")
