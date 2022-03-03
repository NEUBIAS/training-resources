---
title:     Local background correction
layout:    module

prerequisites:
  - "[Median filter](median_filter)"
  - "[Image math](image_math)"
  - "[Projections](../projections)"

objectives:
  - Understand how to use image filters for creating a local background image
  - Use the generated local background image to compute a foreground image

motivation: >
  Very often, biological images contain locally varying background intensities. This hampers both segmentation and intensity quantification. However, given a sufficient separation of length scales in terms of variation in background intensities vs. variation in intensities in the foreground, image filters can be employed to measure and correct for the background.

concept_map: >
  graph LR
    i(Input image) --> bgf(Large size filter)
    bgf --> bgi[Background image]
    bgi --> s[Subtract]
    i --> s
    s --> fgi[Foreground image]

figure: /figures/local_background_correction.png
figure_legend: Local background correction using a median filter. Left - Raw data. Middle - Median filtered image (background). Right - Difference image (foreground).

activity_preface: |
  - Activity 1: background subtraction using a median filter.
    - Open image [xy_8bit__some_spots_with_uneven_bg](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__some_spots_with_uneven_bg.tif)
    - Compute a background image using a median filter
    - Create a foreground image by subtracting the background image from the input image
    - Check how well the background correction worked and whether any artefacts were introduced
    - Optional: discuss how one could automatically segment the two spots in the resulting foreground image (mean filter and object size filter)

  - Activity 2: background subtraction using a maximum intensity projection.
    - Open image [xyt_8bit_polyp](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyt_8bit_polyp.tif)
    - Make a maximum intensity projection of this image. This will essentially create a background image, without the moving polyp.
    - Use the image calculator to subtract the maximum intensity projection from the original image.

activities:
  - ["Activity 1 ImageJ GUI & Macro", "local_background_correction/activities/local_background_correction.ijm", "java"]
  - ["Activity 2 GUI", "local_background_correction/activities/local_background_correction_activity2_gui.md", "markdown"]
  - ["Activity 2 Macro", "local_background_correction/activities/local_background_correction_activity2_macro.ijm", "java"]
  - ["Activity 2 Jython", "local_background_correction/activities/local_background_correction_activity2_jython.py", "python"]

exercises:
  - ["ImageJ GUI & Macro", "local_background_correction/exercises/local_background_correction_imagejmacro.md"]

assessment: |

  ### True or false (discuss with your neighbour)

    1. Mean filter is better than the median filter to generate background image.
    1. On the generated background image the objects of interest should not be visible.
    1. The size of the filter's structuring element for generating the background image should be much smaller than the size of the objects.

    > ## Solution
    > 1. False (mean filter is really quite poor in terms of removing foreground information)
    > 1. True (because this is the background image, so it should not contain any foreground information)
    > 1. False (it should be much (maybe ~3 times) larger)
    {: .solution}

learn_next:

external_links:

---

### Common filters for creating background images

- Median filter
- "Rolling ball" background
  - ImageJ's "Subtract Background"
    - Missing: explanation how it works, exactly
- Morphological opening filter
  - The result of background subtraction using a grayscale opening is called top-hat filter

#### Advanced and powerful filters for creating background images

- Morphological opening using reconstruction
  - How do the work?
  - MATLAB has this option... `imreconstruct`
  - ImageJ MorpholibJ has a Grayscale Attribute Filtering, which seems similar (the same)?
