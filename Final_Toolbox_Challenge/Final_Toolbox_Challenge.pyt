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

# Don't import os - any filepath references (beyond testing code prior to loading in ArcPro) are no-no's.
# Per AD: select tool and SQL queries are dark magic :( - stay away from those and stick to tools that don't require
#         filtering the data or selecting stuff from drop-down lists: I'm thinking clip, erase, and count overlapping
#         features? Everything else looks like some harpy witch magic I have no idea how to access.

import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Final Python Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Clippy, MrCleanMagicEraser, CountOverlap]


class Clippy(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Clippy Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        inFeature = arcpy.Parameter(name="Input_Feature",
                                     displayName="Insert Feature Data Here",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        inFeature.value = r"C:\GitHub\NRS528_Class\Final_Toolbox_Challenge\Final_Toolbox_Data\Leaking_Underground_Storage_Tanks\Leaking_Underground_Storage_Tanks.shp"
              # This is a default value that can be over-ridden in the toolbox
        params.append(inFeature)
        clipFeature = arcpy.Parameter(name="input_polygon",
                                        displayName="Insert Clip Data Here",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        clipFeature.value = r"C:\GitHub\NRS528_Class\Final_Toolbox_Challenge\Final_Toolbox_Data\Wetlands_2020\Wetlands_2020.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(clipFeature)
        output = arcpy.Parameter(name="Output",
                                 displayName="What should we name the output?",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"C:\GitHub\NRS528_Class\Final_Toolbox_Challenge\Final_Toolbox_Data\Clip_Test.shp"  # This is a default value that can be over-ridden in the toolbox
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
        inFeature = parameters[0].valueAsText
        clipFeature = parameters[1].valueAsText
        output = parameters[2].valueAsText

        arcpy.Clip_analysis(in_features=inFeature,
                            clip_features=clipFeature,
                            out_feature_class=output,
                            cluster_tolerance="")
        return


class MrCleanMagicEraser(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Erase Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        inFeature2 = arcpy.Parameter(name="Input_Feature",
                                    displayName="Insert Feature Data Here",
                                    datatype="DEFeatureClass",
                                    parameterType="Required",  # Required|Optional|Derived
                                    direction="Input",  # Input|Output
                                    )
        inFeature2.value = r"C:\GitHub\NRS528_Class\Final_Toolbox_Challenge\Final_Toolbox_Data\Leaking_Underground_Storage_Tanks\Leaking_Underground_Storage_Tanks.shp"
        # This is a default value that can be over-ridden in the toolbox
        params.append(inFeature2)
        eraseFeature = arcpy.Parameter(name="input_polygon",
                                      displayName="Insert Erase Data Here",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",  # Required|Optional|Derived
                                      direction="Input",  # Input|Output
                                      )
        eraseFeature.value = r"C:\GitHub\NRS528_Class\Final_Toolbox_Challenge\Final_Toolbox_Data\Wetlands_2020\Wetlands_2020.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(eraseFeature)
        output = arcpy.Parameter(name="Output",
                                 displayName="What should we name the output?",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"C:\GitHub\NRS528_Class\Final_Toolbox_Challenge\Final_Toolbox_Data\Clip_Test.shp"  # This is a default value that can be over-ridden in the toolbox
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
        inFeature2 = parameters[0].valueAsText
        eraseFeature = parameters[1].valueAsText
        output2 = parameters[2].valueAsText

        arcpy.Erase_analysis(in_features=inFeature2,
                            erase_features=eraseFeature,
                            out_feature_class=output2,
                            cluster_tolerance="")
        return


class CountOverlap(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Count Overlap Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        inFeature3 = arcpy.Parameter(name="Input_Feature",
                                     displayName="Insert Feature Data Here",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        # inFeature3.value = r"C:\GitHub\NRS528_Class\Final_Toolbox_Challenge\Final_Toolbox_Data\Leaking_Underground_Storage_Tanks\Leaking_Underground_Storage_Tanks.shp"
              # This is a default value that can be over-ridden in the toolbox
        params.append(inFeature3)
        output3 = arcpy.Parameter(name="Output",
                                 displayName="What should we name the output?",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        # output3.value = r"C:\GitHub\NRS528_Class\Final_Toolbox_Challenge\Final_Toolbox_Data\Clip_Test.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output3)
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
        inFeature = parameters[0].valueAsText
        output = parameters[1].valueAsText

        arcpy.CountOverlappingFeatures_analysis(in_features=inFeature,
                                                out_feature_class=output,
                                                min_overlap_count="",
                                                out_overlap_table=""
                                                )
        return

# This cheat code block allows you to run your code in a test-mode within PyCharm,
# i.e. you do not have to open the tool in ArcMap. This works best for a "single tool" within the Toolbox.
# def main():
#     tool = Clippy()
#     tool.execute(tool.getParameterInfo(), None)
#
# if __name__ == '__main__':
#     main()