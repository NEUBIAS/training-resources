/*
 * Basic watershed in Fiji
 * 
 * Requirements: 
 * - IJPB-Plugins update site
 */

run("Close All");
setOption("BlackBackground", true);


open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__touching_objects.tif");
rename("input");

// create mask
run("Duplicate...", "title=mask");
setThreshold(14, 255);
run("Convert to Mask");

// invert
selectWindow("input");
run("Duplicate...", "title=invert");
run("Invert");
run("Enhance Contrast", "saturated=0.35");

// watershed
run("Classic Watershed", "input=invert mask=None use min=0 max=255");
rename("watershed");

// watershed with mask
selectWindow("invert");
run("Classic Watershed", "input=invert mask=mask use min=0 max=255");
rename("instance segmentation");
run("glasbey_inverted");