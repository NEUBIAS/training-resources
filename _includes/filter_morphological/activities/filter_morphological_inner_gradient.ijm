run("Close All");
//Make sure black background in Process > Binary > Options is set to true
setOption("black background", true);

open("https://raw.githubusercontent.com/NEUBIAS/training-resources/master/image_data/xy_8bit_binary__h2b_bg_corr.tif");

// Internal gradient is the original - eroded image
// Shown as step by step process
run("Morphological Filters", "operation=Erosion element=Square radius=1");
imageCalculator("Subtract create", "xy_8bit_binary__h2b_bg_corr.tif","xy_8bit_binary__h2b_bg_corr-Erosion");
rename("Internal_gradient");

run("Merge Channels...", "c2=xy_8bit_binary__h2b_bg_corr.tif c6=Internal_gradient create keep");

//Internal gradient
selectWindow("xy_8bit_binary__h2b_bg_corr.tif");
run("Morphological Filters", "operation=[Internal Gradient]  element=Square radius=1");

run("Tile")