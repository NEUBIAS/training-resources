// Create a series of binary masks and then a band of those
// Using for loops generalize the script for multiple erode operations

run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei/xy_8bit_binary__nuclei.tif");
rename("input");

// Erode once
selectWindow("input");
run("Duplicate...", "title=erode1");
run("Erode");
run("Outline");
// Erode twice
selectWindow("input");
run("Duplicate...", "title=erode2");
run("Erode");
run("Erode");
run("Outline");
// Merge images that contain "erode" in the title into one stack
run("Images to Stack", "name=Stack title=erode use");


