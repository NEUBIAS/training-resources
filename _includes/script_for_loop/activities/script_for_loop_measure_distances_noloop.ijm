/*
 * Measure distance of all labels to the first label 
 * 
 * Requirements: 
 * - IJPB-plugins update site
 */
 
// This is what we would do when recording a macro

run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit_labels__nuclei.tif");
rename("labels");
run("Duplicate...", "title=binary");
run("Manual Threshold...", "min=1 max=1");
run("Convert to Mask");
run("Invert");
run("Chamfer Distance Map", "distances=[Chessknight (5,7,11)] output=[16 bits] normalize");
run("Intensity Measurements 2D/3D", "input=binary-dist labels=labels mean max min");
Table.rename("binary-dist-intensity-measurements", "dist_label"+labelID);

