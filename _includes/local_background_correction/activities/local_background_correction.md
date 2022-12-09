## Various activities (SPLITME)

  - Activity 1 - Background subtraction using a median filter.
    - Open image [xy_8bit__some_spots_with_uneven_bg](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__some_spots_with_uneven_bg.tif)
    - Compute a background image using a median filter
    - Create a foreground image by subtracting the background image from the input image
    - (Optional) Segment the spots in the foreground image.
  - Activity 2 - Background subtraction using a maximum intensity projection.
    - Open image [xyt_8bit_polyp](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyt_8bit_polyp.tif)
    - Create a maximum intensity projection of this image.
      - Because the polyp is moving around and is darker than the background this will create a background image.
    - Create a foreground image by subtracting the maximum intensity projection from the original image.

