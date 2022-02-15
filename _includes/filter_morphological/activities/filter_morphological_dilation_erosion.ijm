run("Close All");
//Make sure black background in Process > Binary > Options is set to true
setOption("black background", true);

open("https://raw.githubusercontent.com/NEUBIAS/training-resources/master/image_data/xy_8bit_binary__two_spots_different_size.tif");
rename("binary");

// Erosion, use default binary IJ binary operations
// It is a radius 1 squared SE, i.e. 3x3 SE
run("Duplicate...", "title=eroded");
//Process > Binary > Erode
run("Erode");
rename("eroded");

// Apply second erosion will remove small dot
// Process > Binary > Erode
run("Erode");

// Use MorpholibJ and a radius 2, i.e. 5x5 squared structuring element
// This corresponds to 2 sequntial 3x3 erosions
selectWindow("binary");
// Plugins > MorpholibJ > Filtering > Morphological Filters
run("Morphological Filters", "operation=Erosion element=Square radius=2");


// Dilation, use MorpholibJ
selectWindow("binary");
// Plugins > MorpholibJ > Filtering > Morphological Filters
// Use MorpholibJ and a radius 2, i.e. 5x5 squared structuring element
run("Morphological Filters", "operation=Dilation element=Square radius=1");





