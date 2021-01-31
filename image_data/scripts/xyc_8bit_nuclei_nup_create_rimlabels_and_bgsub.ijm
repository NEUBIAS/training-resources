run("Close All");
open("D:/Code/training-resources/image_data/xyc_8bit__nuclei_nup.tif");
rename("image")
selectWindow("image");
run("Split Channels");
selectWindow("C1-image");
//Create mask nuclei
run("Median...", "radius=10");
setAutoThreshold("Default dark");
run("Convert to Mask");
run("Fill Holes");
run("Erode");
// Create rim
run("Morphological Filters", "operation=[Gradient] element=Disk radius=3");
run("Connected Components Labeling", "connectivity=4 type=[8 bits]");
run("Remove Border Labels", "left right top bottom");
run("Remap Labels");
run("glasbey on dark");
rename("labels");


// Create a background subtracted C2
selectWindow("C2-image");
run("Duplicate...", "median_bg");
rename("C2_median_bg")
//Create mask nuclei
run("Median...", "radius=20");
imageCalculator("Subtract create 32-bit", "C2-image","C2_median_bg");
rename("C2-bg_subtracted");
run("Enhance Contrast", "saturated=0.35");
run("Intensity Measurements 2D/3D", "input=C2-bg_subtracted labels=labels mean max min median numberofvoxels");
run("Intensity Measurements 2D/3D", "input=C2-image labels=labels mean max min median numberofvoxels");

// Check overlay
//run("Add Image...", "image=C1-xyc_8bit__NUP_nuclei01-Gradient-lbl-killBorders x=0 y=0 opacity=50");
