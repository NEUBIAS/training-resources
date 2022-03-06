- Mean filter
  - Open [xy_8bit__nuclei_very_noisy.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_very_noisy.tif)
  - It is helpful to first duplicate the image: **[Image > Duplicate...]** or **[Ctrl-Shift-D]**
    - `Title = mean_1`
  - Apply a mean filter to the image such that you can binarize the image into exactly three disjoint foreground regions (the three nuclei). The resulting mask should look like [xy_8bit_binary__nuclei_very_noisy.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei_very_noisy.tif)
    - (**[Process > Filters > Mean...]**)
      - `Radius = 1 pixels`
    - **[Image > Adjust > Threshold...]**
      - `**[X]** Dark Background`
      - `Lower threshold level = 31`
      - `Higher threshold level = 255`
      - Press `Set`
      - Press `Apply`
      - **[Image > Lookup Tables > Invert LUT]**
    - Repeat the procedure with radii = 2, 5, 7

  - What is the smallest size for the mean filter that does the job?
    - `Radius = 2 pixels` and `Lower threshold level = 30` (other values can also be chosen) can remove the noise and find the appropriate nuclei size after manual thresholding
  - What happens if the filter size increases?
    - The boundaries of segmented nuclei are smoother


- Structuring element inspection
  - Open [xy_8bit_binary__one_foreground_pixel.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__one_foreground_pixel.tif)
  - **[Image > Duplicate...]** or **[Ctrl-Shift-D]**
    - `Title = max_2`
  - (**[Process > Filters > Maximum...]**)
    - `Radius = 2 pixels`
