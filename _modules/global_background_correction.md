---
title:     Global background correction
layout:    module

prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Data types](../datatypes)"
  - "[Image math](../image_math)"

objectives:
  - Measure the background in an image
  - Apply image math to subtract a background intensity value from all pixels and understand that the output image should have a floating point data type

motivation: >
  Most biological images have non-zero intensity values in regions outside of the objects of interest. In order to properly quantify the intensities of objects such background must be taken into account.
  For example, most cameras on microscopes have a read noise with can be many hundred gray values (for 12-bit or 16-bit detection). As such read noise is typically constant across the whole image, subtracting a constant background value for each pixel is possible.

concept_map: >
  graph TD
    I("Image") --> SB("Subtract background")
    SB --> BCI("Background corrected image")
    BCI ---|"datatype"| FP("Floating point")
    I --> MB("Measure background")
    MB --> SB

figure: /figures/global_background_correction.png
figure_legend: Image before and after background correction

activity_preface: |
  - Open image [xy_16bit__nuclei_high_dynamic_range_with_offset](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__nuclei_high_dynamic_range_with_offset.tif)
  - Measure the background using a manually defined region
  - Measure the mean intensities inside of two nuclei using manually defined regions
    - Choose rather dim nuclei of different intensities
    - Measure the intensity ratio with and without background correction
  - Subtract the background value from the image
    - Appreciate that this yields a non-zero background for unsigned integer data types and that a floating point data type is thus necessary
  - Open image [xy_16bit__scanR_datatype_issue](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif)
    - Discuss automated global background estimation methods, e.g.
      - mode
      - mean intensity outside objects

activities:
    - ["ImageJ Macro & GUI", "global_background_correction/activities/global_background_correction.ijm", "java"]

exercise_preface: |
- Open the intensity image 
[xy_16bit__nuclei_with_background.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__nuclei_with_background.tif)
  1. Measure the background.
  2. Subtract the background from the image.
  3. Is the mean intensity in the background region close to 0 (<<1)? If not, which image data type conversion have you forgotten?
  4. Verify that the histogram has not been clipped by the background subtraction operation.
  5. Conceive (and implement) a way of automatically computing a global background.

exercises:
    - ["ImageJ Macro & GUI", "global_background_correction/exercises/global_background_correction.md"]

assessment: |
    ### True or false? 
      1. The datatype is irrelevant for background subtraction.
      2. Background subtraction using a unsigned integer image will always lead to a positive valued background.
      3. Global background subtraction is important for ratiometric computations.
      4. Global background subtraction affects differences in intensities.
        
    > ## Solution
    >  1. The datatype is irrelevant for background subtraction. **FALSE**
    >  2. Background subtraction using a unsigned integer image will always lead to a positive valued background. **TRUE**
    >  3. Global background subtraction is important for ratiometric computations. **TRUE**
    >  4. Global background subtraction affects differences in intensities. **FALSE**       
    {: .solution}

learn_next:
    "[Local background subtraction](../local_background_subtraction)"

external_links:
---
