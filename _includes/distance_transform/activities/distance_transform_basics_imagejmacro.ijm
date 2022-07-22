/*
 * Requirements:
 * - MorpholibJ, Update site: IJPB-Plugins
 *
 **/

run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__dist_trafo_a/xy_8bit_binary__dist_trafo_a.tif");
// [Image > Rename...]
rename("binary");


// ImageJ distance map
selectWindow("binary");
// [Process > Binary > Options...] [x] black
run("Options...", "black"); // Otherwise results not in line with standard conventions
//[Image > Duplicate...]
run("Duplicate...", "Distance Map");
//[Process › Binary › Distance Map]
run("Distance Map"); // Within objects


selectWindow("binary");
//[Image > Duplicate...]
run("Duplicate...", " inverted");
// [Edit > Invert]
run("Invert");

// ImageJ distance map on inverted image
// [Image > Duplicate...]
run("Duplicate...", "Distance Map invert");
// [Process › Binary › Distance Map]
run("Distance Map"); // Data type limits maximal distance

// MorpholibJ distance map
selectWindow("inverted");
// [Plugins › MorphoLibJ › Binary Images › Chamfer Distance Map]
run("Chamfer Distance Map", "distances=[Borgefors (3,4)] output=[16 bits] normalize");
rename("Borgefors");
print(getTitle() + ": " + getPixel(0, 761));
selectWindow("invert");
// [Plugins › MorphoLibJ › Binary Images › Chamfer Distance Map]
run("Chamfer Distance Map", "distances=[Chessknight (5,7,11)] output=[16 bits] normalize");
rename("Chessknight");
print(getTitle() + ": " + getPixel(0, 761));