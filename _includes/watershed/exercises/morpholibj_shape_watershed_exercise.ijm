/*
 * Shape watershed (with distance transform)  in Fiji
 * 
 * Requirements: 
 * - IJPB-Plugins update site
 */

run("Close All");
setOption("BlackBackground", true);

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__several_touching_nuclei.tif");
rename("input");

// create mask
run("Duplicate...", "title=mask");
setThreshold(61, 255);
run("Convert to Mask");

run("Chamfer Distance Map", "distances=[Chessknight (5,7,11)] output=[16 bits] normalize");
rename("dist");
run("Invert");
// remove spurious minima in distance map (choose sigma smaller than object radii)
run("Mean...", "sigma=2");

// watershed with mask
run("Classic Watershed", "input=dist mask=mask use min=0 max=255");