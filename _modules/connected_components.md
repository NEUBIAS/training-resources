---
title: Connected component labeling
layout:  module
tags: ["label mask","instance segmentation"]
prerequisites:
  - "[Thresholding](../binarization)"
  - "[Display settings](../display_settings)"
  - "[Data types](../datatypes)"

objectives:
  - "Understand how objects in images are represented as a label mask image"
  - "Apply connected component labeling to a binary image to create a label mask image"

motivation: >
  A main task of bioimage analysis is to detect objects in images. To do so one needs to be able to label pixels that are part of the same object in a way that this can be efficiently stored and processed by the computer. A prevalent way of doing this is connected component labeling, which is discussed in this module.


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

multiactivities:
  - ["connected_components/connected_components_act1.md", [["ImageJ MorpholibJ Macro & GUI", "connected_components/connected_components_act1_imagejmacro.ijm", java], ["skimage napari", "connected_components/connected_components_act1_skimage_napari.py", python], ["Knime", "connected_components/connected_components_act1_knime.md"]]]
  - ["connected_components/connected_components_act2.md", [["ImageJ MorpholibJ Macro & GUI", "connected_components/connected_components_act2_imagejmacro.ijm", java], 
  ["skimage napari", "connected_components/connected_components_act2_skimage_napari.py", python]]]
  - ["connected_components/connected_components_act3.md",  [["ImageJ MorpholibJ Macro & GUI", "connected_components/connected_components_act3_imagejmacro.ijm"], 
  ["skimage napari", "connected_components/connected_components_act3_skimage_napari.py", python]]]



assessment: >

  #### Fill in the blanks
    Fill in the blanks, using these words: less, larger, 6, 255, 4, more.
    1. In 3D, pixels have _____ neighbors than in 2D.
    1. 8-connected connectivity results in _____ objects than 4-connected connectivity.
    1. In 3D, pixels have ____ non-diagonal neighbors.
    1. In 2D, pixels have ____ non-diagonal neighbors.
    1. A 8-bit label mask image can have maximally _____ objects.
    1. The maximum value in a label mask image is equal to or _____ than the number of objects.
    
    > ## Solution
    > 1. more
    > 1. less
    > 1. 6
    > 1. 4
    > 1. 255
    > 1. larger
    {: .solution}

learn_next:
   - "[Object shape measurements](measure_shapes)"
external_links:
  - "[Wikipedia: Connected components labeling](https://en.wikipedia.org/wiki/Connected-component_labeling)"
---


Typically, one first categorise an image into background and foreground regions, which can be represented as a binary image. Such clusters in the segmented image are called connected components. The relation between two or more pixels is described by its connectivity. The next step is a connected components labeling, where spatially connected regions of foreground pixels are assigned (labeled) as being part of one region (object).

<img src="../figures/connected_components_connectivity2D.png"  align ="left" width="50%" >
<img src="../figures/connected_components_connectivity3D.png"  align ="right" width="50%">

In an image, pixels are ordered in a squared configuration. 

For performing a connected component analysis, it is important to define which pixels are considered direct neighbors of a pixel. This is called connectivity and defines which pixels are considered connected to each other.

Essentially the choice is whether or not to include diagonal connections.

Or, in other words, how many orthogonal jumps to you need to make to reach a neighboring pixel; this is 1 or an orthogonal neighbor and 2 for a diagonal neighbor.

This leads to the following equivalent nomenclatures:

- 2D: 1 connectivity = 4 connectivity
- 2D: 2 connectivity = 8 connectivity
- 3D: 1 connectivity = 6 connectivity
- 3D: 2 connectivity = 26 connectivity


