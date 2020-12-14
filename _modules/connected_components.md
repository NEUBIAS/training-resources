---
title:     Connected component labeling  
layout:    module
prerequisites:
  - "[Image binarization](binarization)"
objectives:
  - Understand what a label mask image is.
  - Apply connected component labeling to create a label mask image.
motivation: >
  Very often, one wants to detect objects or specific regions in images. A typical workflow is to first divide an image into in background and foreground regions, which can be represented as a binary image. The next step is a connected components labeling, where spatially connected regions of foreground pixels are assigned (labeled) as being part of one region (object).
  
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
  Open a binary image and conduct a connected components labeling.

activities:
  "ImageJ GUI": "connected_components/activities/connected_components_imagejgui.md"
  "KNIME": "connected_components/activities/connected_components_knime.md"
#  "MATLAB": "" 

exercises_preface: >

  Fill in the blanks, using these words: less, more, 8, 255, 4, more.
  
  1. In 3D, pixels have _____ neighbors than in 2D.
  2. 8-connected connectivity results in _____ objects than 4-connected connectivity.
  3. In 3D, pixels have ____ non-diagonal neighbors.
  4. In 2D, pixels have ____ non-diagonal neighbors.
  5. A 8-bit label image can maximally have _____ objects.
  6. The maximum value in a label image is equal to or _____ than the number of objects.

exercises:

learn_next:
  - "[Split touching objects](object_splitting)"
  - "[Measure object shapes](measure_shapes)"
external_links:
  - "[Wikipedia: Connected components labeling](https://en.wikipedia.org/wiki/Connected-component_labeling)"
---
