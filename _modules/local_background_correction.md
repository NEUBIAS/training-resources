---
title:     Local background correction
layout:    module

prerequisites:
  - "[Median filter](median_filter)"
  - "[Image math](image_math)"

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
figure_legend: Local background correction using a median filter. Here, this approach creates artefacts at the borders of the large circular background region, the intensities of the two spots are however well preserved.

activity_preface: |
  - Open image [xy_8bit__spots_local_background_with_noise](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__spots_local_background_with_noise.tif)
  - Compute a background image using a median filter
  - Create a foreground image by subtracting the background image from the input image
  - Check how well the background corrrection worked and whether any artefacts were introduced

activities:
  - ["ImageJ Macro", "local_background_correction/activities/local_background_correction.ijm", "java"]

exercises:

assessment: |

  ### True or false (discuss with your neighbour)

    1. Mean filter is better than the median filter to generate background image.
    1. On the generated background image the objects of interest should not be visible.
    1. The size of the filter's structuring element for generating the background image should be much smaller than the size of the objects.
    
    > ## Solution
    > 1. False
    > 1. True
    > 1. False
    {: .solution}

learn_next:

external_links:

---

### Typical filters for creating background images

- Median filter
- Morphological opening filter
  - The result of background subtraction operation is called top-hat filter
