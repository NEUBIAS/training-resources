/*
 * Shape watershed (with distance transform)  in Fiji
 * 
 * Requirements: 
 * - IJPB-Plugins update site
 */

run("Close All");
setOption("BlackBackground", true);

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__touching_objects_same_intensity.tif");
rename("input");

// create mask
run("Duplicate...", "title=mask");
setThreshold(83, 255);
run("Convert to Mask");


run("Chamfer Distance Map", "distances=[Chessknight (5,7,11)] output=[16 bits] normalize");
rename("dist");
run("Invert");

// watershed without mask
run("Classic Watershed", "input=dist mask=None use min=0 max=255");

// watershed mask
run("Classic Watershed", "input=dist mask=mask use min=0 max=255");