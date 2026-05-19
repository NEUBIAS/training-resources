// IJ-Macro that demonstrates the effects of a sipmle 
// Laplacian convolutional filter on an example image

// Open an input image
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__laplacian_test_input.tif");
rename("input");

// Pick a few (three) interesting locations in the image
// and manually compute the response to the
// Laplacian Kernel: 
// [0 -1 0]
// [-1 4 -1]
// [0 -1 0]
// Note down the results to compare with the below
// automated analysis.

// Duplicate the input image 
// such that the raw data is not overwritten
run("Duplicate...", "title=laplacian");

// Create and apply a simple Laplacian filter
run("Convolve...", "text1=[0 -1 0\n-1 4 -1\n0 -1 0\n]");

// Examine at the pixel intensities of the convolved image
// and study how the "response" of the image to the convolution 
// depends on the local structure of the input image.
