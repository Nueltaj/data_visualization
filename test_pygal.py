import pygal

# Create a Scatter chart instance
scatter_chart = pygal.XY(stroke=False, title="Scatter Plot Example")

# Add data points to the scatter chart
scatter_chart.add('Group 1', [(1, 3), (2, 5), (3, 8), (4, 6)])
scatter_chart.add('Group 2', [(1.5, 4), (2.5, 6), (3.5, 7), (4.5, 5)])

# Save the chart to an SVG file
scatter_chart.render_to_file('scatter_plot.svg')
