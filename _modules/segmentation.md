---
title: Segmentation
layout:  module
tags: []
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Data types (unsigned 8-bit)](../datatypes)"
objectives:
motivation: |
concept_map: >
  graph TD
    I("Image") --> IS("Image segments (Regions)")
    IS --> O("Instance segmentation (Objects)")
    IS --> S("Semantic segmentation (Pixel classes)"
    O --> L("Label mask image")
    S --> L

figure: /figures/binarization.png
figure_legend: Images before and after binarization

activity_preface: |

activities:

exercises:

assessment: >

learn_next:

external_links:
  - "[Wikipedia: Segmentation](https://en.wikipedia.org/wiki/Image_segmentation#Groups_of_image_segmentation)"
---
