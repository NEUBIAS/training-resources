run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes_crop.tif");
rename("input");
run("Duplicate...", "title=median");
run("Median...", "radius=7");
rename("background");
imageCalculator("Subtract create 32-bit", "input", "background");
rename("foreground");
run("Tile");
