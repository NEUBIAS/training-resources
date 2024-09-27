---
title: Similarity transformations 
layout: module
tags: ["draft"]
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[Spatial calibration](../spatial_calibration)"
objectives:
  - Understand how similarity transformations alter an image
  - Understand that similarity transforms may create new pixels, which must be created using a carefully chosen interpolation mode
  - Similarity transform an image
motivation: |
  TODO

concept_map: >
  graph TD
    I("Image") --> ST("Similarity transform:\ntranslate, scale, rotate, mirror")
    ST --> TI("Transformed image")
    TI <-->|angles,proportions| I

figure: /figures/similarity_transforms.png
figure_legend: TODO

multiactivities:
  - ["similarity_transforms/scale.md", [["ImageJ GUI", "similarity_transforms/scale_imagejgui.md"], ["PowerPoint", "similarity_transforms/scale_powerpoint.md"]]]

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .
    
    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:
  - "[Automatic threshold for binarization](../auto_threshold)"

external_links:
  - "[Wikipedia: Similarity transformation](https://en.wikipedia.org/wiki/Similarity_(geometry))"
---

