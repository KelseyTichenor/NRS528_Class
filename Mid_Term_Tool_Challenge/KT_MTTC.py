# Mid-Term Tool Challenge #

# In this assignment, you are instructed to produce a small script tool
#   that takes advantage of arcpy and Python.
# You will need to provide example data, and the code should run on all PC's.
# The tool needs to manipulate a dataset across three different processes,
#   for example, extracting, modifying and exporting data.
# The exact workflow is entirely up to yourself.
# You are expected to take 3-4 hours on this coding assignment,
#   and you should deposit your code and example files within a GitHub repository
#   for feedback and grading.
#
# The criteria are:
#
# Cleanliness of code (10 points)
# Functionality (10 points)
# Appropriate use of documentation (10 points)
# Depth of processing operation (10 points)
# In addition, you must provide example data and minimize the amount of editing
#   a user must make in order for the program to run (10 points).
# Help is here when you need it, just email Andy.

#####

# For the record, I'm simplifying a short model I created for NRS 410 last semester
#   (Lab 8 Part 1)
#   and trying to make it run with simple Python script.
# The original goal of this model was to use the Tabulate Area tool to
#   calculate the land cover composition of riparian zones in Richmond, RI.
#   using a raster that I had included in my collection of data.
# Getting the Tabulate Area tool to work was proving to be a giant headache however;
#   which really stinks because I was proud of my re-projecting of the raster I was going to use,
#   so I'm just going to identify the riparian zones in Richmond instead.
# Identifying the zones still uses 3 tools total, so it should still be good enough to complete the challenge.

#####

import os
import arcpy

Base_Path = "C:/GitHub/NRS528_Class/Mid_Term_Tool_Challenge/KT_MTTC_Data_And_Models"
arcpy.env.workspace = Base_Path
keep_temp_files = False
arcpy.env.overwriteOutput = True

Rivers = os.path.join(Base_Path, "Rivers", "Rivers.shp")
towns = os.path.join(Base_Path, "Towns", "Towns.shp")
NLCD_2016_img = os.path.join(Base_Path, "NLCD_2016", "NLCD_2016.img")

# Make Temporary Folder
if not os.path.exists(os.path.join(Base_Path, "Temporary_Files")):
    os.mkdir(os.path.join(Base_Path, "Temporary_Files"))
    print("Temporary files folder created")
else:
    print("Temporary Files Folder already there")

# Process: Select (Select Richmond from the 'Towns' Layer) (analysis)
if not os.path.exists(os.path.join(Base_Path, "Temporary_Files", "Richmond_Select.shp")):
    arcpy.analysis.Select(in_features=towns,
                          out_feature_class=os.path.join(Base_Path, "Temporary_Files", "Richmond_Select.shp"),
                          where_clause="NAME = 'RICHMOND'")
    print("Richmond successfully selected")
else:
    print("This shapefile already exists")

# Process: Clip (Clip the 'Rivers' layer to the selected 'Richmond') (analysis)
if not os.path.exists(os.path.join(Base_Path, "Temporary_Files", "Richmond_River_Clip.shp")):
    arcpy.analysis.Clip(in_features=Rivers,
                        clip_features=os.path.join(Base_Path, "Temporary_Files", "Richmond_Select.shp"),
                        out_feature_class=os.path.join(Base_Path, "Temporary_Files", "Richmond_River_Clip.shp"))
    print("Rivers successfully clipped to Richmond! (Or do I have that backwards?)")
else:
    print("This shapefile already exists")

# Make the folder where the final files are going to be stored
if not os.path.exists(os.path.join(Base_Path, "Richmond_Riparian_Buffer")):
    os.mkdir(os.path.join(Base_Path, "Richmond_Riparian_Buffer"))
    print("Buffer Folder's all set")
else:
    print("Buffer Folder already exists")

# Process: Buffer (Buffer the rivers with a 100-meter zone;
#   everything in the buffer zone = riparian areas) (analysis)
if not os.path.exists(os.path.join(Base_Path, "Richmond_Riparian_Buffer", "Buffer_Zone.shp")):
    arcpy.analysis.Buffer(in_features=os.path.join(Base_Path, "Temporary_Files", "Richmond_River_Clip.shp"),
                          out_feature_class=os.path.join(Base_Path, "Richmond_Riparian_Buffer", "Buffer_Zone.shp"),
                          buffer_distance_or_field="100 Meters",
                          dissolve_option="ALL")
    print("Buffered rivers in Richmond")
else:
    print("This shapefile already exists")

# Deleting The Temporary File Folder
if keep_temp_files == False:
    arcpy.Delete_management(os.path.join(Base_Path, "temporary_files"))
