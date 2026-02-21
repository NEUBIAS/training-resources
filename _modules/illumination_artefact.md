---
title: Illumination and shading artefacts
layout: module
tags: ["microscopy"]
prerequisites:
  - "[Digital image basics](../pixels)"
objectives:
  - "Identify global shading patterns caused by e.g. Gaussian illumination"
  - "Understand implication for intensity measurements"
motivation: |
  Non-uniform illumination and shading artefacts are common image quality issues where brightness varies unevenly across an image, often appearing as vignetting (darker corners), streaks, or gradient shadows. These effects arise from lighting inefficiencies, detection limitations, and/or light path obstructions. They degrade the image quality and confuse intensity-based analysis and image processing. 

concept_map: >
  flowchart TD
      S("Sample") --> |Illumination/detection| I("Image") 
      LS("Light Source (Gaussian)") --> A("Illumination artefacts")
      OP("Optical Path (Dust/Dirt)") --> A
      AL("Misalignment (Köhler)") --> A
      A --> Vignetting("Vignetting (Bright Center)") 
      A --> Gradient("Intensity Gradient") 
      A --> Shadows("Shadows") 
      A --> More("...")


figure: /figures/illumination_artefact.png
figure_legend: Uneven illumination creates artefacts in the image

multiactivities:
  - ["illumination_artefact/act01.md", [["ImageJ GUI", "illumination_artefact/act01_imagejgui.md"], ["ImageJ macro", "illumination_artefact/act01_imagejmacro.ijm"]]]



learn_next:
  - "[Flat field correction](../flatfield_correction)"

external_links:
---

