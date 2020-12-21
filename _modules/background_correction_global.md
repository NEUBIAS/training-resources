---
title:     Background subtraction - global
layout:    module
prerequisites:
  - "[Basic properties of images and pixels](pixels)"
  - "[Pixel data types](pixel_data_types)"
  - "Image math (no module yet)"
objectives:
  - Apply image math to subtract a background intensity value from all pixels.
  - Understand that one may need to convert to a floating point data type to accurately conduct image background subtraction.
motivation: >
  Most biological images have non-zero intensity values in regions outside of the objects of interest. In order to properly quantify the intensities of objects such background must be subtracted.
  For example, most cameras on microscopes have a read noise with can be many hundred gray values (for 12bit or 16bit detection). As such read noise is typically constant across the whole image, subtracting a constant background value from each pixel is possible.
concept_map: >
  graph TD
    I("Image") --> SB("Subtract background")
    SB --> BCI("Background corrected image")
    BCI -->|"should be"| FP("Floating point")
    I --> MB("Measure background")
    MB --> SB

figure: 
figure_legend: 

activity_preface: |
  - Perform background subtraction on an image.
  - Observe that one obtains negative values.
  - Discuss automated global background estimation methods (e.g., mode, outside objects)

activities:

exercises_preface:

exercises:

learn_next:

external_links:
---
