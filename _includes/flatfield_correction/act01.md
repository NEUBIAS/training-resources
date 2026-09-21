<h4 id="flatfield_compute"><a href="#flatfield_compute">Compute a normalized flat field from a standard slide image</a></h4>
To perform a flat field correction we need to first compute a normalized flat field that can be used to correct 
the images acquired with the same modality. For this one can record an homogeneous fluorescent slide and then perform 
background subtraction and normalization. The resulting image will have values around 1.  Make sure that you work 
with the **correct bit-depth (32-bit or more)** to account for real numbers. 

 - Load the bright image [xy_16bit__homogeneous_slide.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_16bit__homogeneous_slide.tif)
 - Load the camera background [xy_16bit__bg_camera.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xy_16bit__bg_camera.tif)
 - Subtract the two images
 - Divide the resulting image by its mean


