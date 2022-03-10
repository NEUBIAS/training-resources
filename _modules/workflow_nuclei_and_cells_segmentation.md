---
title: Nuclei and cells segmentation
layout: module
tags: ["draft","workflow"]
prerequisites:
  - "[Watershed transform](../watershed)"
objectives:
  - "Segment cells and nuclei, using nuclei as seeds for watershed segmentation of the cells."
motivation: |
  It is quite common to have fluorescence microscopy images with stainings for both the nuclei and cytoplasm. While nuclei are typically separate and thus easy to segment, the cells are often touching each other, which makes their segmentation much more challening. The workflow presented in this module is a common approach to tackle this challenge and thus very useful to know.

concept_map: >
  graph TD
    N("Nuclei") --> NM("Nuclei mask")
    C("Cells") --> W("Watershed transform")
    NM -->|seeds| W
    W --> S("Cells label mask")

figure: /figures/template.png
figure_legend: TODO

activity_preface: |
  - Open the image [xy_8bit_binary__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei.tif).
  - TODO

activities:

exercises:

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .
    
    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:

external_links:
---

