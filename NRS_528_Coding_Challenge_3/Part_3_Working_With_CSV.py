# Coding Challenge 3: Part 3

# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions
# from quasi-continuous daily measurements at Mauna Loa, Hawaii dataset,
# Use Python (csv) calculate the following:

# 1. Annual average for each year in the dataset.

import csv

years = []
co2values = []

with open("co2-ppm-daily.csv") as co2csv:
    next(co2csv)
    for row in csv.reader(co2csv, delimiter='-'):
        if row[0] not in years:
            years.append(row[0])

    for year in years:
        with open("co2-ppm-daily.csv") as co2csv:
            saved_header = next(co2csv)
            file = open(r"years/" + year + ".txt", "w")
            file.write(saved_header)
            for row in csv.reader(co2csv):
                if year == row[0]:
                    file.write(", ".join(row))
                    file.write("\n")
            file.close()

with open("co2-ppm-daily.csv") as co2csv:
    next(co2csv)
    for row in csv.reader(co2csv):
            co2values.append(row[1])

# print(len(years))
# print(years)
# print(co2values)

# 2. Minimum, maximum and average for the entire dataset.
# 3. Seasonal average of:
#       Spring (March, April, May),
#       Summer (June, July, August),
#       Autumn (September, October, November)
#       and Winter (December, January, February).
# 4. Calculate the anomaly for each value in the dataset
#       relative to the mean for the entire time series.

#######

# Need 'import csv' in order to actually use the CSV properly
# delimiter: I noticed that '-' let me isolate just the years,
#       which is what I wanted for Question 1.
# Not sure how to separate months from days from years in the 'date' row
#       The delimiter seemed to do this, but it doesn't separate the data at all.
# Creating two separate loops will create a list of years and list of CO2 values.
# Starting on Line 20 and ending Line 29: code from Task 3 - Final Task Video
#       Not recording years in each file, because date components not separated?
#       Tried positioning this block after the block on Line 31: same result
