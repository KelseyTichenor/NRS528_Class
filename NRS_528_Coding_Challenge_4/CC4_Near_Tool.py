# Coding Challenge 4: Let's run the 'near' tool using nothing but Python code!

# Requirements:
# 1. Code must be commented well.
# 2. Code must be able to run on any machine, changing only a base folder location.

################################

# UPDATE! Coding Challenge 8: Convert this code into a function
# Requirements:
# 1. You must do more than one thing to your input to the function
# 2. The function must take two arguments or more
# 3. Provide a zip file of your example data within your repo

################################

# I saw there was a dataset for leaking storage tanks,
#   as well as a dataset for the 2020 wetlands inventory.
# Both datasets came from RIGIS.
# Using the near tool, I want to see how close these leaking underground tanks are to wetlands.
#   I arbitrarily chose a distance of 100 meters, just to see what comes up.

# Step 0: I 100% took this code from example 2 on Esri's Tool Reference page.
# Step 1: Import arcpy
# Step 2: Set up a workspace environment(s)
# Step 3: Set local variables (filepaths should all fit on one line)
#                             (I tried using 2 lines: got Error 000732; filepath doesn't exist)
#       Required: in_features, near_features
#       Optional: search_radius, location, angle, and method (like geodesic, etc)
# Step 4: Print using 'print(arcpy.GetMessages())'
#       According to Esri, there are 3 types of messages:
#           0 = Informative, warning, and error messages are returned.
#           1 = Only warning and error messages are returned.
#           2 = Only error messages are returned.
#           I presume leaving nothing inside the brackets is the same as '0'.
# Step 5: Execute the Function and hope for the best

import os
import arcpy
# Base_Path = "C:/GitHub/NRS528_Class/NRS_528_Coding_Challenge_4"
# arcpy.env.workspace = Base_Path
# arcpy.env.scratchWorkspace = Base_Path
# arcpy.AddMessage("The passed-down current workspace is: %s" % arcpy.env.workspace)
# arcpy.AddMessage("The passed-down scratch workspace is: %s" % arcpy.env.scratchWorkspace)
def describe_wetlands(input_shapefile):
    desc = arcpy.Describe(input_shapefile)
    print("Describing: " + str(input_shapefile))
    if arcpy.Exists(input_shapefile):
        if desc.dataType == "ShapeFile":
            print("Feature Type:  " + desc.shapeType)
            print("Coordinate System Type:  " + desc.spatialReference.type)
            print("Coordinate System used:  " + desc.spatialReference.GCSName)
        else:
            print("Input data not ShapeFile..")
    else:
        print("Dataset not found, please check the file path..")

input_shapefile = r"C:\Data\Course_ArcGIS_Python\Classes\08_Functions\DataFolder_Step_5_Data\Places.shp"
describe_shp(input_shapefile)

# Commented-Out Coding Challenge 4 Code for reference:

# Base_Path = "C:/GitHub/NRS528_Class/NRS_528_Coding_Challenge_4"
# arcpy.env.workspace = Base_Path
# arcpy.env.scratchWorkspace = Base_Path
# arcpy.AddMessage("The passed-down current workspace is: %s" % arcpy.env.workspace)
# arcpy.AddMessage("The passed-down scratch workspace is: %s" % arcpy.env.scratchWorkspace)
#
# try:
#     in_features = os.path.join(Base_Path,
#                                "Leaking_Underground_Storage_Tanks", "Leaking_Underground_Storage_Tanks.shp")
#     near_features = os.path.join(Base_Path, "Wetlands_2020", "Wetlands_2020.shp")
#     search_radius = "100 Meters"
#     location = "#"
#     angle = "#"
#     method = "GEODESIC"
#     arcpy.Near_analysis(in_features, near_features, search_radius, location, angle, method)
#     # time to get geoprocessing messages:
#     print(arcpy.GetMessages())
#
# except arcpy.ExecuteError:
#     print(arcpy.GetMessages(2))
#
# except Exception as err:
#     print(err.args[0])
