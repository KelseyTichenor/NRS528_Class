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

import arcpy

input_shp = r'C:\GitHub\NRS528_Class\NRS_528_Coding_Challenge_9\CC9_Data\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'
fields = ['Site', 'Species', 'Other']

# expression = arcpy.AddFieldDelimiters(input_shp, 'Other') + " = PHOTO" or ' = Photo' or ' = Photos'

with arcpy.da.SearchCursor(input_shp, fields) as cursor:
    for row in cursor:
        print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
