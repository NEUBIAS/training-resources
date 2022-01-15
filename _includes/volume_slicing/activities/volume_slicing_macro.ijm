""" Open a multidimensional image and inspect its dimensions using orthogonal views """

// Close other open images
run("Close All");

// open image 
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif");

// run orthogonal views command
run("Orthogonal Views");