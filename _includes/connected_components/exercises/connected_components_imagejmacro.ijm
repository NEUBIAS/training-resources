/**
 * Connected components exercise
 * 
 * Required update sites: 
 *   - IJPB-Plugins (MorpholibJ)
 */

 
//run("Options...", "black");
run("Close All");

// File › Open...
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__many_vesicles.tif");
// Plugins › MorphoLibJ › Binary Images › Connected Components Labeling
run("Connected Components Labeling", "connectivity=4 type=[16 bits]");
// Image › Lookup Tables › glasbey_on_dark
run("glasbey_on_dark");

