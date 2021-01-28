/**
 * Global background correction
 */


run("Close All");

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__nuclei_high_dynamic_range_with_offset.tif");

// Image › Adjust › Brightness/Contrast...
setMinAndMax(100, 115);

// Use the Rectangle tool from ImageJ's tool bar
makeRectangle(4, 8, 20, 42);

// Analyze › Set Measurements...
run("Set Measurements...", "mean redirect=None decimal=3");

// Analyze › Measure
run("Measure");

// Edit › Selection › Select None (VERY IMPORTANT, otherwise everything you do later will only operate on this region)
run("Select None");

// Image › Duplicate...
run("Duplicate...", "title=float");

// Image › Type › 32-bit
run("32-bit");

// Process › Math › Subtract...
run("Subtract...", "value=104.399");

// Image › Adjust › Brightness/Contrast...
setMinAndMax(-5, 10);

// Use the Line tool from ImageJ's tool bar
makeLine(17, 7, 69, 94);

// Analyze › Plot Profile
run("Plot Profile");
