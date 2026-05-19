/**
 * 2D Nuclei area measurement
 * 
 * Requirements:
 *   - Update site: IJPB-Plugins (MorpholibJ)
 */

// Scijava script UI parameters
// Use the [ Batch ] button in the Fiji script editor to automatically analyse multiple files
#@ File (label="Input image") inputImageFile
#@ File (label="Output directory", style="directory") outputDir

// Processing parameters
// Note that one could decide to expose the below parameters in the above UI, too.
// But then one would need to somehow document their values for each run of the script.
// Like this, one could save the whole script with the analysis results for documentation purposes.
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
