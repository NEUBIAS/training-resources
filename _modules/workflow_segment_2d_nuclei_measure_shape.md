---
title: "Nuclei segmentation and shape measurement"
layout: module
tags: ["workflow"]
prerequisites:
  - "[Thresholding](../binarization)"
  - "[Connected component labeling](../connected_components)"
  - "[Object shape measurements](../measure_shapes)"
objectives:
  - "Create a basic image analysis workflow."
  - "Understand that bioimage analysis workflows consist of a sequence of image analysis components."
  - "Segment nuclei in a 2D image and measure their shapes and understand the components (concepts and methods) that are needed to accomplish this task."
  - "Draw a biophysically meaningful conclusion from applying an image analysis workflow to a set of images."

motivation: |
  Detecting a set of objects in an image, counting them and measuring certain characteristics about their morphology is probably the most frequently occurring task in bioimage analysis. Depending on the image, even this task could become quite challenging and the workflow could become quite complex. Here we start with a relatively simple image where combining a minimal set of image analysis components into a simple workflow does the job.
  
concept_map: >
  graph TD
    I("Grayscale image") --> T("Intensity threshold")
    T --> BI["Binary image"] 
    BI --> C("Connected component labeling")
    C --> LI["Label image"]
    LI --> S("Shape measurement")
    S --> SFT["Object feature table"]

figure: /figures/workflow_segment_2d_nuclei_measure_shape.png
figure_legend: Workflow for nuclei segmentation and area measurement.

multiactivities:
  - ["workflow_segment_2d_nuclei_measure_shape/segment_2d_nuclei.md", [["ImageJ GUI", "workflow_segment_2d_nuclei_measure_shape/segment_2d_nuclei_imagejgui.md", "markdown"], 
  ["ImageJ Macro", "workflow_segment_2d_nuclei_measure_shape/segment_2d_nuclei_imagejmacro.ijm", "java"], 
  ["skimage and napari", "workflow_segment_2d_nuclei_measure_shape/segment_2d_nuclei_skimage_napari.py", "python"]]]
  
assessment: >

learn_next:

external_links:

---
