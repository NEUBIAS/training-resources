### Explore distance transform functionalities
  1. Distance transform basics
    - Open label mask [xy_8bit_binary__dist_trafo_a.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__dist_trafo_a/xy_8bit_binary__dist_trafo_a.tif).
    - Perform a distance transform.
    - Invert the binary input image.
    - Perform another distance transform on the new binary image.
    - Observe that the datatype (in particular 8-bit) of the distance transform image limits the distances.
    - Discuss different metrics.
    - Add a calibration to the inverted image and recompute the distance transform.
    - Observe whether the image calibration is considered for the distances.

  2. Distance measurements
    - Open label mask: [xy_8bit_labels__dist_trafo_b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__dist_trafo_b.tif).
    - Create an inverted binary mask for one of the labels (e.g. label 1)
    - Compute the distance transform
    - Measure intensity (= distances to nearest other objects) of objects in the distance map
    - Show that the measured values correspond to the distance of label 2 and 3 to label 1. 
  
  3. Region selection by distance gating
    - Open reference object image: [xy_8bit_binary__single_object.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__single_object.tif).
    - Invert the binary
    - Compute the distance transform
    - Perform an intensity gating on the distance map, e.g. by thresholding, to create a mask with all pixels of a certain distance, e.g. between 100-120, to the reference object.