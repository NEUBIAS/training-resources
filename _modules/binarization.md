---
title:     Image binarization
layout:    module
prerequisites:
  - "[Basic properties of images and pixels](pixels)"
objectives:
  - "Describe the relationship between an intensity image and a derived binary image"
  - "Apply a threshold to distinguish foreground and background pixels"
motivation: >
  Very often, one wants to detect objects or specific regions in images. Typically, the first step to achieve this aim is to distinguish so-called background pixels, which do not contain objects or interesting regions, from foreground pixels, which mark the areas of interest. The foreground regions can than be further processed, e.g to detect objects or perform measurements.
concept_map: >
  graph TD
    PV("Pixel values") --> BA(Binarization algorithm)
    BA --> BPV("Binarized pixel values")
    BPV --> BG("Background (0)")
    BPV --> FG("Foreground (1)")

figure: /figures/binarization.png
figure_legend: Image before and after binarization by applying a threshold.

activity_preface: >
  Open an image and binarize it by applying a threshold.

activities:
  "ImageJ GUI": "binarization/activities/binarization_imagejgui.md"
  "ImageJ Macro": "binarization/activities/binarization_imagejmacro.md"
  "Jython": "binarization/activities/binarization_jython.md"
  "MATLAB": "binarization/activities/binarization_matlab.md"
  "KNIME": "binarization/activities/binarization_knime.md"

exercises_preface: >

  ### Fill in the blanks

    - Pixels in a binary image can have maximally ___ different values.
    - If the threshold is larger than the maximal pixel value in the intensity image, all pixels in the binary image have a value of ___.

exercises:
  "ImageJ GUI": "binarization/exercises/binarization_imagejgui.md"
  "ImageJ Macro": "binarization/exercises/binarization_imagejmacro.md"
  "Jython": "binarization/exercises/binarization_jython.md"
  "MATLAB": "binarization/exercises/binarization_matlab.md"

learn_next:
  - "[Algorithms to automatically determine a threshold value](auto_threshold)"
  - "[Finding objects in a binary image](connected_components)"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"
---
