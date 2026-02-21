run("Close All");
// Load image where we want to apply a flat field correction 
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xyc_16bit__hoechst_phalloidin_tile_01.tif");
rename("sample_img");

// load the camera background
// Drag and drop
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_16bit__bg_camera.tif");

// [Image › Rename...]
rename("camera_bg");

// Subtract the camera background
imageCalculator("Subtract create 32-bit stack", "sample_img","camera_bg");
rename("sample_img_bg_corr");

// load the normalized flat-field
// Drag and drop
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_32bit__flat_field.tif");
rename("flat_field_normalized");
run("Enhance Contrast", "saturated=0.35");
// Flat field correction
imageCalculator("Divide create 32-bit stack", "sample_img_bg_corr","flat_field_normalized");
rename("sample_img_flat_field_corr");
run("Enhance Contrast", "saturated=0.35");
run("Tile");

