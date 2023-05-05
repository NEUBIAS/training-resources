/**
 * Required update sites: 
 *   - IJPB-Plugins (MorpholibJ)
*/
 
run("Close All");

// File › Open...
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__many_vesicles.tif");
run("Connected Components Labeling", "connectivity=4 type=[16 bits]");
run("glasbey_on_dark");
run("Histogram");
