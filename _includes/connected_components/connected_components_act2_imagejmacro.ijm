
// 3D connected components labeling (6-connected)

open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_binary__spots.tif");
rename("binary");
run("Connected Components Labeling", "connectivity=6 type=[8 bits]");
run("glasbey_on_dark");
setMinAndMax(0, 255); // Note: surprisingly this determines the content of below histogram!
run("Histogram", "stack");