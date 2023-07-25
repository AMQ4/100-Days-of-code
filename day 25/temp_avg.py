import pandas

data = pandas.read_csv("./weather_data.csv")
# temp = data["temp"].to_list()
# __sum = sum(ith_temp for ith_temp in temp)
# print("temperature average for this week {:.2f}".format(__sum / len(temp)))

# alternative way with pandas:
print("{:.2f}".format(data["temp"].mean()))
print(data["temp"].max())
