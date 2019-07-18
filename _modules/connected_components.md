---
title:     Connected components 
layout:    module
prerequisites:
  - "[Image binarization](binarization)"
objectives:
  - TODO
motivation: >
  Very often, one wants to detect objects or specific regions in images. After connected_components, the image is divided in background and foreground pixels. The next step is a connected components analysis, where spatially connected regions of foreground pixels are assigned as being part of one region.
concept_map: >
  graph TD
    BI("Binary image") --> CC("Connected component analysis")
    CC --> LI("Label image")
    LI --> PV("Integer pixel values")
    PV --> BG("0: Background")
    PV --> R1("1: Region 1")
    PV --> R2("2: Region 2")
    PV --> R3("...")

figure: /figures/connected_components.png
figure_legend: Connected component analysis 

activity_preface: >
  Open a binary image and conduct a connected components analysis.

activities:
  "ImageJ GUI": "connected_components/activities/connected_components_imagejgui.md"
#  "MATLAB": "" 

exercises_preface: >

  Fill in the blanks, using these words: less, more, 8, 255, 4, more.
  
  1. In 3D, pixels have _____ neighbors than in 2D.
  1. 8-connected connectivity results in _____ objects than 4-connected connectivity.
  1. In 3D, pixels have ____ non-diagonal neighbors.
  1. In 2D, pixels have ____ non-diagonal neighbors.
  1. A 8-bit label image can maximally have _____ objects.
  1. The maximum value in a label image is equal to or _____ than the number of objects.

exercises:

learn_next:
  - "[Split touching objects](object_splitting)"
  - "[Measure object shapes](measure_shapes)"
external_links:
  - "[Wikipedia: Connected components labeling](https://en.wikipedia.org/wiki/Connected-component_labeling)"
---
