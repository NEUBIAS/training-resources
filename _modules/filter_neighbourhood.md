---
title:     Neighbourhood filters (introduction)
layout:    module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Binarization](../binarization)"

objectives:
  - Understand the basic principle of a neighbourhood filter.
  - Apply a mean filter to an image.

motivation: >
  Images are quite often noisy or have other issues that make them hard to segment, e.g. by means of a simple intensity threshold. Neighbourhood filters are a very important (maybe the most important) means to enhanced images in a sense of making them more amendable for segmentation. 

concept_map: >
  graph TB
    P(Pixel coordinate) -->NBH(Neighbourhood pixels)
    SE(Structuring element) --> NBH
    NBH -->A(Mathematical formula)
    A -->NP(New pixel value) 

figure: /figures/filter_neighbourhood.png
figure_legend: Image with a pixel neighourhood. Same image filtered with neighborhood filters of different kinds (mean, median, vertical edge) and structuring elements (circular with a radius of 1 pixel, top row; radius of 3 pixels, bottom row).

activity_preface: |
  - Open image [xy_8bit__noisy_two_nuclei.tif]( https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__noisy_two_nuclei.tif)
  - Explore the effect of a mean filter of different sizes.
  - Find the minimal size of a mean filter that enables binarization of the image into two forground objects (i.e. the nuclei).
  
  
activities:
- ["ImageJ Macro & GUI", "filter_neighbourhood/activities/filter_mean_imagejmacro.ijm", "java"]
# "KNIME": "filter_neighbourhood/activities/mean_filter_knime.md"
#  "ImageJ Macro":
#  "Jython":
#  "MATLAB":

exercises:
  - ["ImageJ Macro & GUI", "filter_neighbourhood/exercises/filter_mean_imagejmacro.md"]

assessment: >
  #### Fill in the blanks
    Fill in the blanks, using these words: decrease, increase, size, structuring element, large
    - A synonym for neighbourhood is  ____
    - The filter radius characterize the filter ___
    - ___ filter size can cause a loss of details in the filtered image
    - Filter can be used to ____ the noise in an image
    - The usage of filters can ____ the quality of image segmentation/binarization
    
    > ## Solution
    > - A synonym for neighbourhood is **structuring element**
    > - The filter radius characterize the filter **size**
    > - **large** filter size can cause a loss of details in the filtered image
    > - Filter can be used to **decrease** the noise in an image
    > - The usage of filters can **increase** the quality of image segmentation/binarization
    {: .solution}
learn_next:
- "[Convolution filters](../filter_convolution)"
- "[Rank filters](../filter_rank)"
- "[Median filter](../median_filter)"
external_links:

---

### Neighbourhood filters

Neighborhood filters comprise two ingredients: a definition of the pixel neighbourhood (size and shape) and a mathematical recipe what to compute on this neighbourhood. 
The result of this computation will be used to replace the value of the central pixel in the neighbourhood. This procedure can be applied to several (all) pixels of an image 
to obtain a filtered image. The animation shows a square neighbourhoods (3x3) applied to the inner pixels of the image. 

There are really tons of different neighborhood filters, and you can invent a new one!

<img src="../figures/filter_neighbourhood.gif"  align ="center" width="50%" >

#### The neighbourhoods 

The neighborhood of a pixel is also called a structuring element and can have various sizes and shapes.
Here, we use one of the simplest and most widely used neighbourhoods, namely a circular neighborhood, which is defined by a certain radius. We will explore other shapes of structuring elements in more detail in a dedicated module.

#### The math

There are really many many ways how to cleverly compute on a pixel neighborhood. For example, one class of computations is called convolutional filters, another is called rank filters. Here, we focus on the relatively simple mean filter, which is the mean filter.

#### Best practice

As usual, everything depends one the scientific question, but maybe one could say to use a filter that changes the image as little as possible.


