/**
 * 2D Nuclei area measurement
 * 
 * Requirements:
 *   - Update site: IJPB-Plugins (MorpholibJ)
 */

// Scijava script parameters
// Use the [ Batch ] button in the Fiji script editor to automatically analyse multiple files
#@ File (label="Input image") inputImageFile
#@ File (label="Output directory", style="directory") outputDir

// Processing parameters
threshold = 25;

// Clean up and avoid popping up of image windows during run
run("Close All");
run("Clear Results);
setBatchMode(true);

// init options
run("Options...", "iterations=1 count=1 black do=Nothing");

// open and process
//
open(inputImageFile);

// extract image name to create output file names (s.b.)
imageName = File.getNameWithoutExtension(inputImageFile);

// segment
setThreshold(threshold, 65535);
run("Convert to Mask");
run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
run("glasbey_on_dark");
// save segmentation
saveAs("Tiff", outputDir + File.separator + imageName + "_labels.tif");
// measure
run("Analyze Regions", "area");
// save measurements
saveAs("Results", outputDir + File.separator + imageName + ".txt");

run("Close" ); // close results table
