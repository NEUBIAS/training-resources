/*
 * Requirements: 
 * - MorpholibJ, Update site: IJPB-Plugins
 * 
 **/

run("Close All");

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_lablels__dist_trafo_a.tif");
rename("input");

// ImageJ distance map
run("Options...", "black"); // Otherwise results not in line with standard conventions
run("Duplicate...", "Distance Map");
run("Distance Map"); // Within objects

// Invert 
selectWindow("input");
run("Duplicate...", "invert");
run("Manual Threshold...", "min=0 max=0");
run("Convert to Mask");
rename("invert");

// ImageJ distance map on inverted image
run("Duplicate...", "Distance Map 2");
run("Distance Map"); // Data type limits maximal distance

// MorpholibJ distance map
selectWindow("invert");
run("Chamfer Distance Map", "distances=[Borgefors (3,4)] output=[16 bits] normalize");
rename("Borgefors");
print(getTitle() + ": " + getPixel(0, 761));
selectWindow("invert");
run("Chamfer Distance Map", "distances=[Chessknight (5,7,11)] output=[16 bits] normalize");
rename("Chessknight");
print(getTitle() + ": " + getPixel(0, 761));

// Distance measurements
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_lablels__dist_trafo_b.tif");


