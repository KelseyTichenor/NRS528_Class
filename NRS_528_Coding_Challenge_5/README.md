# Coding Challenge 5

<p align="center">
  <img height="300" src="https://github.com/KelseyTichenor/NRS528_Class/blob/main/Images/fishnet.jpg?raw=true">
</p>

* Professor Andy Davies gave us two options for Coding Challenge 5.
* We could use the established one that he published in his repo, or if we were sufficiently struggling, we could complete Step 3 from Class 5 on our own and submit that as the Coding Challenge.
* I was definitely riding the Struggle Bus, so I opted for option 2.
* The object of this modified coding challenge was to use a CSV file full of *Cepphus grylle* data and complete the following tasks:
1. Convert the CSV to a shapefile.
2. Extact the Extent, i.e. XMin, XMax, YMin, YMax of the generated shapefile.
3. Generate a fishnet, but instead of using hard-coded coordinates, define the originCoordinate, yAxisCoordinate and oppositeCorner using the extracted extent from Step 2. 
4. Undertake a Spatial Join to join the fishnet to the observed points.
5. Check that the heatmap is created and delete the intermediate files (e.g. species shapefile and fishnet) using arcpy.Delete_management()..
6. Visualize the heatmap in ArcGIS Pro

I had trouble with this at first because my heatmap was being projected to the literal world origin, but that's because I didn't set a spatial reference originally. Lesson learned.