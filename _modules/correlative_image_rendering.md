---
title: Correlative image rendering
layout: module
tags: ["draft", "visualisation"]
prerequisites:
  - "[Spatial calibration](../spatial_calibration)"
  - "[Digital image basics](../pixels)"
objectives:
  - "Understand how heterogeneous image data can be mapped from voxel space into a global coordinate system."
  - "Understand how an image viewer can render a plane from a global coordinate system."
motivation: |
  In correlative microscopy the same specimen is imaged with multiple modalities. While this provides great opportunities for scientific discovery it poses some visualisation challenges. The various images may have different voxel sizes and different dimensionality and may be translated and rotated with respect to another. To tackle this challenge appropriate image viewer software and image data file formats must be chosen. To make those hoices it is important to understand the basic concepts of correlative image rendering, as well as know some concrete implementations.

concept_map: >
  graph TD
    DC("Data coordinates") -->|"transform (d2g)"| GC("Global coordinates")
    GC -->|"transform (g2v)"| VC("Viewer coordinates")

figure: /figures/template.png
figure_legend: TODO

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
---

