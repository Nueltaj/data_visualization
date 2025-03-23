import matplotlib.pyplot as plt
import numpy as np 
x = [2,5,3,7,1,9,3,6,3,7,9,5,4]

bins = np.arange(1,10)
plt.hist(x, bins,histtype="bar", rwidth=0.6)
plt.show()