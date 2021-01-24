* Open image [xy_16bit_labels__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit_labels__nuclei.tif)
* Measure shapes and find label index of nuclei with largest perimeter
* Create an image with the circulaty feature displayed
* Change pixel size to 0.5 um and repeat the measurements. Why some parameters change and some other don't ?

> ## Solution
> - **[Plugins > MorphoLibJ > Analyze > Analyze Regions]** the upper right nuclei.
> - **[Plugins > MorphoLibJ > Label Regions > Assign Measure to Label]**.
> - Some features are the ratio of dimensional features and so are independent of the spatial calibration.
{: .solution}