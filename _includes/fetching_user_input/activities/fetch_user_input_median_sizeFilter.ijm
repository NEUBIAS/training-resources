//Identify parameters to be fetched and write code to implement them

// close all opened windows
run("Close All");

// open sample blobs image
run("Blobs (25K)");

// Change to gray lookup table
run("Grays");

//Apply median filter with radius of your choice
run("Median...", "radius=3");

// Apply Otsu thresholding to binarize the image
run("Auto Threshold", "method=Otsu white");

// Run a size filter to discard smaller objects
run("Size Opening 2D/3D", "min=100");
