---
title: Flat-field correction
layout: module
tags: ["draft"]
prerequisites:
  - "[Illumination and shading artefacts](../illumination_artefact)"
  - "[Convolutional filters](../filter_convolution)"
  - "[Object intensity measurements](../measure_intensities)"
objectives:
  - Formulate the mathematical relationship between the raw image adn the corrected image
  - Evaluate methods to obtain a flat-field reference (calibration slide or retroscpective computation)
  - Perform a flat-field correction and evaluate the results
motivation: |
  In quantitative fluorescence microscopy, we assume that the pixel intensity is proportional to the concentration of the fluorophore. However, uneven illumination (vignetting) and optical obstructions (dust) violate this assumption. Without correction we may have (1) **Intensity bias**, where cells may appear brighter in the middle than on the edge, (2) *Segmentation errors* segmentation algorithms may fail in certain part of an image. Therefore it is important to learn methods on how to mitigate illumination artefatcs. 

concept_map: >
  graph TD
    FFC("Flat-field Correction") --- Components("Input Frames")
    FFC --- Process("Mathematical Operations")
    
    Components --- Raw("Raw Image (I)")
    Components --- Dark("Dark Frame (D)")
    Components --- Flat("Flat-field (F)")
    
    Flat --- Ref("Standard Slide / Dye")
    Flat --- Retros("Retrospective (Median/Mean)")
    
    Process --- Subtraction("Background Subtraction (I - D)")
    Subtraction --- Normalization("Normalization (F_norm)")
    Normalization --- Division("Division (Final Result)")
    
    Division --- Result("Corrected Signal (S)")

figure: /figures/flatfield_correction.png
figure_legend: TODO

multiactivities:
  - ["flatfield_correction/act01.md", [["ImageJ GUI", "flatfield_correction/act01_imagejgui.md"], ["skimage napari", "flatfield_correction/act01_skimage_napari.py"]]]

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .
    
    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:
  - "[TODO](../auto_threshold)"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"
---

