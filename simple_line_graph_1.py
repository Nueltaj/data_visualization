import matplotlib.pyplot as plt

x_values = list(range(1,101))
y_values = [x**2 for x in x_values]
#using the c function to change the color od the dots
#plt.scatter(x_values, y_values,c="red", edgecolor ="none",s = 40)
plt.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, edgecolor ="none",s = 40)
# Set chart title and label axes.
plt.title("Square of Numbers", fontsize=24)
# setting up the x label and y label
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# setting up the tick_params
plt.tick_params(axis="both", which="major", labelsize=14)

# Set the range for each axis.
plt.axis([0, 110, 0, 11000])
#to show the graph
#plt.show()
#to save as file
plt.savefig("Square_of_numbers_plot.png", bbox_inches ="tight")