/*
 * Requirements:
 * - MorpholibJ, Update site: IJPB-Plugins
 *
 **/


// Distance measurements
run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__dist_trafo_b.tif");
rename("labels");
// Make invert mask of first label
run("Duplicate...", "title=binary");
run("Manual Threshold...", "min=1 max=1");
run("Convert to Mask");
run("Invert");
// Compute distance transform 
run("Chamfer Distance Map", "distances=[Chessknight (5,7,11)] output=[32 bits] normalize");
rename("dist");
run("Intensity Measurements 2D/3D", "input=dist labels=labels mean max min");
