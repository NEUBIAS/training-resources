run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nup_bgsubtracted.tif");
run("Enhance Contrast", "saturated=0.35");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__nup.tif");

// Measure intensities for each label, Plugins > MorpholibJ > Analyze > Intensity Measurements 2D/3D
run("Intensity Measurements 2D/3D", "input=xy_8bit__nup_bgsubtracted.tif labels=xy_8bit_labels__nup.tif mean max min median numberofvoxels");

// Check if label mask fit our expected rim
// Image > Overlay > Add Image...
selectWindow("xy_8bit__nup_bgsubtracted.tif");
run("Add Image...", "image=xy_8bit_labels__nup.tifx=0 y=0 opacity=50");
