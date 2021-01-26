---
title:     Workflow - 2D noisy object segmentation and filtering
layout:    module
prerequisites:
  - "[Neighbourhood filters](../filter_neighbourhood)"
  - "[Binarization](../binarization)"
  - "[Connected component labeling](../connected_components)"
  - "[Object filters](../filter_objects)"
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

activity_preface: |
  
  #### Input images
  - [xy_8bit__nuclei_noisy_small.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_small.tif)
  - [xy_8bit__nuclei_noisy_large.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_large.tif)
  
  #### Workflow:
  Apply the workflow outlined above (see Concept map and Example figure) to both images. The modules listed in this module's Prerequisites contain the information as to how to conduct each step of the workflow.

activities:
  - ["ImageJ Macro & GUI", "workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/activities/segment_2d_noisy_nuclei_and_filter_objects_imagejmacro.ijm", "java"]

exercises:

assessment: >

learn_next:

external_links:

---
