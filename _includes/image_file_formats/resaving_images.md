<h4 id="save"><a href="#save">Resave images in various file formats</a></h4> 

Resaving images in different file formats very often leads to a loss of metadata or distortion of the pixel values. It is critical to be aware of this!

##### Checks to be done after each resaving
- Open the resaved image in all relevant applications and check whether the pixels values and/or metadata are different from the original image
  - This is critical for the scientific integrity of the resaving
- Open the image in a web-browser and observe how the image is rendered
  - This can be useful to share previews with collaborators
 
##### Resave 8 bit single channel image as TIFF
- Open [xy_8bit__nuclei_PLK1_control.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_PLK1_control.tif) 
- Change the contrast limits
- Save as TIFF
- Do the above checks

##### Resave 8 bit single channel image as JPEG 
- Open [xy_8bit__nuclei_PLK1_control.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_PLK1_control.tif) 
- Change contrast such that the cells appear saturated
- Save as JPEG 
- Do the above checks

##### Resave 16 bit two channel movie as JPEG 
- Open [xyzct_16bit__mitosis.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzct_16bit__mitosis.tif)
- Select a timepoint in the middle of the movie 
- Save as JPEG
- Do the above checks

##### Resave 8 bit single channel movie as GIF
- Open  [xyt_8bit__mitocheck_incenp.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyt_8bit__mitocheck_incenp.tif)
- Change contrast such that cells appear saturated
- Save as GIF
- Do the above checks
