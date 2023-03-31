// Close other open images
run("Close All");

// open image
openImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif")

// crop out the green bead
makeRectangle(118,142,37,37);
run("Duplicate...", "duplicate channels=1 slices=15-25");
rename("Green bead");

// Reslice green bead from the top, WITH interpolation
run("Reslice [/]...", "output=0.100 start=Top");
rename("Green bead viewed from the top, WITH interpolation")

// Reslice green bead from the top, WITHOUT interpolation
selectWindow("Green bead")
run("Reslice [/]...", "output=0.100 start=Top avoid");
rename("Green bead viewed from the top, WITHOUT interpolation")

run("Tile")
