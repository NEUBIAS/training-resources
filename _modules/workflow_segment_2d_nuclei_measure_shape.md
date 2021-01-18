---
title:     Workflow - Simple 2D object analysis
layout:    module
prerequisites:
  - "[Binarization](../binarization)"
  - "[Connected component labeling](../connected_components)"
  - "[Object shape measurements](../measure_shapes)"
objectives:
  - "Create a simple image analysis workflow."
  - "Understand that bioimage analysis workflows consist of a sequence of image analysis components."
  - "Segment nuclei in a 2D image and measure their shapes and understand the different components (concepts and methods) that are needed to accomplish this task."
  - "Draw a biophysically meaningful conclusion from applying an image analysis workflow to a set of images."

motivation: |
  Detecting a set of objects in an image, counting them and measuring certain characteristics about their morphology is probably the most frequently occurring task in bioimage analysis. Depending on the image, even this task could become quite challenging and the workflow could become quite complex. Here we start with a relatively easy image where combining a minimal set of image analysis components into a simple workflow does the job.
  
concept_map: >
  graph TD
    B("Binarise") --> BI["Binary Image"] 
    BI --> C("Connected Component Labeling")
    C --> LI["Label Image"]
    LI --> S("Shape Measurement")
    S --> SFT["Shape Feature Table"]

figure: /figures/workflow_segment_2d_nuclei_measure_shape.png
figure_legend: Nuclei segmentation and area measurement workflow

activity_preface: |
  Open the image "xy_8bit_mitocheck_incenp_t1.tif", segment the nuclei, count how many there are and measure their shapes. For this task, you have to combine several image analysis components in the right order (you can find teaching material about those components in this modules prerequistes, s.a.). Specifically, create a table where each row corresponds to one nucleus. One of the colums of this table should contain the area of each nucleus in nm^2. Repeat this for the image "xy_8bit_mitocheck_incenp_t70.tif" and calculate the ratio of the average nucleus areas in both images.


activities:
  - ["ImageJ Macro", "workflow_segment_2d_nuclei_measure_shape/activities/segment_2d_nuclei_imagejmacro.ijm", "java"]

exercises:

assessment: >


learn_next:

external_links:

---
## Background information on the image data

The image data in this workflow is taken from the [mitocheck](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3108885/) publication, where the authors carried out a genome-wide phenotypic profiling of each of the ~21,000 human protein-coding genes by two-day live imaging of fluorescently labelled chromosomes. Phenotypes were scored quantitatively by computational image processing, which allowed them to identify hundreds of human genes involved in diverse biological functions including cell division, migration and survival. The analysis that we do here is of course simpler than what the authors did in the publication, but the essence is already very similar.

To simplify the task we work here on images that were both cropped and slightly filtered to reduce the noise.
