# with open("weather_data.csv") as source:
#     data = source.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# # A table is called a DataFrame
# print(type(data))
# # This will print the temp column. The temp column in a Series
# print(data['temp'])
#
# # This will convert the DataFrame to a dictionary
# data_dict = data.to_dict()
#
# # This will convert the temp Series to a list
# temp_list = data["temp"].to_list()
#
# # Instead of calculating the average temp like this...
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# # ... we can get the average temp using a Pandas function called .mean()
# print(data['temp'].median())
#
# # So this is how we would get the max temp
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# # Get data in the Row
# print(data[data.day == "Monday"])

# # Challenge: print the Row od data where temp was maximum
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp)

# # Challenge get Monday's temp in Fahrenheit
# monday_temp_in_fahrenheit = monday.temp * 9/5 + 32
# print(monday_temp_in_fahrenheit)

# # Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# color_count = data["Primary Fur Color"].unique()
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

squirrel_count = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Squirrel Count": [black, gray, cinnamon]
}

df = pandas.DataFrame(squirrel_count)
df.to_csv("squirrel_count.csv")
