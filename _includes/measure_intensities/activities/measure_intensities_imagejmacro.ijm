/**
 * Nuclei intensity measurments
 * 
 * Requirements:
 *   - Update site: IJPB-Plugins (MorpholibJ)
 * 
 */

run("Close All");
run("Options...", "iterations=1 count=1 black do=Nothing");

// Open the images, change their names, adapt LUT, and make them bigger
//
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_float__h2b_bg_corr.tif");
rename("intensity");
run("Set... ", "zoom=400");

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b_bg_corr.tif");
//open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__larger_regions_h2b_bg_corr.tif");
rename("labels");
run("glasbey_on_dark");
run("Set... ", "zoom=400");

run("Tile");

// Measure the object intensities
//
run("Intensity Measurements 2D/3D", "input=intensity labels=labels mean max numberofvoxels");

// Add the sum intensity measurement
//
IJ.renameResults("Results"); // otherwise below does not work...
for (row=0; row<nResults; row++) {
	sum = getResult("NumberOfVoxels", row) * getResult("Mean", row);
    setResult("sum", row, sum);
}
updateResults();
 