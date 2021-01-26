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
    I("Grayscale image") --> T("Intensity threshold")
    T --> BI["Binary image"] 
    BI --> C("Connected component labeling")
    C --> LI["Label image"]
    LI --> S("Shape measurement")
    S --> SFT["Object feature table"]

figure: /figures/workflow_segment_2d_nuclei_measure_shape.png
figure_legend: Nuclei segmentation and area measurement

activity_preface: |
  
  #### Input images
    - [xy_8bit__mitocheck_incenp_t1.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif)
  - [xy_8bit__mitocheck_incenp_t70.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t70.tif)
  
  The images are two time points of a time lapse experiment where the INCENP gene was subjected to siRNA knock-down. The data are taken from the published [mitocheck screen](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3108885/). In this screen the authors carried out a genome-wide phenotypic profiling of each of the ~21,000 human protein-coding genes by two-day live imaging of fluorescently labelled chromosomes. Phenotypes were scored quantitatively by computational image processing, which allowed them to identify hundreds of human genes involved in diverse biological functions including cell division, migration and survival.
  
  The analysis that we do here is, of course, simpler than what the authors did in the publication, but the essence is already very similar. In addition, to simplify the task we work here on images that were cropped and slightly denoised.
  
  #### Workflow:
  Apply the workflow outlined above (see Concept map) to both images (the modules lists in above "Prerequisites" contain the information as to how to conduct each step of the workflow).
  The nuclei in both images look quite different. Find shape measurements that quantify this.

activities:
  - ["ImageJ Macro & GUI", "workflow_segment_2d_nuclei_measure_shape/activities/segment_2d_nuclei_imagejmacro.ijm", "java"]

exercises:

assessment: >

learn_next:

external_links:

---
