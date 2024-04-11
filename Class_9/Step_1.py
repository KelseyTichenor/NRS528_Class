
#####
# Step 1 - Data Access module
#####

# Cursors are a way that Arcpy interacts with tables

# You can programmatically interact with attribute tables using the data access module. It's easy, fast
# and powerful, allowing you direct access to data with only a few lines of code.

# The code is similar to how we would interact with a CSV file using the CSV package. For example:

# Using data that I obtained from: https://catalog.data.gov/dataset/sandhill-crane-locations-autumn-2013-migration
# lets read in each record, and count how many records there are for crane number 100840:

# Step 1
import csv
# Step 2: Open a CSV file and give it a reference name. Note that this is a function of sorts.
with open(r"Step_1.csv") as crane_csv:
    # Step 2.1: csv_reader = csv.reader (is a function) (x_csv, delimiter = ',')
    # Remember, a delimiter is what separates the columns of the CSV - in this case, a comma
    # because it's a COMMA separated value.
    csv_reader = csv.reader(crane_csv, delimiter=',')
    # Step 2.2: line count = a variable - but we start with 0 to give us a blank slate
    # for what we're about to do.
    line_count = 0
    # Step 2.3: Start a For Loop.
    for row in csv_reader:
        if row[0] == "100840":
            line_count += 1
            # Meaning, for every row with the above identifier in it, add +1 to the count.

# Verify your counts with a print statement.
print("There are " + str(line_count) + " csv records for crane 100840.")

# Uncomment the below, now let's now do the same using arcpy.da (arcpy data access module), you could of course
# use select and get count but we are doing it the hard way!:

# Step 1: Import arcpy - since we're gonna try to do this without the CSV module.
# import arcpy
# # Step 2: Another line count variable, but this one is named differently so as not to confuse with what's above
# line_count_da = 0
# # Step 3: Start another for loop:
# with arcpy.da.SearchCursor("Step_1.csv", ['Crane', 'Time', 'X', 'Y']) as cursor:
#     # crane, time, x, and y are the column names:
#     # you need to know the basics about your CSV before you code with it!
#     # as cursor: I think this is just a variable?
#     # You can call it whatever - I'm probably just gonna leave it as cursor to keep things easy
#     for row in cursor:
#         if row[0] == 100840:
#             line_count_da += 1
#             # Notice that the above 3 lines are very similar to what you'd do for the import CSV module.
# print("There are " + str(line_count_da) + " arcpy.da records for crane 100840.")
# Notice that this gives you the same result as the import csv module does.


# Task - Using arcpy.da, count how many individual cranes there are in the Step_1.csv data (hint: 5), and
# extract their identification numbers and the number of records for each crane
#   (hint: 100840, 100843, 100845, 100853, 100854).

# Think about what you need to do: 1: Run through each row, pull the crane, add it to a list,
# then 2: for each item in your generated list, add it to a dict, count occurrences and then 3: print your len(dict)
# and print dict.

# Here's some helper code to help you do the count, but first you must generate the list of cranes (hint: append to a
# crane list)!
# crane_count={}
# for i in YOUR_LIST_HERE:
#     if crane == row[0]:
#         if i not in crane_count.keys():
#             crane_count[i]=1  #also: if not i in d
#         else:
#             crane_count[i]+=1
import arcpy
# Step 1: create an empty list to append stuff to
crane_list = []
crane_count = {}
with arcpy.da.SearchCursor("Step_1.csv", ['Crane', 'Time', 'X', 'Y']) as cursor:
    for row in cursor:
        if row[0] not in crane_list:
            crane_list.append(row[0])
print(crane_list)
print(len(crane_list))

