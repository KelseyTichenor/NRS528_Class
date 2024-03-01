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

arcpy.env.workspace = r"C:\GitHub\NRS528_Class\Class_5"
arcpy.env.overwriteOutput = True

in_Table = r"Step_3_Cepphus_grylle.csv"
# It's already referenced in the workspace, so the relative path will work OK here.
x_coords = "lon"
y_coords = "lat"
# At first, I transposed latitude and longitude - are they supposed to be backwards in this situation?
z_coords = ""
out_Layer = "Cepphus Grylle"
saved_Layer = r"C:\GitHub\NRS528_Class\Class_5\Step_3_Cepphus_grylle.shp"

# Set the spatial reference
spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

# Save to a layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)

if arcpy.Exists(saved_Layer):
    print("Created file successfully!")

# 2. Extact the Extent, i.e. XMin, XMax, YMin, YMax of the generated Cepphus_grylle shapefile.

desc = arcpy.Describe(r"C:\GitHub\NRS528_Class\Class_5\Step_3_Cepphus_grylle.shp")
# print(desc.extent) - but string substitution notation makes things more accessible, so let's do this instead:
print("Extent:\n XMin: {0},\n XMax: {1},\n YMin: {2},\n YMax: {3}".format(desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax))
# When we run this step:
#  XMin: -82.0,
#  XMax: -50.45,
#  YMin: 36.79312,
#  YMax: 59.4333

# 3. Generate a fishnet, but this time define the originCoordinate, yAxisCoordinate and oppositeCorner
# using the extracted extent from above. Hint: Formatting of the coordinate is important when generating
# the Fishnet, you must present it as: "-176.87 -41", note the space inbetween, and the fact that the
# entire thing is a string. Hint use: cellSizes of 0.25 degrees.

<<<<<<< HEAD

print("Extent:\n  YMin: {0},\n YMax: {1}".format(desc_image.extent.YMin, desc_image.extent.YMax))
=======
# Keep in mind: to find the origin point from the calculated extent:
#   It's literally just (XMin, YMin). Doubts? Calculate the extent from Step_1 and compare with the origin in Step_2.
>>>>>>> dce1bda3ddc603463b0ae323ad7665714869c7fe

outFeatureClass = "Step_3_Fishnet.shp"  # Name of output fishnet
# Set the origin of the fishnet - remember, the coordinates will ALWAYS be in degrees relative to the equator.
originCoordinate = "-82.0 36.79312"  # Left bottom of our point data
yAxisCoordinate = "-82.0 46.79312"  # This sets just the orientation of the y-axis, so we head 10 degrees perfectly north
cellSizeWidth = "0.25"  # if not specified, start with 10 degrees; we can refine later.
cellSizeHeight = "0.25"
numRows = ""  # Leave blank, as we have set cellSize
numColumns = ""  # Leave blank, as we have set cellSize
oppositeCorner = "-50.45 59.4333"  # starts in the bottom left corner, should end in top right corner
# On your own time, do try to make this as weird as possible so you can see how the program works.
# Again, this depends on the extent: should be (XMax, YMax)
labels = "NO_LABELS" # don't want to deal with them here
templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
geometryType = "POLYGON"  # Create a polygon, so we can count the points inside the polygon.
# could be POLYLINE, but can't do spatial analysis on the inside.

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

# WARNING: for some reason what should be the origin corner is acting as the opposite corner.
# UPDATE: this is because before, I set the y-axis coordinate to (-82.0 26.79312) instead.
#         This will force the fishnet points to be reflected below where we need them to be.
#
# 4. Undertake a Spatial Join to join the fishnet to the observed points.
#
# Recall from Step 2 Part B:
# "To (count the amount of points in each fishnet cell),
# we use a tool called SpatialJoin, relatively simple to set up"

target_features="Step_3_Fishnet.shp"
join_features="Step_3_Cepphus_grylle.shp"
out_feature_class="Step_3_Cepphus-grylle_HeatMap.shp"
join_operation="JOIN_ONE_TO_ONE"
join_type="KEEP_ALL" # keep all the polygon shapefiles even if no specimens are in it
field_mapping=""
match_option="INTERSECT"
search_radius=""
distance_field_name=""

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)

# 5. Check that the heatmap is created and delete the intermediate files (e.g. species shapefile and fishnet). Hint:
arcpy.Delete_management("Step_3_Cepphus_grylle.shp", "Step_3_Fishnet.shp")

# 6. Visualize in ArcGIS Pro

# Hint: To stop your script failing due to unable to overwriteOutput error, use the overwriteOutput environment setting:
# import arcpy
# arcpy.env.overwriteOutput = True  # If you get "already exists error" even when True, ensure file is not open in
# ArcGIS Pro or an other program such as Excel.

