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
    N["Nuclei"] --> TN("Threshold")
    G["Golgi"] --> TG("Threshold")
    TN --> CN("Connected components labeling")
    TG --> CG("Connected components labeling")
    CG --> GL["Golgi label mask"]
    CN --> NL["Nuclei label mask"]
    GL -->|assign| NL

figure: /figures/workflow_golgi_per_cell.png
figure_legend: Nuclei/cell and Golgi segmentation with assignment of Golgi labels to cell labels.

activity_preface: |
  - Open the image [xyc_16bit__nuclei_golgi.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nuclei_golgi.tif).
  - Segment nuclei and Golgi
  - Dilate nuclei to approximate cells
  - Assign the Golgi fragments to their parent cell
    - Measure the intensity of the child (Golgi) objects in the parent (cell) label mask
    - You could, e.g., measure the `min`, `max` and `mode` intensity
      - `min = max`: the child object is within one parent object
      - `min != max`: the child object overlaps with multiple parent objects
        - `mode`: the label of the parent object that the child object overlaps most with
      - `min = 0`: the child object is (partically) located outside of any parent cell


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

