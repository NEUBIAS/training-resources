---
title: Projections
layout: module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
objectives:
  - "Project multi-dimensional image data into lower dimensions."
  - "Understand the differences between projection modes such as max, sum, and mean.
motivation: |
  Viewing image data that has more than two dimensions is difficult, because computer monitors are 2-D. Thus, it often is very useful to project the data into a 2-D representation. Of course, doing such a projection will loose information. Thus, performinig projections without compromising the scientific integrity of the data is not easy and should be only done with a sufficient understanding of the various methods.
concept_map: >
  graph LR
    ND("N dimensional image data") --> PM(Projection method)
    PM --> LD("N-1 dimensional image data")

figure: /figures/projection.png
figure_legend: 

activity_preface: |
  - Open [xyz_16bit__spots.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif)
  - Project along the z axis
  - Compare maximum and sum projection
  - Project along the x axis

activities:
  - ["ImageJ GUI", "projections/activities/projections_imagejgui.md", "markdown"]

exercises:
  - ["ImageJ GUI", "projections/exercises/projections_imagejgui.md"]

assessment: >

  ### Fill in the blanks

    - The pixels values in a sum projection will almost always be ___ than the original values.
    - 
    
    > ## Solution
    >   - The pixels values in a sum projection will alomst always be **larger** than the original values.
    >   - If the threshold is larger than the maximal pixel value in the intensity image, 
    > all pixels in the binary image have a value of **0**.
    {: .solution}
    
  ### True or False
    1. Image projections are always along the z-axis.
    1. The data type of the projected image must be the same as the data type of the original image.
    
    > ## Solution
    >   1.There is only one correct threshold value in order to convert an intensity image into a binary image. **False*
    >   1. The data type of the projected image must be the same as the data type of the original image. **False** In sum projections the pixel values are larger than in the original data and a different data type might be need to represent them. For maximum projections however the data type should not be changed. For mean projections it depends on which accuracy (decimal places) your science requires (e.g., decimal places need a floating point data type).
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
 

