open("/Users/tischer/Documents/training-resources/image_data/xy_8bit_binary__test_structures.tif");
rename("input");
run("Duplicate...", " ");
run("Median...", "radius=2");
rename("median_5x5");
imageCalculator("Subtract create 32-bit", "input","median");
rename("difference");
// In order to copy and paste into powerpoint:
// run("Scale...", "x=10 y=10 width=640 height=640 interpolation=None create");