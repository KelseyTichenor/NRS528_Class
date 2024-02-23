# Coding Challenge 3: Part 3

# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions
# from quasi-continuous daily measurements at Mauna Loa, Hawaii dataset,
# Use Python (csv) calculate the following:

# 1. Annual average for each year in the dataset.

import csv

years = []
entire_co2_dataset = []
Jan = 1
Feb = 2
Mar = 3
Apr = 4
May = 5
Jun = 6
Jul = 7
Aug = 8
Sep = 9
Oct = 10
Nov = 11
Dec = 12
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
winter = [12,1,2]

with open("co2-ppm-daily.csv") as co2csv:
    next(co2csv)
    for row in csv.reader(co2csv, delimiter=','):
        year = row[0].split("-")[0]
        month = row[0].split("-")[1]
        entire_co2_dataset.append(float(row[1]))
        if year not in years:
            years.append(year)

# 1. Annual average
for year in years:
    co2values = []
    with open("co2-ppm-daily.csv") as co2csv:
        next(co2csv)
        for row in csv.reader(co2csv, delimiter=','):
            row_year = row[0].split("-")[0]
            if row_year == year:
                co2values.append(float(row[1]))
    print(str(year) + ": " + str(sum(co2values)/len(co2values)))

# 2. Minimum, maximum and average for the entire dataset.
print(str("The min for this dataset is " + str(min(entire_co2_dataset))))
print(str("The max for this dataset is " + str(max(entire_co2_dataset))))
print(str("The mean for this dataset is " + str(sum(entire_co2_dataset)/len(entire_co2_dataset))))

# 3. Seasonal average of:
#       Spring (March, April, May),
#       Summer (June, July, August) (summer = june + july + august),
#       Autumn (September, October, November)
#       and Winter (December, January, February).
print(month)
# 4. Calculate the anomaly for each value in the dataset (average minus value)
#       relative to the mean for the entire time series.
#
# #######
# Notes:
# Set up the dataset the right way before attemoting to answer any questions.
#
