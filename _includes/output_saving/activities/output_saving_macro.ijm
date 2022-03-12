// This macro uses the particle analyzer to measure features of shapes.
// Different outputs are saved: ROIs, results table, and label mask.

// specify an output directory
outputDir = FIXME

// close any pre-existing output you do not want in your saving results
roiManager("reset"); // clear any pre-existing ROIs
run("Clear Results"); // clear any pre-existing results
run("Close All"); // close any open images

// Run particle analyzer on binary shapes image 
run("Set Measurements...", "area centroid center perimeter bounding redirect=None decimal=3") // set desired measurements
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary_randomshapes.tif"); // open binary image with random shapes
run("Analyze Particles...", "size=0-2000 circularity=0-1 show=[Count Masks] display add") // run the particle analyzer
run("glasbey")
roiManager("Select All") // select all rois
roiManager("Save", outputDir + File.separator + "shapes_ROIset_macro.zip"); // save rois to output directory
saveAs("Results", outputDir + File.separator + "shapes_results_macro.txt"); // save results file to output directory
saveAs("Tiff", outputDir + File.separator + "shapes_labels_macro.tif"); // save label mask to output directory
