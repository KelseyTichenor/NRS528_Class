#####
# Step 2 - Executing multiple tools
#####

# We will use multiple tools to generate a heatmap, and visualize it in ArcMap.
# A heatmap is a point or cloud that represents distributions.

# Part a - Using the Step_2_Deep_Coral_Data.zip as our extents, we will generate a fishnet
# grid: https://pro.arcgis.com/en/pro-app/tool-reference/data-management/create-fishnet.htm

import arcpy
# set workspace environment
arcpy.env.workspace = r"E:\Kelsey_Tichenor_NRS_528\GitHub\NRS528_Class\Class_5"
arcpy.env.overwriteOutput = True # very important, you'll get an error otherwise.
# Set coordinate system of the output fishnet - it will always be in degrees if we're doing fishnet grids.
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

# outFeatureClass = "Step_2_Fishnet.shp"  # Name of output fishnet
# 83.4844004°W 36.3123205°N - got this manually through the shapefile, but there has to be a more precise way.
# Set the origin of the fishnet - remember, the coordinates will ALWAYS be in degrees relative to the equator.
originCoordinate = "83.4844004 36.3123205"  # Left bottom of our point data
yAxisCoordinate = "-176.87 -41"  # This sets just the orientation of the y-axis, so we head 10 degrees perfectly north
cellSizeWidth = "10"  # 10 degrees - these cells are going to be big to start with, we can refine later.
cellSizeHeight = "10"
numRows = ""  # Leave blank, as we have set cellSize
numColumns = ""  # Leave blank, as we have set cellSize
oppositeCorner = "162.0200043 71.34999847"  # starts in the bottom left corner, should end in top right corner
# On your own time, do t
labels = "NO_LABELS" # don't want to deal with them here
templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
geometryType = "POLYGON"  # Create a polygon, so we can count the points inside the polygon.
# could be POLYLINE, but can't do spatial analysis on the inside.

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

# Part b - Count the amount of points in each fishnet cell

# To do this we use a tool called SpatialJoin, relatively simple to set up

target_features="E:\Kelsey_Tichenor_NRS_528\GitHub\NRS528_Class\Class_5\Step_2_Fishnet.shp"
join_features="E:\Kelsey_Tichenor_NRS_528\GitHub\NRS528_Class\Class_5\Deep_Coral_Data\Step_2_Deep_Coral_Data.shp"
out_feature_class="Step_2_Deep_Coral_HeatMap.shp"
join_operation="JOIN_ONE_TO_ONE"
join_type="KEEP_ALL" # keep all the polygon shapefiles even if no corals are in it
field_mapping=""
match_option="INTERSECT"
search_radius=""
distance_field_name=""

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)

# Part c - Visualize the file in ArcGIS Pro and change the symbology to a heatmap esq style.


# FOR OUR TASK HERE, HEAD TO STEP_3.PY