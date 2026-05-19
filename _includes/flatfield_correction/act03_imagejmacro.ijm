run("Close All");
// Open images of hoechst
// These are several positions stacked as a "Z-stack"
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_16bit__hoechst_downsampled_stack.tif");
rename("stack");

// Open the camera background
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_16bit__bg_camera_downsampled.tif");
rename("camera_bg");

// We subtract the camera background and the result is converted to 32 bit - Important for subsequent normalization
imageCalculator("Subtract create 32-bit stack", "stack","camera_bg");
rename("stack_bg_corrected");

// Compute an average image
run("Z Project...", "projection=[Average Intensity]");

// Smooth the image to obtain an homogeneous field
run("Gaussian Blur...", "sigma=50");
rename("flat_field_unnormalized");
run("Duplicate...", "title=flat_field_normalized");

//Compute the mean value and normalize
run("Clear Results");
run("Measure");
m = getResult("Mean", 0);
run("Divide...", "value="+m);
run("Enhance Contrast", "saturated=0.35");
