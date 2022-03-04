/**
 * 2D and 3D connected components labeling
 * 
 * Required update sites: 
 *   - IJPB-Plugins (MorpholibJ)
 */

run("Close All");

//  2D connected components labeling

// File › Open...
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei.tif");
// Image › Rename...
rename("binary");

// 4-connected

// Plugins › MorphoLibJ › Binary Images › Connected Components Labeling
run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
// Image › Lookup Tables › glasbey_on_dark
run("glasbey_on_dark");
// Image › Adjust › Brightness/Contrast...
setMinAndMax(0, 20);

// 8-connected

selectWindow("binary");
run("Connected Components Labeling", "connectivity=8 type=[8 bits]");
run("glasbey_on_dark");
setMinAndMax(0, 20);

run("Tile");

// 3D connected components labeling (6-connected)

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_binary__spots.tif");
rename("binary");
run("Connected Components Labeling", "connectivity=6 type=[8 bits]");
run("glasbey_on_dark");
setMinAndMax(0, 255); // Note: surprisingly this determines the content of below histogram!
run("Histogram", "stack");

