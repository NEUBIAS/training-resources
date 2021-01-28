---
title:     Global background correction
layout:    module

prerequisites:
  - "[Basic properties of images and pixels](pixels)"
  - "[Pixel data types](pixel_data_types)"
  - "[Image math](image_math)"

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

figure: figures/global_background_correction.png
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

exercises_preface:

exercises:

learn_next:

external_links:
---