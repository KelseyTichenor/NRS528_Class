# Coding Challenge 8: Convert your Coding Challenge 4 code into a function

# Requirements:
# 1. You must do more than one thing to your input to the function
# 2. The function must take two arguments or more
# 3. Provide a zip file of your example data within your repo

################################

# First, import os and arcpy, then set up base paths, workspaces, etc
import os
import arcpy
Base_Path = "C:/GitHub/NRS528_Class/NRS_528_Coding_Challenge_8"
arcpy.env.workspace = Base_Path
arcpy.env.scratchWorkspace = Base_Path
arcpy.AddMessage("The passed-down current workspace is: %s" % arcpy.env.workspace)
arcpy.AddMessage("The passed-down scratch workspace is: %s" % arcpy.env.scratchWorkspace)

# I'm starting to like printing empty print statements - the code that's returned looks much cleaner this way.
print()


def find_tanks_near_wetlands(input_wetlands_shapefile, input_tanks_shapefile):
    descWetlands = arcpy.Describe(input_wetlands_shapefile)
    descTanks = arcpy.Describe(input_tanks_shapefile)
    # This is me trying to combine the describing of both datasets used into one function.
    # Also using '\n' to break up the line when it comes out. Again, cleaner code
    print("Describing: " + str(input_wetlands_shapefile) + "\nand\n" + str(input_tanks_shapefile))
    # Another empty print statement
    print()
    if arcpy.Exists(input_wetlands_shapefile) and arcpy.Exists(input_tanks_shapefile):
        if descWetlands.dataType and descTanks.dataType == "ShapeFile":
            print("Wetlands Feature Type:  " + descWetlands.shapeType)
            print("Wetlands Coordinate System Type:  " + descWetlands.spatialReference.type)
            print("Wetlands Coordinate System used:  " + descWetlands.spatialReference.GCSName)
            print()
            print("Tanks Feature Type:  " + descTanks.shapeType)
            print("Tanks Coordinate System Type:  " + descTanks.spatialReference.type)
            print("Tanks Coordinate System used:  " + descTanks.spatialReference.GCSName)
            print()
            # Now time to run the Near tool - should indent this to make this part stand out?
            # The code looks like it works regardless.
            print("Finding all the leaking underground storage tanks 100 meters away from a Rhode Island wetland...")
            # This is the same Esri-supplied code used in Coding Challenge 4, modified with the data I'm using.
            # Turns out, no try/except statements are needed to make it run. Surprise!
            in_features = os.path.join(Base_Path,
                                       "Leaking_Underground_Storage_Tanks", "Leaking_Underground_Storage_Tanks.shp")
            near_features = os.path.join(Base_Path, "Wetlands_2020", "Wetlands_2020.shp")
            search_radius = "100 Meters"
            location = "#"
            angle = "#"
            method = "GEODESIC"
            arcpy.Near_analysis(in_features, near_features, search_radius, location, angle, method)
            # time to get geoprocessing messages:
            print(arcpy.GetMessages())

        else:
            print("Input data not ShapeFile..")
    else:
        print("Datasets not found, please check the file path..")

# Defining the wetlands shapefile and leaking tank shapefile
# Boy do I love os.path.join. Thanks for showing us this Andy!

input_wetlands_shapefile = os.path.join(Base_Path, "Wetlands_2020", "Wetlands_2020.shp")
input_tanks_shapefile = os.path.join(Base_Path,
                                     "Leaking_Underground_Storage_Tanks", "Leaking_Underground_Storage_Tanks.shp")

# Now it's finally time to call the function:

find_tanks_near_wetlands(input_wetlands_shapefile, input_tanks_shapefile)

# I'm proud of how this turned out <3
# Thanks for the great video!

##################################

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
