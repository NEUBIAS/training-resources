---
title: Convolutional filters
layout: module
prerequisites:
  - "[Neighborhood filters](../filter_neighbourhood)"
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
  - ["filter_convolution/laplacian.md", [["ImageJ Macro", "filter_convolution/laplacian_imagejmacro.ijm"], ["skimage napari", "filter_convolution/laplacian_skimage_napari.py"]]]
  - ["filter_convolution/gaussian.md", [["ImageJ Macro", "filter_convolution/gaussian_imagejmacro.ijm"], ["skimage napari", "filter_convolution/gaussian_skimage_napari.py"]]]
  - ["filter_convolution/log.md", [["ImageJ Macro", "filter_convolution/log_imagejmacro.ijm"], ["skimage napari", "filter_convolution/log_skimage_napari.py"]]]

assessment: >

  ### Fill in the blanks

    1. What are the entries of a convolutional kernel that computes a local sum?
    1. You want to enhance horizontal filamentous structures in an image, how would a convolutional kernel for this look like?
    1. The entries of a convolutional kernel implementing an edge detection typically sum up to \_\_\_.
    
    > ## Solution
    >   1. The entries are all **1**. 
    >   1. A simple kernel to enhance horizontal lines could be: [[-1,-1,-1],[2,2,2],[-1,-1,-1]]
    >   1. The entries sum up to **zero**, such that the result of the convolution in image regions without edges is zero.
    {: .solution}

learn_next:
  - "[Statistical neighborhood filters](../filter_rank)"

external_links:
  - "[Wikipedia: Image processing kernels](https://en.wikipedia.org/wiki/Kernel_(image_processing))"
  - "[Laplacian filter](https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm)"
  - "[What is a convolution? (Video)](https://www.youtube.com/watch?v=KuXjwB4LzSA)"
---

