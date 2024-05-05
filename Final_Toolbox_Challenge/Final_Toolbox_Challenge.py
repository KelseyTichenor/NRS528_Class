# NRS 528: Final Toolbox Challenge

# In your final assignment for this course, you should create a Python Toolbox that contains
# a minimum of three simple tools for undertaking geoprocessing and file management operations.

# These tools can be discrete or part of a larger workflow.

# However, the caveats are that you should create a "single file" toolbox
# (no includes, or external file tools) and you should aim to not exceed 2000 lines of code in its entirety
# (but if you do, no worries).

# You should document the toolbox using Github README.md and provide example data for running each of your tools.

# Grading and feedback will focus on:

# 1) Does the toolbox install, and the tools run successfully?
# 2) cleanliness of code,
# 3) functionality and depth of processing operation, and
# 4) appropriate use of documentation. Plus,
# 5) provide example data that allows me to test your tools.

# The criteria are:

# Does the toolbox install and run? (25 points)
# Cleanliness of code (25 points)
# Functionality and depth of processing (25 points)
# Appropriate use of documentation (15 points)
# In addition, you must provide example data (10 points).
# Help is here when you need it, just email Andy.

#######

# Just to keep things easy, I'm going to try to take my Mid-Term Coding Challenge code
#   and put it into toolbox form.
# In that challenge, I identified riparian zones in Richmond, RI using the select, clip, and buffer tools.

import os
import arcpy

Base_Path = "C:/GitHub/NRS528_Class/Final_Toolbox_Challenge/KT_Final_Data_And_Models"
arcpy.env.workspace = Base_Path
keep_temp_files = False
arcpy.env.overwriteOutput = True

Rivers = os.path.join(Base_Path, "Rivers", "Rivers.shp")
towns = os.path.join(Base_Path, "Towns", "Towns.shp")

if not os.path.exists(os.path.join(Base_Path, "Temporary_Files")):
    os.mkdir(os.path.join(Base_Path, "Temporary_Files"))
    print("Temporary files folder created")
else:
    print("Temporary Files Folder already there")

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Final Python Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Select]


