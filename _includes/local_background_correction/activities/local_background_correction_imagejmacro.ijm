run("Close All");

// Open data
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__some_spots_with_uneven_bg.tif");
rename("input");

// Create background image
run("Duplicate...", "title=background");
run("Median...", "radius=15");
rename("background");

// Create foreground image
imageCalculator("Subtract create 32-bit", "input","background");
rename("foreground");

run("Tile");

// Create line profiles for more quantitative visualisation of the process
makeLine(99,200,81,121,82,87,91,64,230,26);
run("Plot Profile");
selectWindow("input");
run("Restore Selection");
run("Plot Profile");




