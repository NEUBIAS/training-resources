#@ File (label="Input image") filePath
#@ Integer (label="Median filter radius", value=5) medianFilterRadius
#@ Integer (label="Minimum object size", value=50) minObjectSize

// Parameters
//filePath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif"
//medianFilterRadius = 5;
//minObjectSize = 100;

// close all opened windows
run("Close All");

// open image
open(filePath);

// Change to gray lookup table
run("Grays");

// Apply median filter with radius of your choice
run("Median...", "radius="+medianFilterRadius);

// Apply Otsu thresholding to binarize the image
run("Auto Threshold", "method=Otsu white");

// Run a size filter to discard smaller objects
run("Size Opening 2D/3D", "min="+minObjectSize);
