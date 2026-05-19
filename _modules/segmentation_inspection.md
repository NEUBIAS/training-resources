---
title: Segmentation inspection
layout: module
tags: ["segmentation"]
prerequisites:
  - "[Segmentation overview](../segmentation)"
  - "[Thresholding](../binarization)"
  - "[Connected component labeling](../connected_components)"
objectives:
  - "Visually inspect segmentation quality by overlaying segmentations on the raw image"
  - "Compute IoU for semantic segmentation by converting label masks to binary masks"
  - "Compare instance segmentations using object counts and mean object area"
motivation: |
  Segmentation quality should be inspected both visually and quantitatively.
  In this module we compare segmentation outputs against a reference segmentation
  using a minimal and practical set of checks that are easy to apply in teaching
  and in daily analysis workflows.

concept_map: >
  graph TD
    R("Raw image") --> V("Visual inspection")
    R --> S("Semantic comparison")
    R --> I("Instance comparison")
    S --> B("Binary masks")
    B --> M("IoU")
    I --> C("Object count")
    I --> A("Mean object area")

figure: /figures/segmentation.png
figure_legend: Segmentation can be inspected qualitatively (overlay) and quantitatively (semantic and instance metrics).

multiactivities:
  - ["segmentation_inspection/visual_inspection.md", [["skimage napari", "segmentation_inspection/visual_inspection_skimage_napari.py", "python"]]]
  - ["segmentation_inspection/semantic_comparison.md", [["skimage napari", "segmentation_inspection/semantic_comparison_skimage_napari.py", "python"]]]
  - ["segmentation_inspection/instance_comparison.md", [["skimage napari", "segmentation_inspection/instance_comparison_skimage_napari.py", "python"]]]

assessment: >

  ### Fill in the blanks

    - IoU is computed as intersection divided by ___.
    - For semantic IoU in this module, label masks are first converted to ___.

    > ## Solution
    >   - union
    >   - binary masks
    {: .solution}

learn_next:
  - "[Nuclei segmentation and shape measurement](../workflow_segment_2d_nuclei_measure_shape)"
  - "[Nuclei and cells segmentation](../workflow_nuclei_and_cells_segmentation)"

external_links:
  - "[Metrics reloaded](https://www.nature.com/articles/s41592-023-02151-z)"
---
