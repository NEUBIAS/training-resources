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
#@ File (label="Input image") inputImageFile
#@ File (label="Output directory", style="directory") outputDir

// Clean up, prevent popping up of image windows and initialise options
run("Close All");
run("Clear Results");
setBatchMode(true);
run("Options...", "iterations=1 count=1 black do=Nothing");

// open
open(inputImageFile);
imageName = File.getNameWithoutExtension(inputImageFile);

// process
rename("input");
run("Duplicate...", "title=denoise" );
run("Mean...", "radius=3");
run("Duplicate...", "title=binary" );
setThreshold(25, 65535);
run("Convert to Mask");
run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
run("glasbey_on_dark");
run("Label Size Opening", "min=100");
// save label mask image with border labels
saveAs("Tiff", outputDir + File.separator + imageName + "_labels_with_border.tif");
run("Remove Border Labels", "left right top bottom");
rename("labels");
// save label mask image without border labels
saveAs("Tiff", outputDir + File.separator + imageName + "_labels.tif");
run("Analyze Regions", "area");
// save results table
saveAs("Results", outputDir + File.separator + imageName + ".txt");
run("Close" ); // close results table
