"""
This module retrieves weather data from CSV datasets and plots the high and low temperatures
for Lagos and New York City for the year 2024.
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt


def read_weather_dataset(filename):
    """
    Reads a weather dataset from a CSV file.

    Parameters:
        filename (str): The path to the CSV file.

    Returns:
        tuple: A tuple containing three lists:
            - dates (list of datetime): The dates for the weather data.
            - high_temperatures (list of float): The high temperatures.
            - low_temperatures (list of float): The low temperatures.
    """
    with open(filename, "r", encoding="utf-8") as file_obj:
        reader = csv.reader(file_obj)
        next(reader)  # Skip header

        dates, high_temperatures, low_temperatures = [], [], []
        for row in reader:
            try:
                high_temp = float(row[3])
                low_temp = float(row[2])
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
            except ValueError:
                # Use the original string from the row if conversion fails
                print(row[0], "missing or invalid data")
            else:
                high_temperatures.append(high_temp)
                low_temperatures.append(low_temp)
                dates.append(current_date)
    return dates, high_temperatures, low_temperatures


# Retrieve data for Lagos and New York City
lagos_dates, lagos_highs, lagos_lows = read_weather_dataset("lagos_weather.csv")
nyc_dates, nyc_highs, nyc_lows = read_weather_dataset("new_york_city_weather.csv")

# Plotting the data
fig = plt.figure()
plt.plot(lagos_dates, lagos_highs, c="red", label="High temp. of Lagos", alpha=0.9)
plt.plot(lagos_dates, lagos_lows, c="green", label="Low temp. of Lagos", alpha=0.9)
plt.plot(nyc_dates, nyc_highs, c="orange", label="High temp. of NYC", alpha=0.9)
plt.plot(nyc_dates, nyc_lows, c="blue", label="Low temp. of NYC", alpha=0.9)
plt.ylim(-10, 40)
plt.fill_between(lagos_dates, lagos_highs, lagos_lows, facecolor="green", alpha=0.4)
plt.fill_between(nyc_dates, nyc_highs, nyc_lows, facecolor="blue", alpha=0.4)
plt.title(
    "Comparison of the high-low temperature of Lagos and New York City - 2024",
    fontsize=24,
    y=1.05,
)
plt.xlabel("Date", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (°C)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.legend()
plt.savefig(
    "compare_lagos_weather_to_new_york_city_weather_visualization.png",
    bbox_inches="tight",
)
plt.show()
