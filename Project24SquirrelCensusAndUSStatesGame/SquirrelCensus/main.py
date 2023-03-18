# with open("weather_data.csv") as weather_file:
#     weather = weather_file.readlines()

# import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     print(data)
# #     # for row in data:
# #     #     print(row)
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 1.8 + 32
# print(monday_temp_F)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, red, black]
}
data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")