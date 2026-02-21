<h4 id="flatfield_retro"><a href="#flatfield_retro">Compute a normalized flat field retrospectively</a></h4>
Often we can't record a standard image or it may not reflect our sample peculiarities. 
In this case if we have enough images we can compute an approximate flat field. A typical operation is to compute an average of all images followed by smoothing.  

Make sure that you work with the **correct bit-depth (32-bit or more)** to account for real numbers. 

 - Load the a stack of images [xy_16bit__hoechst_downsampled_stack.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_16bit__hoechst_downsampled_stack.tif). These images have been acquired at several positions and then stacked together for convenience in a single file. 
 - Load the camera background [xy_16bit__bg_camera_downsampled.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_16bit__bg_camera_downsampled.tif)
 - Create a background corrected stack
 - Compute an average projection of the stack
 - Perform a smoothing using for example a gaussian up to the field become homogeneous
 - Normalize the obtained image by its mean