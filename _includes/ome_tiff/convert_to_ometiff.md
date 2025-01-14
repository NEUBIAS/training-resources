<h4 id="convert"><a href="#convert">Convert an image file to OME-TIFF</a></h4>

- Download the image files [two_images.lif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_xyc__two_images.lif) 
and [xyz__multiple_images.czi](https://github.com/NEUBIAS/training-resources/raw/refs/heads/master/image_data/xyz__multiple_images.czi)
- Move the downloaded czi file to the following path: `~/ome_zarr_course/data/czi/xyz__multiple_images.czi`
- Open the files
    - Observe that each file contains multiple independent images 
    - Observe that the images in the lif file have different dimensions
    - Take note of important metadata, such as the spatial calibration
- Convert the files to OME-TIFF
- Open the OME-TIFFs 
    - Check whether the image data and metadata have been preserved