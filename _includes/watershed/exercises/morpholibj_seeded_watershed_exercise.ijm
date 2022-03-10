/*
 * Seeded watershed in Fiji
 * 
 * Requirements: 
 * - IJPB-Plugins update site
 */

run("Close All");
setOption("BlackBackground", true);

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__tubulin.tif");
rename("tubulin_mask");

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei.tif");
rename("nuclei_mask");

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__tubulin_smooth.tif");
rename("tubulin_smooth");
run("Invert"); // invert for watershed

// watershed on inverted tubulin with nuclei as seeds and binary tubulin as mask
run("Marker-controlled Watershed", "input=tubulin_smoot marker=nuclei_mask mask=tubulin_mask compactness=0 binary");