run("Close All");

//File > Open...
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_noisy_squares_different_size.tif");
// Image > Duplicate...
run("Duplicate...", "title=Mean_1");
// Image > Duplicate...
run("Duplicate...", "title=Mean_2");
// Image > Duplicate...
run("Duplicate...", "title=Mean_5");

selectWindow("Median_1");
// Process › Filters › Mean...
run("Mean...", "radius=1");

selectWindow("Mean_2");
// Process › Filters › Mean...
run("Mean...", "radius=2");

selectWindow("Mean_5");
// Process › Filters › Mean...
run("Mean...", "radius=5");
run("Tile")