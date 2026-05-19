open("/Users/tischer/Documents/training-resources/image_data/xy_8bit__spots_local_background_with_noise.tif");
rename("input");

// Compuate Laplacian of the image to enhance spots and edges
// Observe that this yields a very noisy resulting image
selectWindow("input");
run("Duplicate...", "title=Laplacian");
run("32-bit");
run("Convolve...", "text1=[0 -1 0\n-1 4 -1\n0 -1 0\n\n]");
run("Enhance Contrast", "saturated=0.35");

// To reduce the noise first apply a Gaussian 
// and then a Laplacian.
// This is a very common operation, also called 
// "Laplacian of Gaussian (LoG)".
// Visually inspect the image to determinte
// a sigma for the Gaussian kernel that 
// matches the size of the structures 
// that you want to enhance.
selectWindow("input");
run("Duplicate...", "title=LoG");
run("32-bit");
run("Gaussian Blur...", "sigma=7");
run("Convolve...", "text1=[0 -1 0\n-1 4 -1\n0 -1 0\n\n]");
run("Enhance Contrast", "saturated=0.35");


// Learning opportunities:
// - Explore how different values for the Gaussian sigma change the result
// - Observe how the results look very bad if you don't convert to float (32bit)
