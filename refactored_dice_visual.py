#using a list comprehension method for every for lopp in the original file
import pygal
from die import Die

# Create a two D6
die_1 = Die()
die_2 = Die()
# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(5000)]

# Analyze the results.

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]


hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = list(range(2, 13))
hist.x_title = "Result"
hist.add("D6 + D6", frequencies)
hist.render_to_file("refactored_dice_visual.svg")
