// Close all images
run("Close All")

// Open the first image 
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xyc_16bit__hoechst_phalloidin_tile_01.tif")
makeLine(50, 50, 2250, 2250);
run("Plot Profile");

// Open the first image 
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xyc_16bit__hoechst_phalloidin_tile_02.tif")
makeLine(50, 50, 2250, 2250);
run("Plot Profile");

// Open the slide image
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_16bit__homogeneous_slide.tif")
makeLine(50, 50, 2250, 2250);
run("Plot Profile");