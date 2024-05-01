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

### AD - First scan your basePath for the subfolders

imagery_directories = os.listdir(basePath)

for directory in imagery_directories:
    #### AD - os.path.join again
    directory_workspace = os.path.join(basePath, directory)
    arcpy.env.workspace = directory_workspace ## AD - set your workspace to the image subfolder.

    #### AD - Here's how I would find B4 and B5 file, listrasters returns a list, hence [0], I am assuming
    #### only one file called b4 in there.
    raster_b4 = arcpy.Raster(arcpy.ListRasters("*b4*")[0])
    raster_b5 = arcpy.Raster(arcpy.ListRasters("*b5*")[0])

    #### AD - by converting b4/b5 to an arcpy.Raster object, I can do math on it, without using rastercalculator.
    nvdi = (raster_b5 - raster_b4) / (raster_b5 + raster_b4)
    nvdi_raster = arcpy.Raster(nvdi)
    print(nvdi_raster)
    nvdi_raster.save(f'ndvi_raster_' + directory + '.tif')

