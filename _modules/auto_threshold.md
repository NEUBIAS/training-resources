---
title: Automatic threshold
layout: module
tags: ["draft","component"]
prerequisites:
  - "[Thresholding](../binarization)"
objectives:
  - "Understand how an image histogram can be used to derive a threshold"
  - "Apply automatic threshold to distinguish foreground and background pixels"
 
motivation: |
  The manual fixing of a threshold value is user dependent and may require adjustments for every images.
  This is problematic as it reduces the reproducibility of the results and precludes from applying the binarization to many different images. It is therefore important to have a mathematical approach to automatically find a threshold values for segmentation.
  
concept_map: >
  graph TD
    I("Image") --> H("Histogram")
    H --> T("Threshold value")

figure: /figures/auto_threshold.png
figure_legend: Input images, histograms, binary images (Otsu threshold), binary images (Huang threshold)

activity_preface: >

activities:

exercises:

assessment: >

learn_next:

external_links:

---

 
