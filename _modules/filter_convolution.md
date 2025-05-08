---
title: Convolutional filters
layout: module
prerequisites:
  - "[Neighbourhood filtering](../filter_neighbourhood)"
objectives:
  - Understand the basic principle of a convolutional filter.
  - Apply convolutional filters to an image.
motivation: |
  Convolutional filters are very important, because
  - the widely used Gaussian blur smoothing often is implemented as a convolutional filter.
  - the widedly used Laplacian of Gaussian (Log) or Difference of Gaussian (DoG) spot detection filters often are implemented as a convolutional filters.
  - famous edge detection filters (Sobel) are convolutional filters.
  - the widely used convolutional neural networks (CNN) are mainly a sequence of convolutional filters.


concept_map: >
  graph TD
    SM("Small matrix of numbers\n(Kernel)") --> LM("Local, sliding multiplication")
    I("Image") --> LM
    LM --> FI("Filtered image")
    
figure: /figures/filter_convolution.png
figure_legend: Convolutional filtering example, using a 3x3 vertical edge detection filter.

multiactivities:
  - ["filter_convolution/gaussian.md", [["ImageJ GUI", "filter_convolution/gaussian_imagejgui.md"], ["skimage napari", "filter_convolution/gaussian_skimage_napari.py"]]]
  - ["filter_convolution/laplacian.md", [["ImageJ GUI", "filter_convolution/laplacian_imagejgui.md"], ["skimage napari", "filter_convolution/laplacian_skimage_napari.py"]]]
  - ["filter_convolution/log.md", [["ImageJ GUI", "filter_convolution/log_imagejgui.md"], ["skimage napari", "filter_convolution/log_skimage_napari.py"]]]

assessment: >

  ### Fill in the blanks

    1. What are the entries of a convolutional kernel that computed a sum?
    1. The entries of a convolutional kernel repesenting a gaussian blur are \_\_\_ in the centre of the kernel.
    1. The entries of a convolutional kernel implementing an edge detection typically also contains \_\_\_ numbers such that the numbers sum up to \_\_\_.
    
    > ## Solution
    >   1. The entries are all **1**. 
    >   1. The entries are **larger** in the centre.
    >   1. There are **negative** numbers and they sum up to **zero**, such that the result of the convolution in image regions without edges is zero.
    {: .solution}

learn_next:
  - "[Statistical neighborhood filters](../filter_rank)"

external_links:
  - "[Wikipedia: Image processing kernels](https://en.wikipedia.org/wiki/Kernel_(image_processing))"
  - "[Laplacian filter](https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm)"
---

