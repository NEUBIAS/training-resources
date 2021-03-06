run("Close All");

// File › Open...
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes_crop.tif");
// Image › Rename...
rename("input");
// Image › Duplicate...
run("Duplicate...", "title=median");
// Process › Filters › Median...
run("Median...", "radius=7");
// Image › Rename...
rename("background");
// Process › Image Calculator...
imageCalculator("Subtract create 32-bit", "input", "background");
// Image › Rename...
rename("foreground");
// Window › Tile
run("Tile");