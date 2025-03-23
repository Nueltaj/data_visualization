import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from die import Die

#create a D6
die = Die()
#Make some rolls and store in a list
results =[die.roll() for roll_num in range(1000)]
#analyze the results
#count results
frequeny_counter = Counter(results)
frequencies=[ frequeny_counter.get(value,0) for value in range(1, die.num_sides+1)]
# x = np.arange(1, die.num_sides+1)
# plt.bar(x, frequencies, width=0.6, color ="blue", edgecolor="black")
# plt.title("Results of rolling one D6 1000 times")
# plt.xlabel("Result")
# plt.ylabel("Frequency of Result")
# plt.xticks(ticks=x)
# plt.show()
plt.hist(results, bins=np.arange(1, 8) - 0.5, rwidth=0.8, edgecolor='black')
plt.title("Results of rolling one D6 1000 times")
plt.xlabel("Result")
plt.ylabel("Frequency of Result")
plt.xticks(ticks=range(1, 7))
plt.show()
