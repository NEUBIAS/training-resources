---
title: Imaging thick biological samples
layout: module
tags: ["image formation"]
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[Point spread function](../psf)"
  - "[Optical sectioning](../optical_sectioning)"
objectives:
  - Understand that the geometry and optical properties of your biological specimen can have a large influence on the measured intensities
motivation: |
  When imaging thick samples, one needs to be aware that intensities are influenced by many factors, making intensity quantification in general very difficult.  Measured intensities can be affected so much that even object shape measurements can become difficult. Already, the nature of the PSF makes measurements along the Z-direction different than in the XY plane, biological specimens can be more or less opaque (scattering, refracting index mismatch, absorption) making measurements deeper in the sample challenging. For all those reasons it is very important to understand the reasons for signal distortion. Not knowing those effects can easily lead to wrong measurements and conclusions. 

concept_map: >
  graph TD
     Light -->|interacs with| Sample -->|forms an| Image

figure: /figures/image_formation_confocal.png
figure_legend: Membranes in a zebrafish embryo, imaged with a confocal microscope. The optical axis runs from bottom to top. One sees that membranes appear more contrasty if they run along the optical axis. One also sees that the signal gets dimmer further inside the specimen. In fact, here only the outer-most cell layer is clearly visible.

multiactivities:
  - ["image_formation_fluo_mic/image_formation_confocal.md", [["ImageJ GUI", "image_formation_fluo_mic/image_formation_confocal_imagej_gui.md"]]]

assessment: >

  ### Fill in the blanks

    1. In fluorescence microscopy the signal quality typically ___ when imaging deep inside a specimen.
    1. In confocal microscopy elongated structures that align with the z-axis typically appear ___ than elongated structures that align with the x or y-axis.
    
    > ## Solution
    >   1. decreases
    >   1. brighter
    {: .solution}

learn_next:
  - "[Object intensity measurements](../measure_intensities)"
  - "[Spherical aberrations](../spherical_aberrations)"

external_links:
 - 
---

