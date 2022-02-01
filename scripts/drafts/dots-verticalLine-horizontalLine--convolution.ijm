run("Close All");

// Load image
open("/Users/tischi/Documents/imagej-courses/data/convolution/dots-verticalLine-horizontalLine/input01.tif");
input = getTitle();
run("Enhance Contrast", "saturated=0.35");
run("Maximize");

selectWindow(input);
run("Duplicate...", "title=dup");
run("Convolve...", "text1=[-1 +2 -1\n-1 +2 -1\n-1 +2 -1\n]");
rename("VerticalLineConvolution");
run("Enhance Contrast", "saturated=0.35");
run("Maximize");

selectWindow(input);
run("Duplicate...", "title=dup");
run("Convolve...", "text1=[-1 -1 -1\n+2 +2 +2\n-1 -1 -1\n]");
rename("HorizontalLineConvolution");
run("Enhance Contrast", "saturated=0.35");
run("Maximize");

imageCalculator("Add create", "VerticalLineConvolution","HorizontalLineConvolution");
rename("HorizontalLineConvolution_Add_VerticalLineConvolution");

selectWindow("HorizontalLineConvolution_Add_VerticalLineConvolution");
run("Duplicate...", "title=dup");
setThreshold(5, 255);
setOption("BlackBackground", false);
run("Convert to Mask");
run("Invert LUT");
rename("Result");
run("Maximize");
