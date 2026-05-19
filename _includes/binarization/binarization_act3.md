<h4 id="abovebackground"><a href="#abovebackground">Threshold based on noise measurement</a></h4>

Here we set the threshold value `t` such that it is higher than the background intensity plus some noise level.

* Open the image [xy_8bit__two_cells.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif)
* Measure the mean `m` and standard deviation `s` of the intensity in a backgroun region.
* Set the threshold as `t = m + N*s` choosing some `N` larger than 1; `N` effectively determines the statistical significance with which the values above `t` are foreground pixels.

