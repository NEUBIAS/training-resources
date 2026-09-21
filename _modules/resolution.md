---
title: Resolution
layout: module
tags: ["image formation"]
prerequisites:
  - "[Point spread function](../psf)"
objectives:
  - "Understand how resolution is affected by the size of the PSF"
  - "Understand how physical parameters of the microscope affect the resolution"
motivation: |
  A microscope does not deliver a perfect picture of the biological structure. Due to the law of diffraction, we observe a blurred version of it. If part of the structure is too close we will not be able resolve its detail. The so called resolution limit is a distance below which the microscope can't resolve adjacent structures. The final effective resolution depends on a combination of the width of the PSF, signal to background, signal to noise, and sample preparation. 

concept_map: >
  graph TD
    T1("TODO1") --> T2("TODO2")
    T2 --> T3("TODO3")

figure: /figures/resolution.png
figure_legend: TODO

multiactivities:
  - ["resolution/act01.md", [["ImageJ GUI", "resolution/act01_imagejgui.md"], ["skimage napari", "resolution/act01_skimage_napari.py"]]]

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

