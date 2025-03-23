import csv
import matplotlib.pyplot as plt
from datetime import datetime

# get high temperature from the file
filename = "new_york_city_weather.csv"
with open(filename, "r") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # initialize the list
    date, low_temperature, high_temperature = [], [], []
    # reads every line in the file
    for row in reader:
        try:
            # convert string to int
            high_temp=float(row[3])
            low_temp=float(row[2])
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
        except ValueError:
            print(current_date, "missing data")
            continue
            
        else:
            high_temperature.append(high_temp)
            january_temperature = high_temperature[0:31]
            
            low_temperature.append(low_temp)
            
            date.append(current_date)
            january_date = date[:31]

# plot
fig = plt.figure()
plt.plot(date, high_temperature, c="red", label="High_temp",alpha =0.5)
plt.plot(date, low_temperature, c="blue", label="Low_temp", alpha = 0.5)
plt.ylim(-10,40)
plt.fill_between(date,high_temperature,low_temperature, facecolor="blue", alpha = 0.1)
plt.title("Daily High Temperature and Low Temperature - 2024\n New York City, USA", fontsize=24)
plt.ylabel(" Temperature (F)", fontsize=16)
plt.xlabel("Date", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis="both", which="major", labelsize=16)
plt.legend()
plt.savefig("New_york_city_high_low_temperature_visual.png", bbox_inches="tight")
plt.show()
