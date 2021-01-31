Open image [xy_16bit_labels__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit_labels__nuclei.tif)
1. Measure shapes and find label index of nuclei with largest perimeter
2. Create an image with the circulaty feature displayed
3. Change pixel size to 0.5 um and repeat the measurements. Why some parameters change and some other don't ?

> ## Solution
> 1. **[Plugins > MorphoLibJ > Analyze > Analyze Regions]** the upper right nuclei.
> 2. **[Plugins > MorphoLibJ > Label Regions > Assign Measure to Label]**.
> 3. Some features are the ratio of dimensional features and so are independent of the spatial calibration.
{: .solution}
