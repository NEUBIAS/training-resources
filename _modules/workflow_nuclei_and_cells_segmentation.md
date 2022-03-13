---
title: Nuclei and cells segmentation
layout: module
tags: ["draft","workflow"]
prerequisites:
  - "[Watershed transform](../watershed)"
objectives:
  - "Segment cells and nuclei, using nuclei as seeds for watershed segmentation of the cells."
motivation: |
  It is quite common to have fluorescence microscopy images with stainings for both nuclei and cytoplasm. While nuclei are typically separate and thus easy to segment, cells are often touching each other, which makes their segmentation much more challenging. The workflow presented in this module is a common approach to tackle this challenge and thus very useful to know.

concept_map: >
  graph TD
    N("Nuclei") --> NM("Nuclei label mask")
    C("Cells") --> W("Watershed transform")
    NM -->|seeds| W
    W --> S("Cells label mask")

figure: /figures/workflow_nuclei_and_cell_segmentation.png
figure_legend: Workflow for nuclei and cell segmentation using marker-controlled watershed (magenta - H2B-mCherry; green - GFP-tubulin). The nuclei mask is used to define the seeds/markers, the tubulin-channel is used to define the overall cells boundaries, finally the inverted intensity image is used for the watershed transform (i.e. flooding).

activity_preface: |
  - Open image [xyc_16bit__nuclei_tubulin_crop.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nuclei_tubulin_crop.tif).
  - Segment nuclei and cells following the workflow depicted in the module figure.

activities:
  - ["ImageJ Macro", "workflow_nuclei_and_cells_segmentation/activities/workflow_nuclei_and_cells_segmentation_imagejmacro.ijm", "java"]

exercises:

assessment: >

  ### Discuss with your neighbour

    1. For a marker controlled watershed what will happen if you remove seeds touching the boundary before the watershed transform?
    2. Can you use the cell-mask, instead of the intensity image, for the watershed transform? 
    
    > ## Solution
    >   1. This is not a good idea as you may not be able to find all cells and properly separate those. For instance merged cells may still touch the boundary.  
    >   2. Apply a distance transform to the cell-mask and apply the watershed transform on its inverse.
     {: .solution}

  ### True or false?
    1. For cell segmentation with a watershed transform one always needs nuclei as seeds.
    1. Nuclei are less likely to touch each other than cells.
    1. For a watershed transform, it is very important to image the cytoplasmic signal at the highest resolution.
    
    > ## Solution
    >   1. False; if the cellular signal happens to, e.g., be very dim in the cell center and bright at the cell boundaries one may try directly using it as an input to a watershed transform.
    >   1. True; nuclei have the cytoplasm around them, which often creates a spatial gap between neighbouring nuclei, making them easier to segment
    >   1. False; in fact, typically, the blurrier this signal is the better it is suited for separating cells using the watershed transform.
    {: .solution}

learn_next:

external_links:
---

