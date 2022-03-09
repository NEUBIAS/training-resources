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

activity_preface: |
  - Manual vs. auto thresholding
    - Open [xy_8bit__nuclei_without_offset.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_without_offset.tif) and [xy_8bit__nuclei_with_offset.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_with_offset.tif)
    - Explore the differences in doing manual and auto thresholding.


activities:
- ["ImageJ GUI", "auto_threshold/activities/auto_threshold_imagejgui.md", "markdown"]

exercises:

assessment: >

learn_next:

external_links:
- Some common automatic thresholding methods can be studied [here](https://imagej.net/plugins/auto-threshold)

---

### Key points
- Most auto thresholding methods do two class clustering.
- If the histogram is bimodal, most automated methods will perform well
- If the histogram has more than two peaks i.e., automated methods would produce random results.
