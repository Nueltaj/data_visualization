import time
import pygal
from die import Die
from collections import Counter

start_time = time.time()
# Your code here


# Create a D6 and a D8
die_1 = Die()
die_2 = Die(8)
# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(10000000)]

# Analyze the results.

max_result = die_1.num_sides + die_2.num_sides
frequency_collection = Counter(results)
frequencies=[frequency_collection.get(value,0)for value in range(2,max_result+1)]



hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D8 dice 10000000 times."
hist.x_labels = list(range(2, 15))
hist.x_title = "Result"
hist.add("D6 + D8", frequencies)
hist.render_to_file("D8_dice_visual.svg")

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
