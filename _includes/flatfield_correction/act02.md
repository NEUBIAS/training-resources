<h4 id="flatfield_perform"><a href="#flatfield_perform">Perform the flat-field correction</a></h4>
Given that we have normalized flat-field we can correct any image that has been recorded with same
modality (objective, ligh-source). We computed the flat-field in the previous activity. 

Make sure that you work with the **correct bit-depth (32-bit or more)** to account for real numbers. 

 - Load the sample image [xyc_16bit__hoechst_phalloidin_tile_01.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xyc_16bit__hoechst_phalloidin_tile_01.tif)
 - Load the camera background [xy_16bit__bg_camera.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_16bit__bg_camera.tif)
 - Subtract the two images
 - Load the normalized flat field [xy_32bit__flat_field.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_32bit__flat_field.tif)
 - Divide the background subtracted sample image by the normalized flat field