/**
 * 2D nuclei segmentation, including
 *  - image denoising by a mean filter
 *  - removal of small and boundary objects
 *  
 * Requirements:
 *   - Update site: IJPB-Plugins (MorpholibJ)
 * 
 */

// Fetch input image file and output directory using Scijava script parameters
// TODO Fetch input image
// TODO Fetch output directory

// Configure options
run("Options...", "iterations=1 count=1 black do=Nothing");

// Clear up previous images and results
// TODO
// Avoid popping up of images during run
// TODO

// open
open(file);

// process
rename("input");
run("Duplicate...", "title=denoise" );
run("Mean...", "radius=3");
run("Duplicate...", "title=binary" );
setThreshold(25, 255);
run("Convert to Mask");
run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
run("glasbey_on_dark");
run("Label Size Opening", "min=100");
// save label mask image with border labels
// TODO
run("Remove Border Labels", "left right top bottom");
rename("labels");
// save label mask image without border labels
// TODO
run("Analyze Regions", "area");
// save results table
// TODO
