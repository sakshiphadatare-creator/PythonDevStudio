import pandas
data = pandas.read_csv("2018_central_park_squirrel_census_-_squirrel_data.csv")
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])   # this line check the current value is present or not(True/False) data[] it's show whole data.
Black_squirrel = len(data[data["Primary Fur Color"] == "Black" ])
print(gray_squirrel)
print(Cinnamon_squirrel)
print(Black_squirrel)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel, Cinnamon_squirrel, Black_squirrel]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
