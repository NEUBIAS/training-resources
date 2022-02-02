---
title: Distance transform
layout: module
tags: []
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Data types](../datatypes)"
objectives:
motivation: |
concept_map: >
  graph TD
    B("Binary image") -->|distance transform| D("Distance map")
    B --> ("Image with values: 0 or 1")
    D --> ("Image with values: Distance to closest 0")

figure: /figures/binarization.png
figure_legend: Images before and after binarization

activity_preface: |
  ### Distance transform basics
    - Open the binary image [xy_8bit_binary__two_objects.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__two_objects.tif).
    - Perform a distance transform.
      - Discuss that there are various algorithms.
    - Observe that it matters what is foreground and what is background.
    - Observe that the datatype of the distance transform image limits the distances.
    - Observe whether the image calibration is considered for the distances.
  ### Distance measurements
    - Open reference object image: [xy_8bit_binary__single_object.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__single_object.tif).
    - Compute a distance map
    - Open objects image: [xy_8bit_labels__two_spots.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__two_spots.tif).
    - Measure intensity (= distance to reference object) of objects in distance map
  ### Region selection
    - Open reference object image: [xy_8bit_binary__single_object.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__single_object.tif).
    - Compute a distance map.
    - Perform an intensity gating to create a mask with all pixels of a certain distance to the reference object.

activities:
  - ["ImageJ GUI", "binarization/activities/binarization_imagejgui.md", "markdown"]
  - ["ImageJ Macro", "binarization/activities/binarization_imagejmacro.ijm", "java"]
  - ["ImageJ Jython", "binarization/activities/binarization_jython.py", "python"]
  - ["MATLAB", "binarization/activities/binarization_matlab.m", "matlab"]
  - ["KNIME", "binarization/activities/binarization_knime.md", "markdown"]
  - ["Python", "binarization/activities/binarization.py", "python"]

exercises:
  - ["ImageJ GUI", "binarization/exercises/binarization_imagejgui.md"]
  - ["ImageJ Macro", "binarization/exercises/binarization_imagejmacro.md"]
  - ["ImageJ Jython", "binarization/exercises/binarization_jython.md"]

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
  - "[Automatic threshold for binarization](../auto_threshold)"
  - "[Finding objects in a binary image](../connected_components)"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"
  
---
#### Image thresholding
A common algorithm for binarization is thresholding. A threshold value `t` is chosen, either manually or automatically, 
and all pixels with intensities below `t` are set to 0, whereas pixels with intensities `>= t` are set to the value for the foreground. 
Depending on the software the foreground value can be different (e.g. 1 in MATLAB or 255 in ImageJ). At any pixel (x,y):

`p_im(x,y) < t` -> `p_bin(x,y) = 0`

`p_im(x,y) >= t` -> `p_bin(x,y) = 1`

where, p_im and p_bin are the intensity and binary images respectively.

It is also possible to define an interval of threshold values, i.e. a lower and upper threshold value. Pixels with intensity values 
within this interval belong to the foreground and vice versa. 
 

