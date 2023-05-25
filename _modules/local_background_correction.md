---
title: Local background correction
layout: module

prerequisites:
  - "[Median filter](../median_filter)"
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
- ["local_background_correction/local_background_correction_activity1.md", [["Activity 1 ImageJ GUI", "local_background_correction/local_background_correction_imagejgui.md", "markdown"], ["Activity 1 ImageJ Macro", "local_background_correction/local_background_correction_imagejmacro.ijm", "java"], ["Activity 1 skimage napari", "local_background_correction/local_background_correction_activity1_skimage_napari.py", "python"]]]					
- ["local_background_correction/local_background_correction_activity2.md", [["Activity 2 ImageJ GUI", "local_background_correction/local_background_correction_activity2_gui.md", "markdown"], ["Activity 2 ImageJ Macro", "local_background_correction/local_background_correction_activity2_macro.ijm", "java"], ["Activity 2 ImageJ Jython", "local_background_correction/local_background_correction_activity2_jython.py", "python"], ["Activity 2 skimage napari", "local_background_correction/local_background_correction_activity2_skimage_napari.py", "python"]]]

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

external_links:
---
