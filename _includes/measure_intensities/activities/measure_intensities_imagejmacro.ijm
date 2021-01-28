/**
 * Nuclei intensity measurments
 * 
 * Requirements:
 *   - Update site: IJPB-Plugins (MorpholibJ)
 * 
 */

run("Close All");
run("Options...", "iterations=1 count=1 black do=Nothing");


// Open the images, change their names, and make them bigger
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_float__h2b_bg_corr.tif");
rename("intensity");
run("Set... ", "zoom=400");

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b_bg_corr.tif");
rename("labels");
run("Set... ", "zoom=400");

// Measure the object intensities
run("Intensity Measurements 2D/3D", "input=intensity labels=labels mean max numberofvoxels");
