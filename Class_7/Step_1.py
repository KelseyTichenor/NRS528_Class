
#####
# Step 1 - Searching directories for files and list them
#####

# Handling files is a critical part of any GIS (and analysis) workflow. This is particularly true if you are
# working with large amounts of files as we often do. In this step, we cover several ways of searching and
# listing files. We will use a mix of different methods and packages to do this. There are no right or
# wrong ways, providing you get the data you require.

# Part 1 - List files in the Step_1 directory using glob.glob: https://docs.python.org/2/library/glob.html
#
# import glob
# import os
#
# # List all Python files in current directory
# print(glob.glob("*.py"))
# # glob.glob is a search function - * = a wildcard that lets you search for whatever you put after it
# # However, glob.glob will NOT respect Arcpy workspaces since it's not an Arcpy tool - it's a base Python tool
# # os is the base Python package, Arcpy will honor os functions, but os will NOT honor Arcpy functions
#
# # Change to parent of current directory (dangerous as you might struggle to change it back later...)
# os.chdir("../")
# # os.chdir means change directory relative to your execution location.
# # ../ means change it to one folder level dowm (before)
# print(glob.glob("*")) # no pattern match, lists all folders and files
# # Just an asterisk means match everything.
# # If you changed directory, you may need to change it back:
# # glob will not look at hidden files, such as the .idea file
#
# # Part 2 - List files using os (more painful than glob.glob)
# os.chdir("Class_7")
# all = os.listdir(os.curdir)# files and directories
# print(all)
# files = list(filter(os.path.isfile, os.listdir(os.curdir)))  # files only, might not find anything
# print(files)
# #
# for file in os.listdir(os.curdir):
#     if file.endswith(".shp"):
#         print(file)
# #
# # Part 3 - List files using arcpy, note: all will return None
# import arcpy
#
# # ListFiles ({wild_card}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listfiles.htm
# print(arcpy.ListFiles("*"))
#
# # ListDatasets ({wild_card}, {feature_type}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listdatasets.htm
# print(arcpy.ListDatasets("*",  "Feature"))
# # ListFeatureClasses ({wild_card}, {feature_type}, {feature_dataset}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listfeatureclasses.htm
# print(arcpy.ListFeatureClasses("*"))
#
# # ListRasters ({wild_card}, {raster_type})  https://pro.arcgis.com/en/pro-app/arcpy/functions/listrasters.htm
# print(arcpy.ListRasters("*", "TIF"))
# #
#
# Tasks
# 1 - Using the supplied data in Step_1.zip (extract to a folder named Step_1), do the following:
# Hint, you should change your directory to Step_1
import arcpy
import os
import glob
os.chdir("E:/Kelsey_Tichenor_NRS_528/GitHub/NRS528_Class/Class_7/Step_1")
# correct answer = establish a 'base path', THEN use the file name.
# then refer everything to the base path. The os.dir, the arcpy.env.workspace, everything.
arcpy.env.workspace = "E:/Kelsey_Tichenor_NRS_528/GitHub/NRS528_Class/Class_7/Step_1"

# a - List and count all shapefiles, how many are there?
print(glob.glob("*.shp"))
print(len(glob.glob("*.shp")))

# b - List and count all csv, how many are there?
print(glob.glob("*.csv"))
print(len(glob.glob("*.csv")))

# c - List and count all folders, how many are there?
# remember, gotta make a list if you're not using glob!
folder_names = []

for folder_name in os.listdir(os.curdir):
    if os.path.isdir(folder_name): # this function will run through the list and check for folders
        folder_names.append(folder_name)
print(folder_names)
print(len(folder_names))

# d - List and count all rasters in GRID format, how many are there?
step1grids = arcpy.ListRasters("*", "GRID")
for raster in step1grids:
    print(raster)
print(len(step1grids))

# e - List and count all rasters in TIF format, how many are there?
step1tifs = arcpy.ListRasters("*", "TIF")
for raster in step1tifs:
    print(raster)
print(len(step1tifs))

# f - List and count all folders beginning with the letter/character S_, how many are there?
S_Underscore = []

for S_folder_name in os.listdir(os.curdir):
    # if S_folder_name.beginswith("S_"): - incorrect; KT's inventing code again
    if os.path.isdir(S_folder_name) and "S_" in S_folder_name:
        S_Underscore.append(S_folder_name)
print(S_Underscore)
print(len(S_Underscore))
