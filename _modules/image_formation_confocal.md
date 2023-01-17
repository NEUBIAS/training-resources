---
title: Confocal microscopy image formation
layout: module
tags: ["image formation"]
prerequisites:
  - "[TODO](../template)"
objectives:
  - Understand how the intensities in a digital image that was acquired with a confocal microscope are formed
  - Understand that the geometry of your biological specimen can have a large influence on these intensities
motivation: |
  In bioimage analysis one often wants to quantify the intensities in an image. To do this properly one needs to be aware that these intensities are influenced by many factors, making intensity quantification in general very difficult. Sometimes the measured intensities can be affected so much that even object shape measurements can become difficult. For all those reasons it is very important to understand the reasons for signal distortion! Not knowing those effects can easily lead to wrong measurements.

concept_map: >
  graph TD
    F("Fluorophore") --> S("Signal")
    Ex("Excitation") --> F
    F --> Em("Emission")
    Em --> Detector

figure: /figures/template.png
figure_legend: TODO

activity_preface: |
  - Open the image [xy_8bit_binary__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei.tif).
  - TODO

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

