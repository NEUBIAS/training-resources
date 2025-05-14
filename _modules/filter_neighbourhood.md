---
title:     Neighborhood filters
layout:    module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Binarization](../binarization)"

objectives:
  - Understand the basic principle of a neighborhood filter.
  - Apply basic neighborhood filters to an image.

motivation: >
  Images are quite often noisy or have other issues that make them hard to segment, e.g. by means of a simple intensity threshold. Neighborhood filters are often used to enhance the images in order to facilitate better performance of segmentation algorithms.

concept_map: >
  graph TB
    P(Pixel coordinate) -->NBH(Neighborhood pixels)
    SE(Structuring element) --> NBH
    NBH -->A(Mathematical formula)
    A -->NP(New pixel value)

figure: /figures/filter_neighbourhood.png

figure_legend: Image filtering with a pixel neighborhood. (a) Raw intensity image with pixel neighborhood (structuring element (SE), outer green box) and central pixel (inner orange box) on which the filtering operation will be performed. (b) Pixel values in the neighborhood. (c) X is the value that would be replaced after operation (indicated as op). Here, max, mean and variance operations are used. Note - One has to carefully look at the data type of the image as some operations can produce large/floating point values. (d) Different SEs (neighborhood in green and affected pixel in orange) top left - SE  completely inside image boundaries; top right - SE at image boundaries (padding needed); bottom left - SE with different shape; bottom right - Line SE.

multiactivities:
  - ["filter_neighbourhood/filter_mean.md", [["ImageJ GUI", "filter_neighbourhood/filter_mean_imagejgui.md"], ["skimage napari", "filter_neighbourhood/filter_mean_skimage_napari.py"]]]

assessment: >
  #### Fill in the blanks
    Fill in the blanks, using these words: decrease, increase, size, structuring element, large
    - A synonym for neighborhood is  ____
    - The filter radius characterize the filter ___
    - ___ filter size can cause a loss of details in the filtered image
    - Filter can be used to ____ the noise in an image
    - The usage of filters can ____ the quality of image segmentation/binarization

    > ## Solution
    > - A synonym for neighborhood is **structuring element (SE)**
    > - The filter radius characterize the filter **size**
    > - **large** filter size can cause a loss of details in the filtered image
    > - Filter can be used to **decrease** the noise in an image
    > - The usage of filters can **increase** the quality of image segmentation/binarization
    {: .solution}

learn_next:
- "[Morphological filters](../filter_morphological)"
- "[Median filter](../median_filter)"
external_links:

---

Neighborhood filters comprise two ingredients: a definition of the pixel neighborhood (size and shape) and a mathematical recipe what to compute on this neighborhood.
The result of this computation will be used to replace the value of the central pixel in the neighborhood. This procedure can be applied to several (all) pixels of an image to obtain a filtered image. The animation shows a square neighborhood (3x3) applied to the inner pixels of the image.

There are tons of different neighborhood filters, and you can also invent one!

<img src="../figures/filter_neighbourhood.gif"  align ="center" width="50%" >

#### The neighborhoods

The neighborhood of a pixel is also called a structuring element (SE) and can have various sizes and shapes.
Here, we use one of the simplest and most widely used neighborhoods, namely a circular neighborhood, which is defined by a certain radius. We will explore other shapes of SEs in more detail in a dedicated module.

#### Padding

Since the filtering operation takes into account all the directions of extent of SE, border pixels would be affected in a different way and one has to decide that which values they should assume. Padding is the operation of adding an additional layer around your data to get more accurate values after filtering process. It also gives you option to retain same dimensions for your data after filtering. Common padding methods are using zeros or to mirror/replicate the border pixel values.

#### The math

There are many ways how to cleverly compute on a pixel neighborhood. For example, one class of computations is called convolutional filters, another is called rank filters. Here, we focus on the relatively simple mean and variance filters.

#### Best practice

As usual, everything depends one the scientific question, but maybe one could say to use a filter that changes the image as little as possible.
