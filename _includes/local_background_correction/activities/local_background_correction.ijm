run("Close All");

// Open data
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__spots_local_background_with_noise.tif");
rename("input");

// Create background image
run("Duplicate...", "title=background");
run("Median...", "radius=30");
rename("background");

// Create foreground image
imageCalculator("Subtract create 32-bit", "input","background");
rename("foreground");

run("Tile");

// Make line profiles to quantitatively display what happened
run("Line Width...", "line=7");

selectWindow("input");
makeLine(30, 201, 272, 34);
run("Plot Profile");
Plot.setLimits(0,290,-30.0,250);

selectWindow("background");
makeLine(30, 201, 272, 34);
run("Plot Profile");
Plot.setLimits(0,290,-30.0,250);

selectWindow("foreground");
makeLine(30, 201, 272, 34);
run("Plot Profile");
Plot.setLimits(0,290,-30.0,250);



