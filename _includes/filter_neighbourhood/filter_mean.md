<h4 id="mean"><a href="#mean">Mean filter and structuring element exploration</a></h4>

- Explore the effect of a mean filter with different radii
  - Example image: [xy_8bit__nuclei_very_noisy.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_very_noisy.tif)
- Investigate the shapes of structuring elements
    - Sometimes you would like to know how the SE (the neighborhood) of a filter looks like. 
    - One way to do this is to apply a _maximum_ filter to a single white pixel and look at the resulting form.
    - Example image: [xy_8bit_binary__one_foreground_pixel.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__one_foreground_pixel.tif)
