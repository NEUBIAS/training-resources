---
title: Illumination and shading artefacts
layout: module
tags: ["draft"]
prerequisites:
  - "[Digital image basics](../pixels)"
objectives:
  - "Identify global shading patterns caused by e.g. Gaussian illumination"
  - "Distinguish between localized dust artifacts and global intensity gradients"
  - "Understand implication for intensity measurements"
motivation: |
  Non-uniform illumination and shading artefacts are common image quality issues where brightness varies unevenly across an image, often appearing as vignetting (darker corners), streaks, or gradient shadows. These effects arise from lighting inefficiencies, detection limitations, and/or light path obstructions. They degrade the image quality and confuse intensity-based analysis and image processing. 

concept_map: >
  graph TD
    Artifacts("Illumination Artifacts") --- Patterns("Spatial Patterns")
    Artifacts --- Sources("Hardware Sources")
    
    Patterns --- Global("Global Shading")
    Patterns --- Local("Local Artifacts")
    
    Global --- Vignetting("Vignetting (Bright Center)")
    Global --- Gradient("Intensity Gradient")
    
    Local --- Shadows("Shadows")
    Local --- Occlusion("Light Path Obstruction")

    Sources --- Light("Light Source (Gaussian)")
    Sources --- Optics("Optical Path (Dust/Dirt)")
    Sources --- Align("Misalignment (Köhler)")


figure: /figures/illumination_artefact.png
figure_legend: Example of uneven illumination in fluorescence and transmission images

multiactivities:
  - ["illumination_artefact/act01.md", [["ImageJ GUI", "illumination_artefact/act01_imagejgui.md"], ["skimage napari", "illumination_artefact/act01_skimage_napari.py"]]]

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .
    
    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:
  - "[Flat field correction](../flatfield_correction)"

external_links:
---

