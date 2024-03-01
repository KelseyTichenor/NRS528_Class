#####
# Step 1 - Executing and reporting tool outputs
#####

# Part a - convert CSV to shapefile
# In ArcGIS:
# The csv should be given - drag and drop the file into ArcGIS
# to convert it to a shapefile, right click > create points from table > XY Table To Point (creates a file)

# Help on Tool: http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/make-xy-event-layer.htm.
# Using the data Step_1_Lionfish.csv, we will use arcpy to convert this to a shapefile.
# You should see 2 points

import arcpy
# Set your workspace to the directory where you are storing your CSV files
# Stay in pycharm, go to the browser window > file name > copy and paste
# arcpy.env.workspace = r"E:\Kelsey_Tichenor_NRS_528\GitHub\NRS528_Class\Class_5\Step_1_Lionfish.csv"
# arcpy.env.overwriteOutput = True
#
# in_Table = r"Step_1_Lionfish.csv"
# x_coords = "X"
# y_coords = "Y"
# z_coords = ""
# out_Layer = "lionfish" (will get deleted by RAM, this is the in-memory layer, so the name doesn't really matter)
# saved_Layer = r"E:\Kelsey_Tichenor_NRS_528\GitHub\NRS528_Class\Class_5\Step_1_Lionfish_Output.shp"
#       The saved_Layer is what's going to matter.
#
# # Set the spatial reference
# spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
#
# lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
#
# # Print the total rows
# print(arcpy.GetCount_management(lyr))
#
# # Save to a layer file
# arcpy.CopyFeatures_management(lyr, saved_Layer)
#
# if arcpy.Exists(saved_Layer):
#     print("Created file successfully!")


# Tasks - Using the file provided "Step_1_Deep_Coral.csv", undertake the following: Hint: spatial
# reference is the same as above, i.e. WGS 1984.

##### 1. Convert the file to a shapefile.
arcpy.env.workspace = r"C:\GitHub\NRS528_Class\Class_5\Step_1_Deep_Coral.csv"
arcpy.env.overwriteOutput = True


in_Table = r"Step_1_Deep_Coral.csv"
# It's already referenced in the workspace, so the relative path will work OK here.
x_coords = "decimalLongitude"
y_coords = "decimalLatitude"
# At first, I transposed latitude and longitude - are they supposed to be backwards in this situation?
z_coords = ""
out_Layer = "Deep Coral"
saved_Layer = r"C:\GitHub\NRS528_Class\Class_5\Step_1_Deep_Coral_Output.shp"

# Set the spatial reference
spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

# Save to a layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)

if arcpy.Exists(saved_Layer):
    print("Created file successfully!")

##### 2. Print the count of the number of records in the file. (Hint: see above - get count mgmt!)
# https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/get-count.htm
# Print the total rows
print("There are " + str(arcpy.GetCount_management(lyr)) + " rows in this CSV.")

##### 3. Check the correct coordinate system has been applied (Hint: see last week - describe tool!)

desc = arcpy.Describe(r"C:\GitHub\NRS528_Class\Class_5\Step_1_Deep_Coral_Output.shp")
print(desc.spatialReference.name)
print("Extent:\n XMin: {0},\n XMax: {1},\n YMin: {2},\n YMax: {3}".format(desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax))

##### 4. Visualize the file in ArcPro by dragging it into the program.
# DONE :D

# Step 1: Priority: create file and set up references to things
# The other steps should just build off the references you already did, and shouldn't be more than a few lines.

