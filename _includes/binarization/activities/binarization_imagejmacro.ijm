// Parameters
threshold1 = 49;
threshold2 = 100;

run("Close All");

// Code
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif");
setThreshold(threshold1, 65535);
setOption("BlackBackground", true);
run("Convert to Mask");

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif");
setThreshold(threshold2, 65535);
setOption("BlackBackground", true);
run("Convert to Mask");
