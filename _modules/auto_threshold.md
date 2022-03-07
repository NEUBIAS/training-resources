---
title: Automatic thresholding
layout: module
tags: ["draft","component"]
prerequisites:
  - "[Thresholding](../binarization)"
objectives:
  - "Understand how an image histogram can be used to derive a threshold"
  - "Apply automatic threshold to distinguish foreground and background pixels"
 
motivation: |
  The manual determination of a threshold value is tedious and subjective.
  This is problematic as it reduces the reproducibility of the results and may preclude determining threshold values for many different images. It is therefore important to know about reproducible mathematical approaches to automatically determine threshold values for image segmentation.
  
concept_map: >
  graph TD
    I("Image") --> H("Histogram")
    H --> T("Threshold value")

figure: /figures/auto_threshold.png
figure_legend: Input images, histograms (Otsu threshold - orange, Huang threshold - blue), binary images (Otsu), binary images (Huang).

activity_preface: >

activities:

exercises:

assessment: >

learn_next:

external_links:

---

 
