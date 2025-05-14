---
title: Correlative image rendering
layout: module
tags: ["visualisation"]
prerequisites:
  - "[Spatial calibration](../spatial_calibration)"
  - "[Digital image basics](../pixels)"
objectives:
  - "Understand how heterogeneous image data can be mapped from voxel space into a global coordinate system."
  - "Understand how an image viewer can render a plane from a global coordinate system."
motivation: |
  "In correlative microscopy the same specimen is imaged with multiple modalities. While this provides great opportunities for scientific discovery it poses some visualisation challenges. The various images may have different voxel sizes and different dimensionality and may be translated and rotated with respect to another. To tackle this challenge appropriate image viewer software and image data file formats must be chosen. To make those hoices it is important to understand the basic concepts of correlative image rendering, as well as know some concrete implementations."

concept_map: >
  graph TD
    DC1("Image data 1") -->|"transform (dgt_1)"| GC("Global (physical) coordinates")
    DC2("Image data 2") -->|"transform (dgt_2)"| GC
    GC -->|"transform (gvt)"| VC("Viewer (screen) coordinates")

figure: /figures/registration_visualization.svg
figure_legend: "Depiction of how the data (array) spaces of two hetero-dimensional images are mapped onto a computer screen. Note that even though the first image is 2-D, it is depicted 3-D in data space by means of adding a singleton dimension. In practice, the computer can loop through all screen pixels (viewer space) and use the given formula to fetch the corresponding values from the data spaces. If there are several values (in this example there are two), then a blending and coloring scheme must be applied to produce the final RGB value that is displayed on the computer screen (this will be discussed in other teaching modules). NOTE: probably it is better to speak of array space rather than data space, because the actual data may live below the array in some other space, like a series of time-tagged measurements in a point-scanning confocal. Then there also is the storage space, which is probably linear, e.g. on a hard-disk, and may be chunked."

multiactivities:
  - ["correlative_image_rendering/activities/correlative_image_rendering.md", [["MoBIE", "correlative_image_rendering/activities/mobie.md", "markdown"]]]

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
  - "[BigDataViewer publication](https://www.nature.com/articles/nmeth.3392/)"
  - "[Model View Projection](https://jsantell.com/model-view-projection/)"
---

