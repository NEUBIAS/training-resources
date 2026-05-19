<h4 id="workflow"><a href="#workflow">Workflow to measure the intensity on a nuclear membrane</a></h4>
In image [xyc_16bit__nup__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei.tif) 
we would like to measure the intensity along the nuclear membrane (channel 1) using the information from the DNA (channel 2) using following workflow:
* Segmentation of the nuclei using channel 2, the results is a binary mask.
* Cleanup of the binary mask using morphological filters (try opening and closing operations). You should get something like 
[xy_8bit_binary__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei/xy_8bit_binary__nuclei.tif). 
* Use the improved binary mask to compute a rim mask around the nucleus 
* Perform a connected components analysis to obtain a labeled image of the nuclear rim. You should get something like 
	[xy_8bit_labels__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei/xy_8bit_labels__nuclei.tif).
* Measure the intensities in channel 1 on the nuclear rim
