# Coding Challenge 4: Let's run the 'near' tool using nothing but Python code!

# Requirements:
# 1. Code must be commented well.
# 2. Code must be able to run on any machine, changing only a base folder location.

# I saw there was a dataset for leaking storage tanks,
#   as well as a dataset for the 2020 wetlands inventory.
# Both datasets came from RIGIS.
# Using the near tool, I want to see how close these leaking underground tanks are to wetlands.
#   I arbitrarily chose a distance of 250 meters, just to see what comes up.

# Step 0: I 100% took this code from example 2 on Esri's Tool Reference page.
# Step 1: Import arcpy
# Step 2: Set a workspace environment
# Step 3: Set local variables
#       Required: in_features, near_features
#       Optional: search_radius, location, angle, and method (like geodesic, etc)
# Step 4: Execute the Function and hope for the best

import arcpy
arcpy.env.workspace = r"C:\GitHub\NRS528_Class\NRS_528_Coding_Challenge_4"
arcpy.env.scratchWorkspace = r"C:\GitHub\NRS528_Class\NRS_528_Coding_Challenge_4"
arcpy.AddMessage("The passed-down current workspace is: %s" % arcpy.env.workspace)
arcpy.AddMessage("The passed-down scratch workspace is: %s" % arcpy.env.scratchWorkspace)
try:
    in_features = r"C:\GitHub\NRS528_Class\NRS_528_Coding_Challenge_4\Leaking_Underground_Storage_Tanks\Leaking_Underground_Storage_Tanks.shp"
    near_features = r"C:\GitHub\NRS528_Class\NRS_528_Coding_Challenge_4\Wetlands_2020\Wetlands_2020.shp"
    search_radius = "250 Meters"
    location = "#"
    angle = "#"
    method = "GEODESIC"
    arcpy.Near_analysis(in_features, near_features, search_radius, location, angle, method)

    # get geoprocessing messages
    print(arcpy.GetMessages())

except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))

except Exception as err:
    print(err.args[0])
