run("Close All");

// Compute the normalized flat field

// load a bright homogeneous image (standard slide)
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_16bit__homogeneous_slide.tif");
rename("bright_image");

// load the camera background
// Drag and drop
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_16bit__bg_camera.tif");

// [Image › Rename...]
rename("camera_bg");

// Subtract the camera background
// [Process › Image Calculator...]
imageCalculator("Subtract create 32-bit", "bright_image","camera_bg");

// Smooth the result to remove noise
// [Process › Filters › Gaussian Blur...]
run("Gaussian Blur...", "sigma=50");

//Compute the mean value and normalize
// Make sure the that you can measure the mean
run("Set Measurements...", "area mean display redirect=None decimal=3");
// [ Analyze › Clear Results]
run("Clear Results");
// [ Analyze › Measure]
run("Measure");
// Copy value of mean 
m = getResult("Mean", 0);

// Perform normalization 
// [Process › Math › Divide...]
run("Divide...", "value="+m);

// [Image › Rename...]
rename("flat_field_normalized");
run("Enhance Contrast", "saturated=0.35");
