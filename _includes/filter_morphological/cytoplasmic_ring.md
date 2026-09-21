<h4 id="cytoring"><a href="#cytoring">Create a cytoplasmic ring label mask</a></h4>
- Open the nuclei label mask image [xy_8bit_labels__nuclei](https://github.com/NEUBIAS/training-resources/raw/master/image_data/watershed/xy_8bit_labels__nuclei.tif).
- Create cytoplasmic rings by dilating the labels and subtracting the original (or slightly dilated) input nuclei labels.
- Note that a naive morphological dilation will not work here as close by nuclei will grow into each other. 
