// Get input from user
#@File image (label="input image")
#@File (style="directory", label="output directory") outputDirectory

// Open image
run("Close All");
open(image);

// Binarize (Threshold)
setThreshold(24, 255);
setOption("BlackBackground", true);
run("Convert to Mask");

// Connected components
run("Connected Components Labeling", "connectivity=4 type=[16 bits]");

// Measure shape
run("Region Morphometry");

// Export results
saveAs("Results", outputDirectory + "/" + Table.title + ".csv");

// Clean up
run("Close All");
// TODO: close table 
