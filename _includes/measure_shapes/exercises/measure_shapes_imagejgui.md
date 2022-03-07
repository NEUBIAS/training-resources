Open image [xy_16bit_labels__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit_labels__nuclei.tif)
Using MorpholibJ:
1. Measure object shapes and find the label index of the nucleus with the largest perimeter
2. Change the pixel size to 0.5 um and repeat the measurements. Why do some parameters change while others don't?
3. (Optional) Create an image where each object is coloured according to the measured circularity

> ## Solution
> 1. **[Plugins > MorphoLibJ > Analyze > Analyze Regions]** the upper right nuclei.
> 2. Some features are the ratio of dimensional features and so are independent of the spatial calibration.
> 3. **[Plugins > MorphoLibJ > Label Regions > Assign Measure to Label]**.
{: .solution}
