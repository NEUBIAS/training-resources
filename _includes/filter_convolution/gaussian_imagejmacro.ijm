// IJ-Macro that demonstrates the effects of a Gaussian 
// blur on a delta peak and example images

// Create a delta peak image
newImage("Delta Peak", "8-bit black", 5, 5, 1);
setPixel(2, 2, 255); // Set the center pixel to maximum intensity
print("Delta Peak Image:");
run("Print...", ""); // Print the image values to the log

// Apply a Gaussian blur with sigma 1 to the delta peak image
run("Gaussian Blur...", "sigma=1");
print("Gaussian Kernel (sigma=1):");
run("Print...", ""); // Print the blurred image values to the log

// Load an example image
open("/Users/tischer/Documents/training-resources/image_data/xy_8bit__spots_local_background_with_noise.tif");
//open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__spots_local_background_with_noise.tif");
rename("input");

// Apply Gaussian blur with sigma 1 to the example image
// Observe that this does not suffice to smooth the image
selectWindow("input");
run("Duplicate...", "title=gaussian_1");
run("Gaussian Blur...", "sigma=1");

// Apply Gaussian blur with sigma 7 to the example image
// Observe that now all noise seems gone while the structures are quite well preserved
selectWindow("input");
run("Duplicate...", "title=gaussian_7");
run("Gaussian Blur...", "sigma=7");


// Learning opportunities: 
// - Inspect Gaussian kernel with sigma 7, using the delta peak image trick
