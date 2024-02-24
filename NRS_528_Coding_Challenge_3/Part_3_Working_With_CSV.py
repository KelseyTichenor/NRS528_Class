# Coding Challenge 3: Part 3

# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions
# from quasi-continuous daily measurements at Mauna Loa, Hawaii dataset,
# Use Python (csv) calculate the following:

# 1. Annual average for each year in the dataset.

import csv

years = []
entire_co2_dataset = []
springCo2 = []
summerCo2 = []
autumnCo2 = []
winterCo2 = []

# General File Setup:

with open("co2-ppm-daily.csv") as co2csv:
    next(co2csv)
    for row in csv.reader(co2csv, delimiter=','):
        year = row[0].split("-")[0]
        entire_co2_dataset.append(float(row[1]))
        if year not in years:
            years.append(year)

# Seasonal File Setup:

# Spring:
with open("co2-ppm-daily.csv") as co2csv:
    next(co2csv)
    for row in csv.reader(co2csv, delimiter=','):
        month = row[0].split("-")[1]
        if month == "03":
             springCo2.append(float(row[1]))
        elif month == "04":
            springCo2.append(float(row[1]))
        elif month == "05":
            springCo2.append(float(row[1]))

# Summer:
with open("co2-ppm-daily.csv") as co2csv:
    next(co2csv)
    for row in csv.reader(co2csv, delimiter=','):
        month = row[0].split("-")[1]
        if month == "06":
            summerCo2.append(float(row[1]))
        elif month == "07":
            summerCo2.append(float(row[1]))
        elif month == "08":
            summerCo2.append(float(row[1]))

# Autumn:
with open("co2-ppm-daily.csv") as co2csv:
    next(co2csv)
    for row in csv.reader(co2csv, delimiter=','):
        month = row[0].split("-")[1]
        if month == "09":
            autumnCo2.append(float(row[1]))
        elif month == "10":
            autumnCo2.append(float(row[1]))
        elif month == "11":
            autumnCo2.append(float(row[1]))

# Winter:
with open("co2-ppm-daily.csv") as co2csv:
    next(co2csv)
    for row in csv.reader(co2csv, delimiter=','):
        month = row[0].split("-")[1]
        if month == "12":
            winterCo2.append(float(row[1]))
        elif month == "01":
            winterCo2.append(float(row[1]))
        elif month == "02":
            winterCo2.append(float(row[1]))

# Sanity Check:
    print(len(springCo2))
    print(len(summerCo2))
    print(len(autumnCo2))
    print(len(winterCo2))

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
print(str("Average Spring CO2: " + str(sum(springCo2)/len(springCo2))))
print(str("Average Summer CO2: " + str(sum(summerCo2)/len(summerCo2))))
print(str("Average Autumn CO2: " + str(sum(autumnCo2)/len(autumnCo2))))
print(str("Average Winter CO2: " + str(sum(winterCo2)/len(winterCo2))))

# 4. Calculate the anomaly for each value in the dataset (average minus value)
#       relative to the mean for the entire time series.


# #######
# Notes:
# Set up the dataset the right way before attempting to answer any questions.
# It's important to know how the CSV should work before trying to code with it
