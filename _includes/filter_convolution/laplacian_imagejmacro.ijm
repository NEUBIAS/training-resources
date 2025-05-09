// IJ-Macro that demonstrates the effects of a sipmle 
// Laplacian convolutional filter on prepared example data

// Open an input image
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__laplacian_test_input.tif");
rename("input");

// Duplicate such that the raw data is not overwritten
run("Duplicate...", "title=laplacian");

// Create and apply a simple Laplacian filter
run("Convolve...", "text1=[0 -1 0\n-1 4 -1\n0 -1 0\n\n]");

// Examine at the pixel intensities of the convolved image
// and study how the "response" of the image to the convolution 
// depends on the local structure of the input image.
