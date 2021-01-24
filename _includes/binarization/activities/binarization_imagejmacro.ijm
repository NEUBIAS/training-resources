open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif");
setThreshold(49, 255);
setOption("BlackBackground", true);
run("Convert to Mask");

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif");
setThreshold(88, 255);
setOption("BlackBackground", true);
run("Convert to Mask");