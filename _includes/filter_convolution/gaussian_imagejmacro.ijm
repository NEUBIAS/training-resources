// IJ-Macro that demonstrates the effects of a Gaussian 
// blur on a delta peak and example images

// Open an input image
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__spots_local_background_with_noise.tif");
rename("input");

// Duplicate the input image to preserve the original
run("Duplicate...", "title=gaussian_sigma7");

// Apply a Gaussian filter
run("Gaussian Blur...", "sigma=7");