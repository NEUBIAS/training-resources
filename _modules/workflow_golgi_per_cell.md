---
title: Segment Golgi objects per cell
layout: module
tags: ["draft","workflow"]
prerequisites:
  - "[Nuclei segmentation and shape measurement](../workflow_segment_2d_nuclei_measure_shape)"
objectives:
  - "Segment intracellular objects and assign them to their parent cell"
motivation: |
  Very often in bioimage analysis one wants to measure the properties of certain intracellular objects (e.g. vesicles) per cell. For example, those objects might be more frequent or larger in one cell than another. To perform such measurements it is very important to know how to assign ("child") objects that are contained in larger ("parent") objects to another.

concept_map: >
  graph TD
    N["Nuclei"] --> T("Threshold")
    N["Golgi"] --> T("Threshold")
    T --> C("Connected components labeling")
    C --> GL["Golgi label mask"]
    C --> NL["Nuclei label mask"]
    GL -->|intensity in| NL

figure: /figures/template.png
figure_legend: TODO

activity_preface: |
  - Open the image [xyc_16bit__nuclei_golgi.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nuclei_golgi.tif).
  - Segment nuclei and Golgi
  - Dilate nuclei to approximate cells
  - Assign the Golgi fragments to their parent cell
    - Technically: Measure the intensity of the Golgi objects in the cell label mask 

activities:
  - ["ImageJ Macro", "workflow_golgi_per_cell/activities/workflow_golgi_per_cell.ijm", "java"]

exercises:

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

