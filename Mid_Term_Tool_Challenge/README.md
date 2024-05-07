# NRS 528: Mid-Term Tool Challenge

<p align="center">
  <img height="300" src="https://github.com/KelseyTichenor/NRS528_Class/blob/main/Images/halfway.jpg?raw=true">
</p>

* The Mid-Term Tool Challenge marked the halfway point of the Spring 2024 semester. 
* For this, we needed to create a small script tool that takes advantage of both arcpy and Python.
* The code needed to be able to run on all PC's, and we needed to provide example data.
* The tool needs to use three different geoprocessing tools to manipulate the example data.
* To make this easier, I decided to 'cheat' by turning a simplified version of a model I made in NRS 410 into a Python code snippet.
* Then, I functionalized the code in order to make it run in pycharm. 
* The model was designed to identify riparian zones in Richmond, RI.
* The resulting Python code was designed to select Richmond out of the RI Towns dataset, clip the RI rivers dataset to the RI Towns dataset, then buffer the rivers in the clipped towns/rivers layer.
* This was honestly fun to put together, and it felt great to know that it actually worked!
* To keep the code path-agnostic, I made prodigious use of my new favorite command, os.path.join to link relative filepaths to a predefined base path.