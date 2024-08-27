run("Close All");
//Make sure black background in Process > Binary > Options is set to true
setOption("black background", true);

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__three_spots_different_size.tif");
// Image > Rename
rename("binary");
run("Set... ", "zoom=400 x=29 y=25");
// Erosion, use default binary IJ binary operations
// It is a radius 1 squared SE, i.e. 3x3 SE

// Image > Duplicate, name it eroded
run("Duplicate...", "title=eroded");
//Process > Binary > Erode
run("Erode");
run("Set... ", "zoom=400 x=29 y=25");
// Apply second erosion will remove small dot
// Image > Duplicate, name it eroded_twice
run("Duplicate...", "title=eroded_twice");
// Process > Binary > Erode
run("Erode");
run("Set... ", "zoom=400 x=29 y=25");
// Use MorpholibJ and a radius 2, i.e. 5x5 squared structuring element
// This corresponds to 2 sequntial 3x3 erosions
selectWindow("binary");
// Plugins > MorpholibJ > Filtering > Morphological Filters 
// Select Erosion, Element Square 
run("Morphological Filters", "operation=Erosion element=Square radius=2");
rename("erosion_radius2");
run("Set... ", "zoom=400 x=29 y=25");
// Dilation, use MorpholibJ
selectWindow("binary");
// Plugins > MorpholibJ > Filtering > Morphological Filters
// Use MorpholibJ and a radius 2, i.e. 5x5 squared structuring element
run("Morphological Filters", "operation=Dilation element=Square radius=1");
rename("dilation_radius1");
run("Set... ", "zoom=400 x=29 y=25");
// Dilation, use MorpholibJ
selectWindow("binary");
// Plugins > MorpholibJ > Filtering > Morphological Filters
// Use MorpholibJ and a radius 2, i.e. 5x5 squared structuring element
run("Morphological Filters", "operation=Dilation element=Square radius=2");
rename("dilation_radius2");
run("Set... ", "zoom=400 x=29 y=25");
run("Tile")

