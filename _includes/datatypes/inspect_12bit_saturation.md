<h4 id="saturation_12bit"><a href="#saturation_12bit">Inspect a 12-bit image</a></h4> 

Saturation, i.e. pixel value at the upper end of the datatype, is a typical problem in fluorescence microscopy images. 

Inspecting 12-bit images, as acquired by some camera based systems, is particularly tricky, because 12-bit images are typically represented as 16-bit images, both on disk and within analysis software.

- Open [xy_12bit__saturated_plant.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_12bit__saturated_plant.tif)
- Observe that while this opens as 16-bit image there are many pixels at the highest value of 4095, which is the maximum of a 12-bit image.
