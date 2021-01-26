---
title:     Connected component labeling  
layout:    module

prerequisites:
  - "[Binarization](../binarization)"
  - "[Lookup tables](../lut)"
  - "[Data types](../datatypes)"

objectives:
  - Understand how objects in images are represented as a label mask image.
  - Apply connected component labeling to a binary image to create a label mask image.

motivation: >
  In bioimage analysis one very often wants to detect objects or specific regions in images. A typical workflow is to first categorise an image into in background and foreground regions, which can be represented as a binary image. The next step is a connected components labeling, where spatially connected regions of foreground pixels are assigned (labeled) as being part of one region (object).

concept_map: >
  graph TD
    BI("Binary image") -->|input|CC("Connected component analysis")
    C("Connectivity") -->|parameter|CC
    OD("Output data type") -->|parameter|CC
    CC -->|output|LI("Label image")
    LI -->|display with|MCL("Multi color LUT")
    LI -->|content|PV("Integer pixel values")
    PV --> BG("0: Background")
    PV --> R1("1: Region 1")
    PV --> R2("2: Region 2")
    PV --> R3("...")

figure: /figures/connected_components.png
figure_legend:

activity_preface: >
  1. 2D connected component labeling:
    - Open image [xy_8bit_binary__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei.tif).
    - Create a label image by means of 4-connected connected components labeling. 
    - Apply a multi-color LUT.
    - Repeat with 8-connected labeling and discuss the difference.
  2. 3D connected component labeling:
    - Open image [xyz_8bit_binary__spots.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_binary__spots.tif) 
    - Inspect the histogram of the label image and discuss what you can learn from it.

activities:
  - ["ImageJ MorpholibJ Macro & GUI", "connected_components/activities/connected_components_imagejmacro.ijm", java]
#  "KNIME": "connected_components/activities/connected_components_knime.md"

exercises:
  - ["ImageJ MorpholibJ Macro & GUI", "connected_components/exercises/connected_components_imagejmacro.md"]



assessment: >

  #### Fill in the blanks
    Fill in the blanks, using these words: less, more, 8, 255, 4, more.
    1. In 3D, pixels have _____ neighbors than in 2D.
    1. 8-connected connectivity results in _____ objects than 4-connected connectivity.
    1. In 3D, pixels have ____ non-diagonal neighbors.
    1. In 2D, pixels have ____ non-diagonal neighbors.
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

# Connectivity

In an image pixels are ordered in a squared configuration. For performing a connected component analysis 
it is important to define which pixels are considered direct neighbors of a pixel. This is called connectivity and defines which 
pixels are considered connected to each other. Unfortunately, there is not only one way to define connectivity. Depending,
if we consider corner pixels or not we can have in 2D a 4 or 8--connectivity, respectively, in 3D a 6 or 26-connectivity. Which connectivity 
value we choose can affect the object size.
<img src="../figures/connected_components_connectivity2D.png"  align ="left" width="50%" >
<img src="../figures/connected_components_connectivity3D.png"  align ="right" width="50%">





