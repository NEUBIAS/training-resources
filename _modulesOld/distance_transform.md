---
title: Distance transform
layout: module
tags: ["draft"]
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Data types](../datatypes)"
objectives:
motivation: |
concept_map: >
  graph TD
    B("Input image") -->|distance transform| D("Distance map image")
    B -->|must contain| P("Pixels with value 0")
    D -->|contains| DN("Distances to nearest 0 pixel")

figure: /figures/distance_transform.png
figure_legend: Upper panel - Label mask image and the corresponding distance map. The distance map has three local maxima, which are very useful for object splitting and defining object centers. Lower panel - The label mask image has been binarized and inverted in order to compute the distances to the objects.

activity_preface: |
  - Distance transform basics
    - Open label mask [xy_8bit_labels__dist_trafo_a.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__dist_trafo_a.tif).
    - Perform a distance transform.
    - From label mask create binary image where the objects are `0` and the background is `1`.
    - Perform another distance transform on the new binary image.
    - Observe that the datatype of the distance transform image limits the distances.
    - Observe whether the image calibration is considered for the distances.
  - Distance measurements
    - Open label mask: [xy_8bit_labels__dist_trafo_b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__dist_trafo_b.tif).
    - Measure intensity (= distances to nearest other objects) of objects in the distance map of the binary image (s.a.)
  - Region selection
    - Open reference object image: [xy_8bit_binary__single_object.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__single_object.tif).
    - Compute a distance map.
    - Perform an intensity gating to create a mask with all pixels of a certain distance to the reference object.

activities:
  - ["ImageJ GUI MorpholibJ", "distance_transform/activities/distance_transform_imagejgui.md", "markdown"]
  - ["ImageJ Macro MorpholibJ", "distance_transform/activities/distance_transform_imagejmacro.ijm", "java"]
  - ["Python Napari", "distance_transform/activities/distance_transform_napari_skimage.py", "python"]

exercises:
  - ["ImageJ GUI", "binarization/exercises/binarization_imagejgui.md"]
  - ["ImageJ Macro", "binarization/exercises/binarization_imagejmacro.md"]

assessment: >

  ### Fill in the blanks

    - Pixels in a binary image can have maximally ___ different values.
    - If the threshold is larger than the maximal pixel value in the intensity image, all pixels in the binary image have a value of ___.
    
    > ## Solution
    >   - Pixels in a binary image can have maximally **2** different values.
    >   - If the threshold is larger than the maximal pixel value in the intensity image, 
    > all pixels in the binary image have a value of **0**.
    {: .solution}
    
  ### True or False
    - There is only one correct threshold value in order to convert an intensity image into a binary image. 
    - Binary images are always unsigned 8-bit where the foreground is 255.
    
    > ## Solution
    >   - There is only one correct threshold value in order to convert an intensity image into a binary image. **False**
    >   -  Binary images are always unsigned 8-bit where the foreground is 255. **False**
    {: .solution}

learn_next:
  - "[TODO](../auto_threshold)"
  - "[TODO](../connected_components)"

external_links:
  - "[Wikipedia: Dist](https://en.wikipedia.org/wiki/Binary_image)"
---
