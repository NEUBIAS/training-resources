/*
 * Nuclei and cells segmentation in Fiji
 * 
 * Requirements: 
 * - IJPB-Plugins update site
 */

run("Close All");
setOption("BlackBackground", true);


// open the images
open("/Users/tischer/Documents/training-resources/image_data/cell_segmentation_workflow/xyc_16bit__nuclei_tubulin_full_image.tif");
makeRectangle(626, 272, 163, 156);
run("Crop");
run("Duplicate...", "duplicate title=input");
run("Split Channels", "keep");
run("Grays");
selectWindow("C1-input");
rename("cells");
run("Grays");
selectWindow("C2-input");
rename("nuclei");
run("Grays");

// create nuclei binary mask
selectWindow("nuclei");
run("Duplicate...", "title=nuclei-binary");
run("Median...", "radius=5");
setThreshold(33089, 65535);
run("Convert to Mask");

// smooth cells
selectWindow("cells");
run("Duplicate...", "title=cells-smooth");
run("Mean...", "radius=3");

// create cells binary mask
run("Duplicate...", "title=cells-binary");
setThreshold(33565, 65535);
run("Convert to Mask");

// perform seeded watershed on inverted and smoothed cell signal
selectWindow("cells-smooth");
run("Duplicate...", "title=cells-smooth-invert");
run("Invert");
run("Marker-controlled Watershed", "input=cells-smooth-invert marker=nuclei-binary mask=cells-binary compactness=0 binary use");
rename("watershed-segmentation");

// remove border cells and change LUT
run("Remove Border Labels", "left right top bottom");
rename("cell-segmentation")
run("glasbey_on_dark");

// overlay on input image
selectWindow("cells");
run("Enhance Contrast", "saturated=0.35");
run("Add Image...", "image=cell-segmentation x=0 y=0 opacity=40");;

run("Tile");
