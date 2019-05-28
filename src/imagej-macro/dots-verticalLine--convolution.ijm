run("Close All");

// Load image
open("/Users/tischi/Documents/imagej-courses/data/convolution/dots-verticalLine/input01.tif");
input = getTitle();
run("Enhance Contrast", "saturated=0.35");
run("Maximize");

run("Duplicate...", "title=dup");
run("Convolve...", "text1=[-1 +2 -1\n-1 +2 -1\n-1 +2 -1\n]");
rename("VerticalLineConvolution");
run("Enhance Contrast", "saturated=0.35");
run("Maximize");

run("Duplicate...", "title=dup");
setThreshold(4, 255);
setOption("BlackBackground", false);
run("Convert to Mask");
run("Invert LUT");
rename("Result");
run("Maximize");
