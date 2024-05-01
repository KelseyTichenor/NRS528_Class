# Coding Challenge 10:

# Our coding challenge this week that improves our practice with rasters from Week 10.
# Task 1:
# Use what you have learned to process the Landsat files provided, this time, you know you are interested in the NVDI
#   index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the Landsat 8 imagery.
# See here for more info about the bands: https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites
# Data provided are monthly (a couple are missing due to cloud coverage) during the year 2015 for the State of RI,
#   and stored in the file Landsat_data_lfs.zip.
#
# Before you start, here is a suggested workflow:
# 1. Extract the Landsat_data_lfs.zip file into a known location.
# 2. For each month provided, you want to calculate the NVDI,
#    using the equation: nvdi = (nir - vis) / (nir + vis)
#    https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index.
#    Consider using the Raster Calculator Tool in ArcMap and using "Copy as Python Snippet" for the first calculation.
#
# The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided.
# As part of your code submission, you should also provide a visualization document
# (e.g. an ArcMap layout in PDF format), showing the patterns for an area of RI that you find interesting.

import os
import arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

basePath = r"C:\Schoolwork\NRS_528\CC10_Landsat_Data"
# basePath not connected to GitHub, cuz who wants to commit a ton of 500 mB files?
arcpy.env.workspace = basePath
arcpy.env.overwriteOutput = True

# Per AD - First scan your basePath for the subfolders (Thanks for this!)

raster_directories = os.listdir(basePath)  # Remember from earlier in the semester - lists contents of directories :)

for directory in raster_directories:
    directory_workspace = os.path.join(basePath, directory)  # Lets you iterate through all directories in the basePath
    arcpy.env.workspace = directory_workspace  # Sets the workspace for just within this loop
    arcpy.env.scratchWorkspace = directory_workspace
    # Per AD - Here's how I would find B4 and B5 file, listrasters returns a list, hence [0], I am assuming
    # only one file called b4 in there. Same goes for b5.
    raster_b4 = arcpy.Raster(arcpy.ListRasters("*b4*")[0])
    raster_b5 = arcpy.Raster(arcpy.ListRasters("*b5*")[0])
    # Ah, I see two asterisks are needed when using them as a wildcard function. Noted.

    # This is probably gonna work, but let's do some print statements to see what this *should* look like.
    print(raster_b4)
    print(raster_b5)

    # Success!
    # Per AD - by converting b4/b5 to an arcpy.Raster object, I can do math on it, without using rastercalculator.
    #          (Thank God - that tool WAS finicky!)
    # Would be good to remember that raster_b4 and raster_b5 are only defined within this 'for' loop.
    # That means that any math that needs to be done has to be done within this loop as well, like this:

    nvdi = (raster_b5 - raster_b4) / (raster_b5 + raster_b4)  # Wow this is way easier than I was imagining it would be!
    nvdi_raster = arcpy.Raster(nvdi)
    print(nvdi_raster)

    # Printing these gave me a bunch of files that look similar to this:
    # "C:\Users\ektic\AppData\Local\Temp\x62a2cf7b_e977_4794_9ae5_2d89035da382y0.afr"
    # I wonder what these do? - UPDATE: They're temporary files that go with the .tif file that gets saved
    #       as part of .save
    nvdi_raster.save(f'ndvi_raster_' + directory + '.tif')

    if arcpy.Exists(f'ndvi_raster_' + directory + '.tif'):
        print("NDVI rasters created successfully!")

# Confirmed in the directories that the .tif files have been created, and they visualize in ArcPro beautifully.
# Per Wikipedia: NDVI's will be values between -1 and 1.
# 1 indicates healthy vegetation, and 0 indicates no vegetation.
# Values between 0 and 1 indicate varying degrees of vegetation.
# Anything less than 0 indicates a lack of dry land.
# A value of -1 is straight up ocean.
# Holy crap, you're a lifesaver Andy, thanks for the help!
