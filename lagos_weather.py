#retrieve data from a dataset and plot the high and low temperature
import csv
import matplotlib.pyplot as plt 
from datetime import datetime

filename ="lagos_weather.csv"
with open(filename,"r") as file_obj:
    reader= csv.reader(file_obj)
    header_row = next(reader)
    
    
    date,high_temperature,low_temperature =[],[],[]
    for row in reader:
        try:
            high_temp=float(row[3])
            low_temp=float(row[2])
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
        
        except ValueError:
            print(current_date,"missing data")
            
        else:
            high_temperature.append(high_temp)
            low_temperature.append(low_temp)
            date.append(current_date)
            
#plot 
fig = plt.figure()
plt.plot(date,high_temperature, c="red" ,label="High_temp", alpha = 0.5)
plt.plot(date,low_temperature,c="blue", label="Low_temp" ,alpha=0.5)
plt.ylim(-10, 40)
plt.fill_between(date,high_temperature, low_temperature, facecolor= "blue", alpha = 0.1)
plt.title("Daily High Temperature and Low Temperature - 2024\n Lagos,Nigeria", fontsize=24)
plt.xlabel("Date", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (°C)", fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)
plt.legend()
plt.savefig("lagos_high_low_temperature_visual.png", bbox_inches="tight")
plt.show()