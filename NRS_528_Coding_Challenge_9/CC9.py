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

basePath = r'H:\NRS528_2024\Kelsey_Tichenor\NRS_528_Coding_Challenge_9\CC9_Data'
input_shp = os.path.join(basePath, 'RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp')
fields = ['Site', 'Species', 'Other']
unique_species = []
desc = arcpy.Describe(input_shp)


# Part 1: Counting how many individual records have photos, and how many do not
expressionNone = arcpy.AddFieldDelimiters(input_shp, 'Other') + "NOT LIKE 'PHOTO'"
with arcpy.da.SearchCursor(input_shp, fields, expressionNone) as cursorN:
    count_1 = 0
    for row in cursorN:
        count_1 = count_1 + 1
# Printing the number of records without photos
print("Number of records without photos: " + str(count_1))

expressionPhotos = arcpy.AddFieldDelimiters(input_shp, 'Other') + " = PHOTO"
with arcpy.da.SearchCursor(input_shp, fields, expressionPhotos) as cursor:
    count_2 = 0
    for row in cursor:
        count_2 = count_2 + 1
# Printing the number of records with photos
print("Number of records with photos: " + str(count_2))

#######

# Part 2: Counting the number of unique species in the dataset
with arcpy.da.SearchCursor(input_shp, fields) as cursor:
    for row in cursor:
        if row[1] not in unique_species:
            unique_species.append(row[1])
# Row 1 refers to row 1 in the cursor (which is the Species column in the dataset)
# Printing the result, but not without making sure the code works, using another print statement
print(unique_species)
print("Number of unique species: " + str(len(unique_species)))

#######

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

# Invasive Species With Photos
OutputFeatureP = os.path.join(basePath, "Invasives_Data_With_Photos", "Invasives_With_Photos.shp")
cur = arcpy.InsertCursor(OutputFeatureP)
feat = cur.newRow()
fields = ['Site', 'Species', 'Other']
expressionP = arcpy.AddFieldDelimiters(input_shp, 'Other') + " = PHOTO "
with arcpy.da.InsertCursor(OutputFeatureP, fields, expressionP) as p_out_cursor:
    with arcpy.da.SearchCursor(input_shp, fields, expressionP) as p_in_cursor:
        # Yes, I'm referencing the original RIGIS forest data from the beginning of the file
        for row in p_in_cursor:
            cur.insertRow(feat)
print("Hope this works!")

# Invasive Species Without Photos

OutputFeatureN = os.path.join(basePath, "Invasives_Data_WITHOUT_Photos", "Invasives_Without_Photos.shp")
cur = arcpy.InsertCursor(OutputFeatureN)
feat = cur.newRow()
fields = ['Site', 'Species', 'Other']
expressionN = arcpy.AddFieldDelimiters(input_shp, 'Other') + "NOT LIKE 'PHOTO'"
with arcpy.da.InsertCursor(OutputFeatureN, fields, expressionN) as out_cursor:
    with arcpy.da.SearchCursor(input_shp, fields, expressionN) as in_cursor:
        for row in in_cursor:
            cur.insertRow(feat)
print("Hope this works!")
