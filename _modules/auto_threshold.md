---
title: Automatic thresholding (histogram-based)
layout: module
prerequisites:
  - "[Thresholding](../binarization)"
objectives:
  - "Understand how an image histogram can be used to derive a threshold"
  - "Apply automatic threshold to distinguish foreground and background pixels"

motivation: |
  The manual determination of a threshold value is tedious and subjective.
  This is problematic as it reduces the reproducibility of the results and may preclude determining threshold values for many different images as the dataset becomes large. It is therefore important to know about reproducible mathematical approaches to automatically determine threshold values for image segmentation.

concept_map: >
  graph TD
    I("Image") --> H("Histogram")
    H -- algorithm --> T("Threshold value")

figure: /figures/auto_threshold.png
figure_legend: Input images, histograms (Huang threshold - blue, Otsu threshold - orange),  binary images (Huang), binary images (Otsu).

activity_preface: |
  - Manual vs. auto thresholding
    - Open [xy_8bit__nuclei_without_offset.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_without_offset.tif) and [xy_8bit__nuclei_with_offset.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_with_offset.tif)
    - Explore the differences in doing manual and auto thresholding


activities:
- ["ImageJ GUI", "auto_threshold/activities/auto_threshold_imagejgui.md", "markdown"]

exercise_preface: |
  - Auto thresholding on image stack
    - Open [xyz_8bit__nuclei_autothresh.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__nuclei_autothresh.tif)
    - Select any threshold method and observe the differences in segmentation when you use the histogram computed from all images in 3D stack      

exercises:
- ["ImageJ GUI", "auto_threshold/exercises/auto_threshold_imagejgui.md", "markdown"]

assessment: >

  ### True or False
    - Using stack histogram yields only one threshold value for binarization when applying auto thresholding
    - Auto thresholding gives better segmentation results than manual thresholding in the presence of noise

    > ## Solution
    >   - **True**
    >   - **False**
    {: .solution}

learn_next:

external_links:
- Some common automatic thresholding methods can be studied here [Imagej.net Auto-threshold](https://imagej.net/plugins/auto-threshold)

---

### Key points
- Most auto thresholding methods do two class clustering
- If the histogram is bimodal, most automated methods will perform well
- If the histogram has more than two peaks, automated methods could produce noisy results
