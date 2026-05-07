---
title: Optical sectioning
layout: module
tags: ["draft"]
prerequisites:
  - "[Point spread function](../psf)"
objectives:
  - "Understand the effect of optical sectioning in an image"
motivation: |
  The signal (e.g. photons) from a plane that is in focus gives a crisp and well resolved image. Unfortunately, we may also get photons from planes that are not in focus and this deteriorates the quality of the image (blur).  Optical sectioning describe the ability of an imaging system to isolate a thin plane of interest within a 3D specimen and reject (or avoid) out of focus light. 
  
  Technically there are different ways to achieve optical sectioning (pinhole in the detection, selective plane illumination, multi-photon). We can also use post-acquisition computational methods to reassign out-of-focus light, i.e. deconvolution. 

concept_map: >
  graph LR
      %% 1. The Starting Point
      Object[3D Specimen] -->|Goal: Isolate thin slices| OS{OPTICAL<br>SECTIONING}

      %% 2. The Three Main Categories
      OS --> Hardware[1. Hardware Sectioning<br>Photon Rejection]
      OS --> Illumination[2. Illumination Sectioning<br>Selective Excitation]
      OS --> Computational[3. Computational Sectioning<br>Photon Reassignment]

      %% 3. Specific Methods
      subgraph Methods [Specific Implementations]
          Hardware --- Confocal["Confocal (Pinhole)"]
          
          Illumination --- LSFM["Light Sheet (LSFM)"]
          Illumination --- TIRF["TIRF (Evanescent wave)"]
          
          Computational --- Decon["Deconvolution (PSF-based)"]
      end

figure: /figures/optical_sectioning.png
figure_legend: Concept of optical sectioning and comparison of a widefield and confocal image

multiactivities:
  - ["optical_sectioning/act01.md", [["ImageJ GUI", "optical_sectioning/act01_imagejgui.md"]]]

assessment: >

  ### Fill in the blanks

    1. In fluorescence microscopy the signal quality typically ___ when imaging deep inside a specimen.
    1. In wide-field fluorescence microscopy there is no  ___ and thus signal intensity quantifications for one specific z-position are typically not possible.
    
    > ## Solution
    >   1. decreases
    >   1. optical sectioning
    {: .solution}

learn_next:
  - 

external_links:
  - "[Optical sectioning methods in three-dimensional bioimaging](https://www.nature.com/articles/s41377-024-01677-x)"
---

