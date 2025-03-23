import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]
# sets the line-width and input values
plt.plot(input_values, squares, linewidth=5)
# sets a title
plt.title("Square of Numbers", fontsize=24)
# sets a label on the x axis
plt.xlabel("Value", fontsize=14)
# sets a label on the y axis
plt.ylabel("Square of Value", fontsize=14)
# sets the tick
plt.tick_params("both", labelsize=14)
plt.show()
