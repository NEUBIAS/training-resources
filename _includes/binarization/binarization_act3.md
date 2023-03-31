#### Threshold above background

Here we set the threshold value `t` as a value x-times above the background + noise. 

* Open the image [xy_8bit__two_cells.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif)
* Measure the mean `m` and standard deviation `s` of the intensity in a region where there are no foreground pixels
* Set the threshold as `t = x*(m + s)` where `x>1`

