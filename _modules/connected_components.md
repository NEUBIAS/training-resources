---
title:     Connected component labeling  
layout:    module

prerequisites:
  - "[Image binarization](binarization)"

objectives:
  - Apply connected component labeling to create a label mask image.

motivation: >
  In bioimage analysis one very often wants to detect objects or specific regions in images. A typical workflow is to first categorise an image into in background and foreground regions, which can be represented as a binary image. The next step is a connected components labeling, where spatially connected regions of foreground pixels are assigned (labeled) as being part of one region (object).
  
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
figure_legend:

activity_preface: >
  Open a binary image and conduct a connected components labeling.

activities:
#  "ImageJ GUI": "connected_components/activities/connected_components_imagejgui.md"
#  "KNIME": "connected_components/activities/connected_components_knime.md"
#  "MATLAB": "" 

exercises:

assessment: >

  ### Connected component labelling and label mask image properties
    Fill in the blanks, using these words: less, more, 8, 255, 4, more.
    1. In 3D, pixels have _____ neighbors than in 2D.
    1. 8-connected connectivity results in _____ objects than 4-connected connectivity.
    1. In 3D, pixels have ____ non-diagonal neighbors.
    1.  In 2D, pixels have ____ non-diagonal neighbors.
    1. A 8-bit label mask image can have maximally _____ objects.
    1. The maximum value in a label mask image is equal to or _____ than the number of objects.
    
    > ## Solution
    > 1. more
    > 1. less
    > 1. 8
    > 1. 4
    > 1. 255
    > 1. less
    {: .solution}

learn_next:
#  - "[Split touching objects](object_splitting)"
#  - "[Measure object shapes](measure_shapes)"
external_links:
  - "[Wikipedia: Connected components labeling](https://en.wikipedia.org/wiki/Connected-component_labeling)"
---
