run("Close All");
//Make sure black background in Process > Binary > Options is set to true
setOption("black background", true);
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__for_open_and_close.tif")
rename("binary");

// Opening, use default binary IJ binary operations in sequence
run("Duplicate...", "title=opening");
//Process > Binary > Erode
run("Erode");
//Process > Binary > Dilate
run("Dilate");
// See how the thin structure disappear

// Opening, use default binary IJ binary operations
selectWindow("binary");
run("Duplicate...", "title=opening2");
//Process > Binary > Open
run("Open");


// Opening, use MorpholibJ, try different radii
selectWindow("binary");
// Plugins > MorpholibJ > Filtering > Morphological Filters
run("Morphological Filters", "operation=Opening element=Square radius=1");
rename("binary-Opening_radius=1");

selectWindow("binary");
// Plugins > MorpholibJ > Filtering > Morphological Filters
run("Morphological Filters", "operation=Opening element=Square radius=3");
rename("binary-Opening_radius=3");
// see how also the small blob disappear, side of large blob are deformed


// Closing, use MorpholibJ
selectWindow("binary");
// Plugins > MorpholibJ > Filtering > Morphological Filters
run("Morphological Filters", "operation=Closing element=Square radius=1");
rename("binary-Closing_radius=1");
// Fill the hole in big blob
// Closes the gap
run("Tile")
