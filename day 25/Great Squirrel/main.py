import pandas

# Read the dataset into a DataFrame.
data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Create a dictionary to store squirrel colors and their counts.
squirrel_colors = {}
colors = data["Primary Fur Color"]

# Add the values to the dictionary, incrementing each color count by 1.
for color in colors:
    if color not in squirrel_colors:
        squirrel_colors[color] = 1
    else:
        squirrel_colors[color] += 1

# Initialize a dictionary to represent the final CSV file with color and count data.
squirrel_colors_report = {"color": [], "count": []}

# Loop through the squirrel_colors dictionary and discard 'nan' values if present.
for color in squirrel_colors:
    if type(color) != float:  # Check to discard the `nan` values if there are any.
        squirrel_colors_report["color"].append(color)
        squirrel_colors_report["count"].append(squirrel_colors[color])

# Convert `squirrel_colors_report` to a DataFrame object.
data_report = pandas.DataFrame(squirrel_colors_report)

# Save the DataFrame as a CSV file named "Squirrel_Color_Report.csv" in the current directory.
data_report.to_csv("./Squirrel Color Report/Squirrel_Color_Report.csv")

# We can achieve the same in a few line of code by retrieving all specific color rows by
# data[data.color == "color name"].count()
# with a higher time complexity.
