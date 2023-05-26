// Open image
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyt_8bit_polyp.tif");
// Create maximum intensity projection
run("Z Project...", "projection=[Max Intensity]");
// Subtract maximum intensity projection from original image
imageCalculator("Subtract create 32-bit stack", "xyt_8bit_polyp.tif","MAX_xyt_8bit_polyp.tif");
