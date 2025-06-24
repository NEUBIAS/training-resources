/**
 * 2D Nuclei area measurement
 * 
 * Requirements:
 *   - Update site: IJPB-Plugins (MorpholibJ)
 */


// Get input and output directories from the user
inputDir = getDirectory("Choose Input Directory");
if (inputDir == "") exit("User cancelled input directory selection.");
outputDir = getDirectory("Choose Output Directory");
if (outputDir == "") exit("User cancelled output directory selection.");

// Processing parameters
// Note that one could decide to expose the below parameters in the above UI, too.
// But then one would need to somehow document their values for each run of the script.
// Like this, one could save the whole script with the analysis results for documentation purposes.
threshold = 25;


// Clean up and avoid popping up of image windows during run
run("Close All");
run("Clear Results");
setBatchMode(true);

// init options
run("Options...", "iterations=1 count=1 black do=Nothing");

// Get list of files in the input directory
list = getFileList(inputDir);

// Loop through all files in the directory
for (i = 0; i < list.length; i++) {
    fileName = list[i];
    // Skip directories and non-image files (basic check)
    if (File.isDirectory(inputDir + fileName) || startsWith(fileName, ".") || !(endsWith(fileName, ".tif") || endsWith(fileName, ".tiff"))) {
        print("Skipping: " + fileName);
        continue;
    }
    
    print("Processing: " + inputDir + fileName);

    // open and process
    //
    open(inputDir + fileName);

    // extract image name to create output file names (s.b.)
    imageName = File.getNameWithoutExtension(fileName);

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
    run("Clear Results"); // Clear results for the next image
    close(); // Close the current image
}

setBatchMode(false); // Restore normal display mode
run("Close All"); // Close any remaining windows (like results table if not cleared properly)
print("Batch processing finished.");
