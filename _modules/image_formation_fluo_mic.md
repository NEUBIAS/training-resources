---
title: Fluorescence microscopy image formation
layout: module
tags: ["image formation"]
prerequisites:
  - "[Digital image](../pixels.md)"
objectives:
  - Understand how the intensities in a digital image that was acquired with a fluorescence microscope are formed
  - Understand how this image formation process has critical influence on the interpretation of intensity measurements
  - Understand that the geometry of your biological specimen can have a large influence on the measured intensities
motivation: |
  In bioimage analysis one often wants to quantify the intensities in an image. To do this properly one needs to be aware that these intensities are influenced by many factors, making intensity quantification in general very difficult. Sometimes the measured intensities can be affected so much that even object shape measurements can become difficult. For all those reasons it is very important to understand the reasons for signal distortion! Not knowing those effects can easily lead to wrong measurements.

concept_map: >
  graph TD
    Ex("Excitation") -->|Sample| F("Fluorophore")
    F --> Em("Emission")
    Em -->|Sample| D("Detector")
    D --> I("Digital image")
    Ex --- PSF("Spatial distribution: PSF")
    F --- SD("Spatial distribution: Sample shape")

figure: /figures/image_formation_confocal.png
figure_legend: Membranes in a zebrafish embryo, imaged with a confocal microscope. The optical axis runs from bottom to top. One sees that membranes appear more contrasty if they run along the optical axis. One also sees that the signal gets dimmer further inside the specimen. In fact, here only the outer-most cell layer is clearly visible.

multiactivities:
  - ["image_formation_fluo_mic/image_formation_confocal.md", [["ImageJ GUI", "image_formation_fluo_mic/image_formation_confocal_imagej_gui.md"]]]
  - ["image_formation_fluo_mic/image_formation_wf_vs_confocal.md", [["ImageJ GUI", "image_formation_fluo_mic/image_formation_wf_vs_confocal_imagej_gui.md"]]]

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

