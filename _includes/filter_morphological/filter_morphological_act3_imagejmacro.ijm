run("Close All");
//Make sure black background in Process > Binary > Options is set to true
setOption("black background", true);

open("https://raw.githubusercontent.com/NEUBIAS/training-resources/master/image_data/xy_8bit_binary__h2b.tif");
rename("binary");

// Internal gradient is the original - eroded image
// Shown as step by step process
// Erode image
// Plugins > MorpholibJ > Filtering >  Morphological Filters
//   Operation = Erosion
//   Element = Square
//   Radius (in pixels) = 1
run("Morphological Filters", "operation=Erosion element=Square radius=1");
rename("eroded")
// Process > Image Calculator ... 
//    image1 = binary
//    operation = subtract
//    image2 = binary-Erosion
//    [x] Create enew window
imageCalculator("Subtract create", "binary","eroded");
rename("internal_gradient");

// Add internal_gradient as overlay
selectImage("binary");
// Image > Overlay > Add..
run("Add Image...", "image=internal_gradient x=0 y=0 opacity=50");

//Internal gradient with MorpholibJ

selectWindow("binary");
// Plugins > MorpholibJ > Filtering >  Morphological Filters
//   Operation = Erosion
//   Element = Square
//   Radius (in pixels) = 1
run("Morphological Filters", "operation=[Internal Gradient]  element=Square radius=1");

run("Tile")