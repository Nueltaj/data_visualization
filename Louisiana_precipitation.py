#retrieve data from a dataset and plot the high and low temperature
import csv
import matplotlib.pyplot as plt 
from datetime import datetime

def read_weather_dataset(filename):
    with open(filename,"r") as file_obj:
        reader= csv.reader(file_obj)
        next(reader)
        
        
        date,precipitation =[],[]
        for row in reader:
            try:
                precipitation_levels=float(row[4])
                current_date = datetime.strptime(row[0],"%Y-%m-%d")
            
            except ValueError:
                print(current_date,"missing data")
                continue
                
            else:
                precipitation.append(precipitation_levels)
                date.append(current_date)
    return date,precipitation
date,precipitation = read_weather_dataset("Louisiana_weather.csv")
           
#plot 
fig = plt.figure()
plt.bar(date,precipitation, color="blue" ,label="total precipitation", alpha = 0.9)
plt.title("Precipitation levels of New Orleans, Louisiana - 2024", fontsize=24,y = 1.05)
plt.xlabel("Date", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitationn (inches/mm)", fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)
plt.legend()
plt.savefig("louisania_precipitation.png", bbox_inches="tight")
plt.show()