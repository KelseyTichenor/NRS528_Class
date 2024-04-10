
#####
# Step 0 - Practice tasks before we start.
#####

# Express these items as a list using list append (i.e. .append) and print it:

Step0List = []

item1 = "woodlands.shp"
item2 = "marshlands.shp"
item3 = "beaches.shp"

Step0List.append(item1)
Step0List.append(item2)
Step0List.append(item3)
print(Step0List)

# How many files are in the list?

print("There are " + str(len(Step0List)) + " files in this list.")

# Take this list of files (file_list), and using a for loop, go through each file name and change
#   the file extension from shp to csv and print new_extension_file_list.
#   Hint: I would use something like filename.split(".") to extract the filename[0] which would be the
#   part of the name without the extension.

# 1st: you need another empty list

newExtensionStep0List = []

# He asked for a for loop right? Get it going.

for file in Step0List:
    # file_name = you want to keep the original shapefile name
    # .split(".") will erase everything to the right of the period, and the period itself
    file_name = file.split(".")
    # Now we add the ".csv" at the end of the new file name by appending, just like how we did above.
    # Remember list indexing: 0 = the first item in the list
    # Now just repeat for each file in the list.
    newExtensionStep0List.append(file_name[0] + ".csv")
    # newExtensionStep0List.append(file_name[1] + ".csv")
    # newExtensionStep0List.append(file_name[2] + ".csv")

# OH CRAP - the .split function doesn't just erase; it separates the file name into 2 columns;
# One with the original file name, and the other with just the file extension.
# No wonder why file_name[2] triggers an error; the .split function splits into 2 columns, and
# I'm asking for a third out of nowhere. Noted.
# Uncommented out stuff = correct way to do this step.

print(newExtensionStep0List)
