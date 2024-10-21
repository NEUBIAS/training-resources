---
title: Batch exploration of segmentation results
layout: module
tags:
prerequisites:
  - "[Segment and measure nuclei shapes](../workflow_segment_2d_nuclei_measure_shape)"
objectives:
  - "Use various tools to efficiently inspect segmented images and corresponding object measurements."
motivation: |
  Deriving scientifically sound conclusions from microscopy experiments typically requires batch analysis of large image data sets. Once the analysis has been conducted it is critical to visually inspect the results to identify errors and to make scientific discoveries. To do so efficiently requires making oneself familiar with appropriate tools.

concept_map: >
  graph TD
    I("Images") --> BA("Batch analysis")
    BA --> S("Segmentations") 
    S --> M("Object measurements")
    I --> Q("Visual QC")
    S --> Q
    M --> Q

figure: /figures/batch_qc_and_exploration.png
figure_legend: "Depiction of a typical bioimage analysis workflow, where batch analysis of many input images yields object segmentation images and measurements, which must be quality controlled and explored for scientific discovery."

multiactivities:
  - ["batch_qc_and_exploration/batch_explore_segmented_images.md", [["Fiji MoBIE", "batch_qc_and_exploration/batch_explore_segmented_images_fiji_mobie.md"], ["napari (TODO)", "batch_qc_and_exploration/batch_explore_segmented_images_napari.py"]]]
  - ["batch_qc_and_exploration/batch_explore_segmented_images_and_object_measurements.md", [["Explore Images & Labels & Tables - Fiji MoBIE", "batch_qc_and_exploration/batch_explore_segmented_images_and_object_measurements_fiji_mobie.md"], ["Explore Objects Table - Fiji MoBIE", "batch_qc_and_exploration/batch_explore_objects_table_fiji_mobie.md"]]]
  - ["batch_qc_and_exploration/batch_explore_ilastik_output.md", [["Explore ilastik tracking results - Fiji MoBIE", "batch_qc_and_exploration/batch_explore_ilastik_tracking_results_fiji_mobie.md"]]]

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .
    
    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:
  - 

external_links:
  - "[MoBIE documentation](https://mobie.github.io/)"
---

