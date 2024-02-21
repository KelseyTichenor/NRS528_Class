# Coding Challenge 4: Let's run a tool using nothing but Python code!

# Requirements:
# Code must be well-commented.
# Code must be able to run on any machine with a simple filepath change.

# Let's keep this easy and try running the Union tool:

# Step 1: Open up ArcPro and import arcpy and related modules, as per Esri.
import arcpy
from arcpy import env
# Step 2: Set up the environment.
env.workspace = r"C:\GitHub\NRS528_Class\NRS_528_Coding_Challenge_4"
env.scratchWorkspace = r"C:\GitHub\NRS528_Class\NRS_528_Coding_Challenge_4"
# Step 3: Define required and optional features, then plug them in accordingly.
# Required: (in_features (input shapefiles), out_features (output shapefile)
# Optional: {join_attributes (lets us be selective about which features get transferred,
#           cluster_tolerance (minimum distance separating polygons.
#           gaps (identify areas completely enclosed by polygons)}
inFeatures = ["NWI14.shp", "Building_footprints_South_Kingston.shp"]
outFeatures = ["Wetlands_and_Building_Footprints.shp"]
arcpy.Union_analysis(inFeatures, outFeatures)
print("Let's hope this works.")