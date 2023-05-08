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

multiactivities:
  - ["auto_threshold/auto_threshold_act1.md", [["ImageJ GUI", "auto_threshold/auto_threshold_act1_imagejgui.md", "markdown"], ["skimage napari", "auto_threshold/auto_threshold_act1_skimage_napari.py", "python"]]]
  - ["auto_threshold/auto_threshold_act2.md", [["ImageJ GUI", "auto_threshold/auto_threshold_act2_imagejgui.md", "markdown"], ["skimage napari", "auto_threshold/auto_threshold_act2_skimage_napari.py", "python"]]]

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
- Advanced material can be found in [Introduction to Bioimage Analysis by Pete Bankhead](https://bioimagebook.github.io/chapters/2-processing/3-thresholding/thresholding.html)

---

### Key points
- Most auto thresholding methods do two class clustering
- If the histogram is bimodal, most automated methods will perform well
- If the histogram has more than two peaks, automated methods could produce noisy results
