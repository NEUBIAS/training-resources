run("Close All");

// Load image
open("/Users/tischi/Documents/imagej-courses/data/deep-convolution/edge-of-dots/input-01.tif");
input = getTitle();
run("Enhance Contrast", "saturated=0.35");
run("Maximize");

run("Duplicate...", "title=dup");
run("Convolve...", "text1=[-1 -1 -1\n-1 +2 -1\n-1 -1 -1\n]");
rename("SpotConvolution");
run("Enhance Contrast", "saturated=0.35");
run("Maximize");

run("Duplicate...", "title=dup");
run("Bin...", "x=2 y=2 bin=Max");
rename("SpotConvolution-MaxBin");
run("Enhance Contrast", "saturated=0.35");
run("Maximize");

selectWindow("SpotConvolution-MaxBin");
run("Duplicate...", "title=dup");
run("Convolve...", "text1=[-1 -1 -1\n+2 +2 +2\n-1 -1 -1\n]");
rename("SpotConvolution-MaxBin-HorizontalLine");
run("Enhance Contrast", "saturated=0.35");
run("Maximize");

selectWindow("SpotConvolution-MaxBin");
run("Duplicate...", "title=dup");
run("Convolve...", "text1=[-1 +2 -1\n-1 +2 -1\n-1 +2 -1\n]");
rename("SpotConvolution-MaxBin-VerticalLine");
run("Enhance Contrast", "saturated=0.35");
run("Maximize");

selectWindow("SpotConvolution-MaxBin-HorizontalLine");
run("Duplicate...", "title=dup");
run("Bin...", "x=5 y=5 bin=Max");
rename("SpotConvolution-MaxBin-HorizontalLine-MaxBin");
run("Maximize");

selectWindow("SpotConvolution-MaxBin-VerticalLine");
run("Duplicate...", "title=dup");
run("Bin...", "x=5 y=5 bin=Max");
rename("SpotConvolution-MaxBin-VerticalLine-MaxBin");
run("Maximize");

imageCalculator("Add create", "SpotConvolution-MaxBin-HorizontalLine-MaxBin","SpotConvolution-MaxBin-VerticalLine-MaxBin");
run("Enhance Contrast", "saturated=0.35");
rename("Addition");
run("Maximize");

run("Duplicate...", "title=dup");
setThreshold(17, 255);
setOption("BlackBackground", false);
run("Convert to Mask");
run("Invert LUT");
rename("Result");
run("Maximize");
