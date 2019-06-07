#@File image
#@Integer radius

// open
run("Close All");
open(image);
rename("input");

// median filter
run("Duplicate...", "title=median");
run("Median...", "radius=31");

// image subtraction
imageCalculator("Subtract create 32-bit", "input","median");