class Select(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Select Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_line = arcpy.Parameter(name="input_line",
                                     displayName="Input Line",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_line.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\URI_Campus_Roads_OSM.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_line)
        input_polygon = arcpy.Parameter(name="input_polygon",
                                        displayName="Input Polygon",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        input_polygon.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\URI_Campus_Buildings_OSM.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_polygon)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\Output.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_line = parameters[0].valueAsText
        input_polygon = parameters[1].valueAsText
        output = parameters[2].valueAsText

        arcpy.Clip_analysis(in_features=input_line,
                            clip_features=input_polygon,
                            out_feature_class=output,
                            cluster_tolerance="")
        return

#
# class Clip(object):
#     def __init__(self):
#         """Define the tool (tool name is the name of the class)."""
#         self.label = "Clippy Tool"
#         self.description = ""
#         self.canRunInBackground = False
#
#     def getParameterInfo(self):
#         """Define parameter definitions"""
#         params = []
#         input_line = arcpy.Parameter(name="input_line",
#                                      displayName="Input Line",
#                                      datatype="DEFeatureClass",
#                                      parameterType="Required",  # Required|Optional|Derived
#                                      direction="Input",  # Input|Output
#                                      )
#         input_line.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\URI_Campus_Roads_OSM.shp"  # This is a default value that can be over-ridden in the toolbox
#         params.append(input_line)
#         input_polygon = arcpy.Parameter(name="input_polygon",
#                                         displayName="Input Polygon",
#                                         datatype="DEFeatureClass",
#                                         parameterType="Required",  # Required|Optional|Derived
#                                         direction="Input",  # Input|Output
#                                         )
#         input_polygon.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\URI_Campus_Buildings_OSM.shp"  # This is a default value that can be over-ridden in the toolbox
#         params.append(input_polygon)
#         output = arcpy.Parameter(name="output",
#                                  displayName="Output",
#                                  datatype="DEFeatureClass",
#                                  parameterType="Required",  # Required|Optional|Derived
#                                  direction="Output",  # Input|Output
#                                  )
#         output.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\Output.shp"  # This is a default value that can be over-ridden in the toolbox
#         params.append(output)
#         return params
#
#     def isLicensed(self):
#         """Set whether tool is licensed to execute."""
#         return True
#
#     def updateParameters(self, parameters):
#         """Modify the values and properties of parameters before internal
#         validation is performed.  This method is called whenever a parameter
#         has been changed."""
#         return
#
#     def updateMessages(self, parameters):
#         """Modify the messages created by internal validation for each tool
#         parameter.  This method is called after internal validation."""
#         return
#
#     def execute(self, parameters, messages):
#         """The source code of the tool."""
#         input_line = parameters[0].valueAsText
#         input_polygon = parameters[1].valueAsText
#         output = parameters[2].valueAsText
#
#         arcpy.Clip_analysis(in_features=input_line,
#                             clip_features=input_polygon,
#                             out_feature_class=output,
#                             cluster_tolerance="")
#         return
#
#
# class Buffer(object):
#     def __init__(self):
#         """Define the tool (tool name is the name of the class)."""
#         self.label = "Clippy Tool"
#         self.description = ""
#         self.canRunInBackground = False
#
#     def getParameterInfo(self):
#         """Define parameter definitions"""
#         params = []
#         input_line = arcpy.Parameter(name="input_line",
#                                      displayName="Input Line",
#                                      datatype="DEFeatureClass",
#                                      parameterType="Required",  # Required|Optional|Derived
#                                      direction="Input",  # Input|Output
#                                      )
#         input_line.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\URI_Campus_Roads_OSM.shp"  # This is a default value that can be over-ridden in the toolbox
#         params.append(input_line)
#         input_polygon = arcpy.Parameter(name="input_polygon",
#                                         displayName="Input Polygon",
#                                         datatype="DEFeatureClass",
#                                         parameterType="Required",  # Required|Optional|Derived
#                                         direction="Input",  # Input|Output
#                                         )
#         input_polygon.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\URI_Campus_Buildings_OSM.shp"  # This is a default value that can be over-ridden in the toolbox
#         params.append(input_polygon)
#         output = arcpy.Parameter(name="output",
#                                  displayName="Output",
#                                  datatype="DEFeatureClass",
#                                  parameterType="Required",  # Required|Optional|Derived
#                                  direction="Output",  # Input|Output
#                                  )
#         output.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\Output.shp"  # This is a default value that can be over-ridden in the toolbox
#         params.append(output)
#         return params
#
#     def isLicensed(self):
#         """Set whether tool is licensed to execute."""
#         return True
#
#     def updateParameters(self, parameters):
#         """Modify the values and properties of parameters before internal
#         validation is performed.  This method is called whenever a parameter
#         has been changed."""
#         return
#
#     def updateMessages(self, parameters):
#         """Modify the messages created by internal validation for each tool
#         parameter.  This method is called after internal validation."""
#         return
#
#     def execute(self, parameters, messages):
#         """The source code of the tool."""
#         input_line = parameters[0].valueAsText
#         input_polygon = parameters[1].valueAsText
#         output = parameters[2].valueAsText
#
#         arcpy.Clip_analysis(in_features=input_line,
#                             clip_features=input_polygon,
#                             out_feature_class=output,
#                             cluster_tolerance="")
#         return

# This cheat code block allows you to run your code in a test-mode within PyCharm,
# i.e. you do not have to open the tool in ArcMap. This works best for a "single tool" within the Toolbox.
# def main():
#     tool = Clippy()
#     tool.execute(tool.getParameterInfo(), None)
#
# if __name__ == '__main__':
#     main()
