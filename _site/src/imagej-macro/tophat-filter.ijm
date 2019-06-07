#@File image
#@Integer radius

// open
run("Close All");
open(image);
rename("input");

// erode
run("Morphological Filters", "operation=Erosion element=Disk radius="+radius);

// dilate
run("Morphological Filters", "operation=Dilation element=Disk radius="+radius);

// dilate(erode(input)) = opening(input)

// subtract opening from input
// (no need for floating point, because there cannot be negative values)
imageCalculator("Subtract create", "input","input-Erosion-Dilation");
rename("tophat");

// all in one command:   tophat = input - dilate(erode(input))
// run("Morphological Filters", "operation=[White Top Hat] element=Disk radius=15");