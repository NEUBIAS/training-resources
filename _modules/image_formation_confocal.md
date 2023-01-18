---
title: Confocal microscopy image formation
layout: module
tags: ["image formation","draft"]
prerequisites:
  - "[TODO](../template)"
objectives:
  - Understand how the intensities in a digital image that was acquired with a confocal microscope are formed
  - Understand that the geometry of your biological specimen can have a large influence on these intensities
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

activity_preface: |
  - Open the [zebrafish embryo image](https://oc.embl.de/index.php/s/gRckFAfkkbrRGQh)
  - Inspect the image and appreciate that 
    - membranes appear with more contrast if they run along the optical axis
    - signal decays within the specimen, due to scattering and absorption
  - To do so, it is useful to slice the data along the x-z or y-z axis

activities:

exercises:

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

