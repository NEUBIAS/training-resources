// Parameters
//
threshold1 = 49; // two cells
threshold2 = 100; // only the bright cells
threshold3 = 5; // cells merge and some noise become segmented

// Code
//

// open
run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif");
rename("input");

// apply threshold 1
selectWindow("input");
run("Duplicate...", "title=threshold1");
setThreshold(threshold1, 65535);
setOption("BlackBackground", true);
run("Convert to Mask");

// apply threshold 2
selectWindow("input");
run("Duplicate...", "title=threshold2");
setThreshold(threshold2, 65535);
setOption("BlackBackground", true);
run("Convert to Mask");

// apply threshold 3
selectWindow("input");
run("Duplicate...", "title=threshold3");
setThreshold(threshold3, 65535);
setOption("BlackBackground", true);
run("Convert to Mask");
