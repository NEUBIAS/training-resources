---
title:     Neighbourhood filters
layout:    module
prerequisites:
  - "[Image pixels](image_pixels)"
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
figure_legend: The same input image filtered with neighborhood filters of different kinds (mean, median, edge) and shapes (circular with a radius of 1 pixel, top row; radius of 3 pixels, bottom row).

activity_preface: >
  Open image [xy_8bit__noisy_two_nuclei.tif]( https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__noisy_two_nuclei.tif) and explore the effect of a mean filter of different sizes.

activities:
- ["ImageJ Macro & GUI", "filter_neighbourhood/activities/mean_filter_imagejmacro.ijm", "java"]
# "KNIME": "filter_neighbourhood/activities/mean_filter_knime.md"
#  "ImageJ Macro":
#  "Jython":
#  "MATLAB":

exercises_preface: >

exercises:
#  "ImageJ GUI": 
#  "ImageJ Macro":
#  "Jython":
#  "MATLAB":

learn_next:
- "[Convolution filters](filter_convolution)"
- "[Rank filters](filter_rank)"

external_links:

---

### Neighbourhood filers

Neighborhood filters comprise two ingredients: a definition of the pixel neighbourhood (size and shape) and a mathematical recipe what to compute on this neighourhood. The result of this computation will be used to replace the value of the central pixel in the neighbourhood.

There are really tons of different neighborhood filters, and you can invent a new one!

#### The neighbourhoods 

The neighborhood of a pixel is also called a structuring element and can have various sizes and shapes.
Here, we use one of the simplest and most widely used neighbourhoods, namely a circular neighborhood, which is defined by a certain radius. We will explore other shapes of structuring elements in more detail in a dedicated module.

#### The math

There are really many many ways how to cleverly compute on a pixel neighborhood. For example, one class of computations is called convolutional filters, another is called rank filters. Here, we focus on the relatively simple mean filter, which is the mean filter.