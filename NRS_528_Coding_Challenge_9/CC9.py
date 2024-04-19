# Coding Challenge 9:

# In this coding challenge, your objective is to utilize the arcpy.da module
#    to undertake some basic partitioning of your dataset.

# In this coding challenge, I want you to work with the Forest Health Works dataset from RI GIS
# (I have provided this as a downloadable ZIP file in this repository).

# Using the arcpy.da module (yes, there are other ways and better tools to do this),
# I want you to extract all sites that have a photo of the invasive species (Field: PHOTO) into a new Shapefile,
# and do some basic counts of the dataset.

# In summary, please address the following:

# 1. Count how many individual records have photos, and how many do not (2 numbers), print the results.
# 2. Count how many unique species there are in the dataset, print the result.
# 3. Generate two shapefiles, one with photos and the other without.

import os
import arcpy

basePath = r'C:\GitHub\NRS528_Class\NRS_528_Coding_Challenge_9\CC9_Data'
input_shp = os.path.join(basePath, 'RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp')
fields = ['Site', 'Species', 'Other']
unique_species = []
desc = arcpy.Describe(input_shp)

expression = arcpy.AddFieldDelimiters(input_shp, 'Other') + " = PHOTO" or ' = Photo' or ' = Photos'

# Part 1: Counting how many individual records have photos, and how many do not
with arcpy.da.SearchCursor(input_shp, fields) as cursor:
    count_1 = 0
    for row in cursor:
        # print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
        count_1 = count_1 + 1
# Printing the first number
print("No expression: " + str(count_1))

with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    count_1 = 0
    for row in cursor:
        # print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
        count_1 = count_1 + 1
# Printing the second number
print("Expression: " + str(count_1))



# Part 2: Counting the number of unique species in the dataset
with arcpy.da.SearchCursor(input_shp, fields) as cursor:
    for row in cursor:
        if row[1] not in unique_species:
            unique_species.append(row[1])
# Row 1 refers to row 1 in the cursor (which is the Species column in the dataset)
# Printing the result, but not without making sure the code works, using another print statement
print(unique_species)
print("Number of unique species = " + str(len(unique_species)))



# Part 3: Generating two shapefiles: one with photos and one without
#
# To create an empty shapefile, first set the workspace (should be listed at the start of the file)
#
# Use Describe to get a SpatialReference object:
print(desc.spatialReference.name)
print(desc.spatialReference.type)
#
# Let's make some directories these things can live in, because good file management is important:
if not os.path.exists(os.path.join(basePath, "Invasives_Data_With_Photos")):
    os.mkdir(os.path.join(basePath, "Invasives_Data_With_Photos"))
    print("Directory for shapefile with photos created")
else: print("This directory already exists")

if not os.path.exists(os.path.join(basePath, "Invasives_Data_WITHOUT_Photos")):
    os.mkdir(os.path.join(basePath, "Invasives_Data_WITHOUT_Photos"))
    print("Directory for shapefile without photos created")
else: print("This directory already exists")

# Set local variables:

out_path = os.path.join(basePath, "Invasives_Data_With_Photos")
out_name = "Invasives_With_Photos.shp"
geometry_type = "POINT"
template = "#"
has_m = "DISABLED"
has_z = "DISABLED"
spatial_ref = 4326

# Execute CreateFeatureclass (With Photos)
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                    has_m, has_z, spatial_ref)

print("Shapefile with photos created")

out_path = os.path.join(basePath, "Invasives_Data_WITHOUT_Photos")
out_name = "Invasives_Without_Photos.shp"
geometry_type = "POINT"
template = "#"
has_m = "DISABLED"
has_z = "DISABLED"
spatial_ref = 4326

# Execute CreateFeatureclass (Without Photos)
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                    has_m, has_z, spatial_ref)

print("Shapefile without photos created")

# Now we have the blank shapefiles we need. Let's add the photo data to them using the arcpy.da.InsertCursor function.
# Might be stealing some code from
#       https://community.esri.com/t5/geoprocessing-questions/converting-contours-to-points/td-p/521512#449508
#       and the concept of how to use it from:
#       https://community.esri.com/t5/python-questions/use-insertcursor-to-copy-geometry-from-one-dataset/td-p/84671

input_shp_photos = os.path.join(basePath, "Invasives_Data_With_Photos", "Invasives_With_Photos.shp")
fields = ['Site', 'Species', 'Other']
expression = arcpy.AddFieldDelimiters(input_shp, 'Other') + " = PHOTO" or ' = Photo' or ' = Photos'
with arcpy.da.InsertCursor(input_shp_photos, fields, expression) as out_cursor:
    with arcpy.da.SearchCursor(input_shp_photos, fields, expression) as in_cursor:
        for row in in_cursor:
            if row[1] not in out_cursor:
                out_cursor.insertRow(row)
print("Hope this works!")
# Spoiler alert: this code doesn't work at all - I didn't think I needed to use the trig stuff here
#       because this is meant to be a point feature class, but should I be using the trig stuff?
