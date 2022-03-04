run("Close All");
// File › Open...
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__noisy_two_nuclei.tif");
// Image › Rename...
rename("input");
// Image › Duplicate...
run("Duplicate...", "title=mean_1" );
// Process › Filters › Mean...
run("Mean...", "radius=1");

selectWindow("input");
run("Duplicate...", "title=mean_7" );
run("Mean...", "radius=7");

run("Tile");
