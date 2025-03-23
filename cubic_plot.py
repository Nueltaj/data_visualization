# 15-1. Cubes: A number raised to the third power is a cube. Plot the first five
# cubic numbers, and then plot the first 5000 cubic numbers.
# 15-2. Colored Cubes: Apply a colormap to your cubes plot.
import matplotlib.pyplot as plt

x_inputs = list(range(1, 51))
y_inputs = [x**3 for x in x_inputs]
plt.scatter(x_inputs, y_inputs, edgecolors="none", s=10, c=y_inputs, cmap=plt.cm.Reds)
plt.title("Scatter Plot of Cubic Numbers (1 to 50)", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube Values", fontsize=14)

plt.tick_params(axis="both", which="major", labelsize=14)
plt.axis([0, max(x_inputs) + 5, 0, max(y_inputs) + 10000])

plt.show()
#plt.savefig("Scatter Plot of Cubic Numbers (1 to 5000)", bbox_inches="tight")

