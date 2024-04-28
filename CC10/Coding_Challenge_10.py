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
# raster_list = []

# for folder in basePath:
#     for raster in arcpy.ListRasters('*B4'):
#         raster_list.append(raster)
# print(raster_list)
#
# ^^^^ Not sure what I'm actually supposed to do here ^^^^
# Maybe it'll make more sense if I can get the raster calculator tool going.

#######
# Sourced code from https://pro.arcgis.com/en/pro-app/latest/arcpy/spatial-analyst/raster-calculator.htm
#   and tried to make it work with the Python snippet copied from the tool in ArcPro

with arcpy.EnvManager(scratchWorkspace=basePath):
    in_raster1 = "LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif"
    in_raster2 = "LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif"
    outRaster = arcpy.ia.RasterCalculator(
        expression=((int(in_raster1)) - (int(in_raster2)) / (int(in_raster1)) + (int(in_raster2))
    outRaster.save(os.path.join(basePath, "Test.tif"))


# Original Python snippet copied from ArcPro: save this if you mess up with editing the code

# with arcpy.EnvManager(scratchWorkspace=r"c:\users\ektic\onedrive\documents\arcgis\projects\myproject1\myproject1.gdb"):
#     output_raster = arcpy.ia.RasterCalculator(
#         expression='("LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif" - "LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif") / ( "LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif" +  "LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif")'
#     )
#     output_raster.save(r"c:\users\ektic\onedrive\documents\arcgis\projects\myproject1\myproject1.gdb\nirvis_raste")
