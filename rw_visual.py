import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()
    # set, the background of the plot
    plt.figure(facecolor="lightgrey")
    point_numbers = list(range(rw.num_points))
    plt.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolor="none",
        s=5,
    )
    # Emphasize the first and last points.
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
    # hide axes
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ").lower().strip()
    if keep_running == "n":
        break
