# Coding Challenge 10

<p align="center">
  <img height="300" src="https://github.com/KelseyTichenor/NRS528_Class/blob/main/Images/NVDI.jpg?raw=true">
</p>

* We got to play with rasters this time! For this challenge, we needed to calculate the NVDI index, which uses LANDSAT files to tell us about the vegetation in an area.
* Specifically, we wanted Bands 4 (red, AKA visible light) and 5 (near-infrared)

* Per Wikipedia: NDVI's will be values between -1 and 1.
* 1 indicates healthy vegetation, and 0 indicates no vegetation.
* Values between 0 and 1 indicate varying degrees of vegetation.
* Anything less than 0 indicates a lack of dry land.
* A value of -1 is straight up ocean.

* To do this, I extracted the Landsat data provided to a known location on my computer.
* Then, I converted Bands 4 and 5 in each file to a raster object so I could do math on it.
* The alternative was to use the Raster Calculator tool. I tried, but it was proving rather fiddly (and by that I mean impossible (for me) to work with due to the fact that Esri kept saying the Raster Calculator tool wasn't meant for scripting).
* ANYWAY,
* For each month provided (February, April, May, July, October, and November), I calculated the NVDI using the equation: nvdi = (nir - vis) / (nir + vis).
* This gave me good data I could use to create a map layout to show the differences between each month. The layout is posted at the top of this README and is in PDF form in this repo.