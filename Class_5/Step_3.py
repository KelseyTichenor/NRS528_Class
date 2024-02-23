#####
# Step 3 - Executing multiple tools - and automating most of it
#####

# We will use the exact same approach to generate a heatmap from a CSV file, but this time
# You will have to automate the extraction of start extent, opposite corner etc for the fishnet
# generation. I have given hints, but everything you are using here has been shown in last week's
# and this week's session.

# Using Step_3_Cepphus_grylle.csv:

# 1. Convert Step_3_Cepphus_grylle.csv to a shapefile.

import arcpy

arcpy.env.workspace = r"E:\Kelsey_Tichenor_NRS_528\GitHub\NRS528_Class\Class_5"
arcpy.env.overwriteOutput = True

in_Table = r"Step_3_Cepphus_grylle.csv"
# It's already referenced in the workspace, so the relative path will work OK here.
x_coords = "lon"
y_coords = "lat"
# At first, I transposed latitude and longitude - are they supposed to be backwards in this situation?
z_coords = ""
out_Layer = "Cepphus Grylle"
saved_Layer = r"E:\Kelsey_Tichenor_NRS_528\GitHub\NRS528_Class\Class_5\Step_3_Cepphus_grylle.shp"

# Set the spatial reference
spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

# Save to a layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)

if arcpy.Exists(saved_Layer):
    print("Created file successfully!")

# 2. Extact the Extent, i.e. XMin, XMax, YMin, YMax of the generated Cepphus_grylle shapefile.
desc = arcpy.Describe(r"E:\Kelsey_Tichenor_NRS_528\GitHub\NRS528_Class\Class_5\Step_3_Cepphus_grylle.shp")
# print(desc.extent) - but string substitution notation makes things more accessible, so let's do this instead:
print("Extent:\n  XMin: {0},\n XMax: {1},\n YMin: {2},\n YMax: {3}".format(desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax))

# 3. Generate a fishnet, but this time define the originCoordinate, yAxisCoordinate and oppositeCorner
# using the extracted extent from above. Hint: Formatting of the coordinate is important when generating
# the Fishnet, you must present it as: "-176.87 -41", note the space inbetween, and the fact that the
# entire thing is a string. Hint use: cellSizes of 0.25 degrees.

print(desc.origin_coord)

# originCoordinate = "-176.87 -51"  # Left bottom of our point data
# yAxisCoordinate = "-176.87 -41"  # This sets just the orientation of the y-axis, so we head 10 degrees perfectly north
# cellSizeWidth = "10"  # 10 degrees - these cells are going to be big to start with, we can refine later.
# cellSizeHeight = "10"
# numRows = ""  # Leave blank, as we have set cellSize
# numColumns = ""  # Leave blank, as we have set cellSize
# oppositeCorner = "162.0200043 71.34999847"  # starts in the bottom left corner, should end in top right corner
# # On your own time, make this as weird as possible just so you get comfortable with this tool.
# labels = "NO_LABELS" # don't want to deal with them here
# templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
# geometryType = "POLYGON"  # Create a polygon, so we can count the points inside the polygon.
# # could be POLYLINE, but can't do spatial analysis on the inside.
#
# arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
#                                cellSizeWidth, cellSizeHeight, numRows, numColumns,
#                                oppositeCorner, labels, templateExtent, geometryType)

# 4. Undertake a Spatial Join to join the fishnet to the observed points.

# 5. Check that the heatmap is created and delete the intermediate files (e.g. species shapefile and fishnet). Hint:
# arcpy.Delete_management()..

# 6. Visualize in ArcGIS Pro

# Hint: To stop your script failing due to unable to overwriteOutput error, use the overwriteOutput environment setting:
# import arcpy
# arcpy.env.overwriteOutput = True  # If you get "already exists error" even when True, ensure file is not open in
# ArcGIS Pro or an other program such as Excel.

