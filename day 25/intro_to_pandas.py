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
#
import pandas

data = pandas.read_csv("./weather_data.csv")


# print(data)

# to get a data frame of the rows that satisfying a particular condition
# print(data[data.temp == data.temp.max()])

def C_to_F(c):
    return c * 9 / 5 + 32


# to get the temp on monday in F.
print(C_to_F(data[data.day == "Monday"].temp))
