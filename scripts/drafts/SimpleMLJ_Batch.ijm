# @File image
# @File (style='directory') outputDir 

// Open image
open(image);

// Binarize
run("Auto Threshold", "method=Huang white");

// Connected components
run("Connected Components Labeling", "connectivity=4 type=[16 bits]");

// Measure
run("Analyze Regions", "area perimeter");

// Save
saveAs("Results", outputDir + File.separator + File.nameWithoutExtension + ".csv" );

// Clean up
run("Close")
run("Close")
run("Close")


