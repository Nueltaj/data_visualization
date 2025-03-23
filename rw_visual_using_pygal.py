import pygal
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()
    projection = pygal.XY(
        stroke=False,
        title="Visualization of a Random Walk",
        show_x_labels=False,
        show_y_labels=False,
        show_legend = False
    )
    point_numbs = [(x,y) for x,y in zip(rw.x_values, rw.y_values)]
    projection.add("Random Walk",point_numbs)
    projection.add("Start", [(0,0)], dot_size =10)
    projection.add("End", [(rw.x_values[-1],rw.y_values[-1])], dot_size=10)
    projection.render_to_file("random_walk_visual_using_pygal.svg")
    
        # Prompt to continue or exit
    keep_running = input("Make another walk? (y/n): ").lower()
    if keep_running == 'n':
        break


