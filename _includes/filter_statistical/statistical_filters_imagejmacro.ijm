run("Close All");

// File > Open...
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__statistical_filter_test_input.tif");
zoom();

// Manual activity:
// Choose one interesting 5x5 region
// in the image and manually compute
// the below statistical filters.
// Note down the resulting numbers and later check
// whether they agree with the below
// automated analysis.


// Image > Duplicate...
run("Duplicate...", "title=Minimum"); zoom();
run("Duplicate...", "title=Maximum"); zoom();
run("Duplicate...", "title=Mean"); zoom();
run("Duplicate...", "title=Median"); zoom();
run("Duplicate...", "title=Variance"); zoom();

// Apply Minimum filter
selectWindow("Minimum");
// Process › Filters › Minimum...
run("Minimum...", "radius=2");

// Apply Maximum filter
selectWindow("Maximum");
// Process › Filters › Maximum...
run("Maximum...", "radius=2");

// Apply Mean filter
selectWindow("Mean");
run("32-bit"); // Results of mean filter are generally not 8=bit
// Process › Filters › Mean...
run("Mean...", "radius=2");

// Apply Median filter
selectWindow("Median");
// Process › Filters › Median...
run("Median...", "radius=2");

// Apply Variance filter
selectWindow("Variance");
run("32-bit"); // Results of variance filter are generally not 8=bit
// Process › Filters › Variance...
run("Variance...", "radius=2");

// Arrange windows in a tiled layout
run("Tile");

// Learning opportunities:
// - Check the result of a variance filter without converting the image to 32-bit float

function zoom() { 
	run("In [+]");
	run("In [+]");
	run("In [+]");
	run("In [+]");
}


