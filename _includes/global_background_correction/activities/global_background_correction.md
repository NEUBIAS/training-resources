## Subtract the background from an image
  - Open image [xy_16bit__nuclei_high_dynamic_range_with_offset](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__nuclei_high_dynamic_range_with_offset.tif)
  - Measure the background using a manually defined region
  - Measure the mean intensities inside of two nuclei using manually defined regions
    - Choose rather dim nuclei of different intensities
    - Measure the intensity ratio with and without background correction
  - Subtract the background value from the image
    - Appreciate that this yields a non-zero background for unsigned integer data types and that a floating point data type is thus necessary
  - Open image [xy_16bit__scanR_datatype_issue](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif)
    - Discuss automated global background estimation methods, e.g.
      - mode
      - mean intensity outside objects

