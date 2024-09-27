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
     Light -->|interacs with| Sample -->|forms an| Image

figure: /figures/image_formation_confocal.png
figure_legend: Membranes in a zebrafish embryo, imaged with a confocal microscope. The optical axis runs from bottom to top. One sees that membranes appear more contrasty if they run along the optical axis. One also sees that the signal gets dimmer further inside the specimen. In fact, here only the outer-most cell layer is clearly visible.

multiactivities:
  - ["image_formation_fluo_mic/image_formation_confocal.md", [["ImageJ GUI", "image_formation_fluo_mic/image_formation_confocal_imagej_gui.md"]]]
  - ["image_formation_fluo_mic/image_formation_wf_vs_confocal.md", [["ImageJ GUI", "image_formation_fluo_mic/image_formation_wf_vs_confocal_imagej_gui.md"]]]

assessment: >

  ### Fill in the blanks

    1. In fluorescence microscopy the signal quality typically ___ when imaging deep inside a specimen.
    1. In confocal microscopy elongated structures that align with the z-axis typically appear ___ than elongated structures that align with the x or y-axis.
    1. In wide-field fluorescence microscopy there is no  ___ and thus signal intensity quantifications for one specific z-position are typically not possible.
    
    > ## Solution
    >   1. decreases
    >   1. brighter
    >   1. optical sectioning
    {: .solution}

learn_next:
  - "[Intensity measurements of fluorescent objects](../measure_intensities)"

external_links:
---

