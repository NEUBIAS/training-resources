---
title: Local background correction
layout: module

prerequisites:
  - "[Median filter](../median_filter)"
  - "[Statisical (rank) filters](../filter_statistical)"
  - "[Projections](../projections)"

objectives:
  - Understand how to use image filters for creating a local background image
  - Use the generated local background image to compute a foreground image

motivation: >
  Very often, biological images contain locally varying background intensities. This hampers both segmentation and intensity quantification. However, often it is possible to generate a background image that can be subtracted in order to yield a foreground image with zero background. It is very important to know about this, because removing spatially varying background is a prevalent task in bioimage analysis.

concept_map: >
  graph TD
    ii(Input image)
    ii --> bgi[Background image]
    bgi --> s[Subtract]
    ii --> s
    s --> fgi[Foreground image]

figure: /figures/local_background_correction.png
figure_legend: Local background correction using a median filter. Left - Raw data. Middle - Median filtered image (background). Right - Difference image (foreground).

multiactivities:
  - ["local_background_correction/local_background_correction_act1.md", [["ImageJ GUI", "local_background_correction/local_background_correction_act1_imagejgui.md", "markdown"], ["ImageJ Macro", "local_background_correction/local_background_correction_act1_imagejmacro.ijm", "java"], ["skimage napari", "local_background_correction/local_background_correction_act1_skimage_napari.py", "python"]]]
  - ["local_background_correction/local_background_correction_act2.md", [["ImageJ GUI", "local_background_correction/local_background_correction_act2_imagejgui.md", "markdown"], ["ImageJ Macro", "local_background_correction/local_background_correction_act2_imagejmacro.ijm", "java"], ["ImageJ Jython", "local_background_correction/local_background_correction_act2_jython.py", "python"], ["skimage napari", "local_background_correction/local_background_correction_act2_skimage_napari.py", "python"]]]

assessment: >

  ### True or false?

    1. Mean filter is better than the median filter to generate a background image.
    1. On the generated background image the objects of interest should not be visible.
    1. When creating a background image by means of filtering: The size of the filter's structuring element should be much smaller than the size of the objects.

    > ## Solution
    > 1. False (mean filter is really quite poor in terms of removing foreground information)
    > 1. True (because this is the background image, so it should not contain any foreground information)
    > 1. False (it should be much (maybe ~3 times) larger in order to remove the objects from the image)
    {: .solution}

learn_next:
  - "[Morphological filters](../filter_morphological)"
  
external_links:
---

There exist multiple methods on how to compute a background image. 
Which methods and parameters work best depends on the specific input image and the size of the object of interest. 


Common methods are:

* **Median filtering**
* **Morphological opening**. Subtraction of the opened image from the original image is also called **Top-Hat** filtering. 
* **Rolling ball**, this alogorithm is implemented for instance in ImageJ `Background Subtraction` or [`skimage.restoration.rolling_ball`](https://scikit-image.org/docs/stable/api/skimage.restoration.html#skimage.restoration.rolling_ball)

Some of the methods may be sensistive to noise. Therefore, it can be convenient to smooth the image, e.g. with a mean or gaussian filtering,  prior computing the background image.  
