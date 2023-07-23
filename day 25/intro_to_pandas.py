# with open("./weather_data.csv") as weather_data:
#     data = weather_data.readlines()
# print(data)

# import csv
# weather_data = open("./weather_data.csv")
# data = csv.reader(weather_data)
# temp = []
# for raw in data:
#     print(raw)
# weather_data.close()

import pandas
data = pandas.read_csv("./weather_data.csv")
print(data, data["temp"])
