with open("weather_data.csv","r") as csv_file:
    csv_reader = csv_file.readlines()
    print(csv_reader)

# Instead of above code we use import csv which is already build-in library in python.
# Notes
# data[1:] means: “give me everything except the first item.”

import csv
with open("weather_data.csv", "r") as data_file:
    data = list(csv.reader(data_file))  # Convert iterator to list

    temperatures = []
    for row in data[1:]:  # Skip header row
        row[1] = int(row[1])  # Convert temperature string to integer
        temperatures.append(row[1])

    print(temperatures)

# #--------------------------------------------------------------------------
#
import csv
with open("weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)

    temperatures = []
    for row in data:
         #print(row[1])
         if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

       # Above methods not useful for huge data (more complexity required)

import pandas as pd
data = pd.read_csv("weather_data.csv")   # show data in tabular form.
print(data["temp"])


import pandas as pd
data = pd.read_csv("weather_data.csv")   # show data in tabular form.
# print(type(data))   # <class 'pandas.core.frame.DataFrame'>
# print(type(data["temp"]))    #<class 'pandas.core.series.Series'>

# data_dict = data.to_dict()
# print(data_dict)

# list_data = data["temp"].to_list()
# print(list_data)
# sum1 = sum(list_data)/len(list_data)
# print("Avg = ",sum1)


import pandas as pd
data = pd.read_csv("weather_data.csv")
print(data["temp"].mean())
print(data["temp"].median())
print(data["temp"].mode())
print(data["temp"].max())
print(data["temp"].min())
max_num = data["temp"].max()
print(max_num)

# Get data in column
print(data["condition"])
print(data.condition)    # data.attribute to get hold of the data in that column.

#Get data in row
print(data[data.day == "Monday"])
print(data[data.condition == "Sunny"])

high = data["temp"].max()
print(data[data.temp == high])

print(data[data.temp == data.temp.max()])

#convert monday's temperature into fahrenheit.
monday = data[data.day == "Monday"]
print(monday.condition)
mon_tem = monday.temp[0]
result = mon_tem * 9/5 + 32
print(result)

# create a dataframe from scratch
data = {
    "Name" : ["sakshi", "pranav"],
    "Age" : [20,40],
    "Marks": [33, 20]
}
data = pd.DataFrame(data)
print(data)
# Create the new csv file and store the above data into file
data.to_csv("new_data.csv")