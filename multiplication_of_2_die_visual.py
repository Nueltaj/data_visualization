import pygal
from die import Die
from collections import Counter
import time 
start_time = time.time()
# Create a D6,D6,D6
die_1 = Die()
die_2 = Die()
# Make some rolls, and store results in a list.
results = [die_1.roll() * die_2.roll()for roll_num in range(10000)]

# Analyze the results.

max_result = die_1.num_sides * die_2.num_sides 
frequency_counter = Counter(results)
frequencies = [frequency_counter.get(value,0) for value in range(1, max_result + 1)]



hist = pygal.Bar()
hist.title = "Results of rolling a multiplied D6 dice 10000 times."
hist.x_labels = list(range(1, 37))
hist.x_title = "Result"
hist.add("D6*D6", frequencies)
hist.render_to_file("multiplication_of_2_die_visual.svg")
end_time = time.time()
print(f"execution time:{end_time - start_time} seconds")