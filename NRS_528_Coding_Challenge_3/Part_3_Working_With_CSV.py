# Coding Challenge 3: Part 3

# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions
# from quasi-continuous daily measurements at Mauna Loa, Hawaii dataset,
# Use Python (csv) calculate the following:
#
# 1. Annual average for each year in the dataset.
# 2. Minimum, maximum and average for the entire dataset.
# 3. Seasonal average of:
#       Spring (March, April, May),
#       Summer (June, July, August),
#       Autumn (September, October, November)
#       and Winter (December, January, February).
# 4. Calculate the anomaly for each value in the dataset
#       relative to the mean for the entire time series.

import pandas

years = []
co2_Values = []

with open("co2-ppm-daily.csv") as co2_csv:
    next(co2_csv) #skip first line
    for row in co2_csv:
        years.append(row[3])
        co2_Values.append(row[1])
        print(row)
    #     total += float(row[3]) #3 = 4th column, in this case, population, remember Python uses zero indexing
    # print(format(total, 'f')) # format prints as float
    # print(total) # without we print as engineering notation
print(years)
print(co2_Values)

# Okay, why is Pycharm treating each number in the dataset like it's its own row?
# For the year 1958: Row 0 = 1, Row 1 = 9, Row 2 = 5, Row 3 = 8