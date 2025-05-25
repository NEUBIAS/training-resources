---
title: "2D noisy object segmentation and filtering"
layout: module
tags: ["workflow"]
prerequisites:
  - "[Neighborhood filters](../filter_neighbourhood)"
  - "[Thresholding](../binarization)"
  - "[Connected component labeling](../connected_components)"
  - "[Object filtering](../filter_objects)"
  - "[Object shape measurements](../measure_shapes)"
objectives:
  - "Create an image analysis workflow comprising image denoising and object filtering."

motivation: |
  Finding objects in images typically presents itself with two challenges. First, the input image may not lend itseld to a simple intensity thresholding operation for binarisation. Second, there may be unwanted objects in the image such as hot pixels or objects that are not fully in the image. The first challenge typically is tackled by applying appropriate image filters to the raw data. The second challenge is tackled by defining and applying reproducible criteria to remove certain objects from the image.
  
concept_map: >
  graph TD
    GI["Grayscale input image"] --> FGI["Filtered grayscale image"]
    FGI -->|has property|P["Interesting stuff is bright"]
    FGI --> BI["Binary image"]
    BI --> LI["Label image"]
    LI --> FLI["Subset label image"]
    FLI -->|has property|U["Unwanted labels are removed"]
    FLI --> S("Shape measurement")
    S --> SFT["Object feature table"]

figure: /figures/workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape.png
figure_legend: Nuclei segmentation and area measurement, including image denoising and object filtering.

multiactivities:
  - ["workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/segment_2d_noisy_nuclei_and_filter_objects.md", [["ImageJ Macro & GUI", "workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/segment_2d_noisy_nuclei_and_filter_objects_imagejmacro.ijm", "java"], ["skimage and napari", "workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/segment_2d_noisy_nuclei_and_filter_objects_skimage_napari.py"]]]

exercises:

assessment: >

learn_next:

external_links:

---
