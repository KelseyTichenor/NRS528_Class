
#####
# Step 2 - Making and deleting files and folders
#####

# It is quite common that you will create a large amount of temporary files during the course of a normal
# geoprocessing operation, one way to store physical files is to use temporary directories, which can be removed
# following the successful completion of the processing operation.

# import os
# import arcpy
# import csv
#
# input_directory = "E:\Kelsey_Tichenor_NRS_528\GitHub\NRS528_Class\Class_7"
# keep_temp_files = True
# # keep the above command the way it is, that way you can see things that go wrong.
#
# # In this example, I show you how to use os.path.join to create directory names, which can be used to
# # test if the directory exists, and if not, create it.
#
# if not os.path.exists(os.path.join(input_directory, "species_files")):
#     os.mkdir(os.path.join(input_directory, "temporary_files"))
#     if not os.path.exists(os.path.join(input_directory, "outputs")):
#         os.mkdir(os.path.join(input_directory, "outputs"))
#
#     # above = if this stuff doesn't exist, make it. If not, ignore it.
#     # There's no need for us to manually create these folders - the computer can do it for you.
#
#     # Deletion of the files can also be controlled using a True or False variable. In this case, I only delete
#     # the temporary_files and species_files directories. I use arcpy to do this, as if you are generating files
#     # through arcpy, other methods such as shutil.rmtree will fail due to arcpy file locks.
#
#     if keep_temp_files == False:
#         arcpy.Delete_management(os.path.join(input_directory, "species_files"))
#         arcpy.Delete_management(os.path.join(input_directory, "temporary_files"))
#     os.mkdir(os.path.join(input_directory, "species_files"))
# if not os.path.exists(os.path.join(input_directory, "temporary_files")):


# arcpy.Delete_management is a lot more powerful than os, since this deletes all the files in the folder,
# plus the folder - not just the one folder.

# Task 1 - Using the code above create a temporary folder and an output folder, and adjust the code below to store the
# generated CSV files in the temporary folder, and the generated shapefiles in the output folder. Then delete
# the temporary file folder.

import os
import arcpy
import csv

# USERS EDIT THIS STUFF HERE

input_directory = r"E:\Kelsey_Tichenor_NRS_528\GitHub\NRS528_Class\Class_7"
data_file = "Step_2.csv"
keep_temp_files = False
arcpy.env.overwriteOutput = True

# DO NOT DO ANYTHING TO THE BELOW (this is more for other users - I can do whatever I want >:) )
##################################### (More insurance)

arcpy.env.workspace = input_directory

# if not os.path.exists(os.path.join(input_directory, "species_files")):
#     os.mkdir(os.path.join(input_directory, "temporary_files"))
#     if not os.path.exists(os.path.join(input_directory, "outputs")):
#         os.mkdir(os.path.join(input_directory, "outputs"))
# print("All set")
# # The above code works as long as the files I'm trying to make don't exist. Moving on.

# Step 1: Lets determine our species
species_list = []
with open(os.path.join(input_directory, data_file)) as species_csv:
    header_line = next(species_csv)
    for row in csv.reader(species_csv):
        try: # Using try/except saves us if there is a line with no data in the file
            if row[0] not in species_list:
                species_list.append(row[0])
        except:
            pass
print(species_list)
print("..There are: " + str(len(species_list)) + " species to process..")
# everything hangs on os.path.join and making sure you reference the right files
# #
# Step 2: Lets split the files
if len(species_list) > 1:
    for species in species_list:
        print("The species being processed is: " + species)
        species_count = 1
        with open(os.path.join(input_directory, data_file)) as species_csv:
            for row in csv.reader(species_csv):
                if row[0] == species:
                    if species_count == 1:
                        file = open(os.path.join(input_directory, "temporary_files", species + ".csv"), "w")
                        file.write(header_line)
                        s_count = 0
                    # the below code will make sure your output is a well formatted line:
                    file.write(",".join(row))
                    file.write("\n")
        file.close()
print("All set")
# #
# # Step 3: Convert those files into Shapefiles
import glob

os.chdir(os.path.join(input_directory, "temporary_files"))# same as env.workspace
arcpy.env.workspace = os.path.join(input_directory, "temporary_files")
species_file_list = glob.glob("*.csv")# Find all CSV files... Now you will get an error because I have not imported..??

count = 0

for species_file in species_file_list:
    print(".. Processing: " + str(species_file) + " by converting to shapefile format")
    in_Table = species_file
    x_coords = "decimalLongitude"
    y_coords = "decimalLatitude"
    z_coords = ""
    out_Layer = "species" + str(count)
    saved_Layer = species_file.replace(".","_") + ".shp"
    # We do this because shapefile names can only have 1 full stop in them.
#
    # Set the spatial reference
    spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
    arcpy.CopyFeatures_management(lyr, os.path.join(input_directory, "outputs", saved_Layer))
    count = count + 1
    arcpy.Delete_management(lyr)
print("All set")

#
if keep_temp_files == False:
    arcpy.Delete_management(os.path.join(input_directory, "temporary_files"))
    os.rmdir(os.path.join(input_directory, "temporary_files"))

# Actually, keep_temp_files == false won't automatically delete the folder for you anymore
# Make sure you use the above (or a different method) to make sure it gets deleted


