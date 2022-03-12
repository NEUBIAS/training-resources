---
title: Batch processing
layout: module
tags: ["scripting"]
prerequisites:
objectives:
  - "Automatically process a number of images"
motivation: |
  Scientific discovery is based on reproducibility. Thus, it is very common to apply the same analysis workflow to a number of images, possibly comprising different biological conditions. To achieve this, it is very important to know how to efficiently "batch process" many images.

concept_map: >
  graph TD
    I1("Image 1") --> S("Analysis workflow")
    I2("Image 2") --> S
    IN("Image ...") --> S
    S --> R1("Result 1")
    S --> R2("Result 2")
    S --> RN("Result ...")

figure: /figures/batch_processing.png
figure_legend: Batch processing of many images, yielding many tables.

activity_preface: |
  - Batch process several images containing nuclei.
  - Example images can be found in [image_data/batch_process](https://github.com/NEUBIAS/training-resources/tree/master/image_data/batch_process).
    - For each image
      - Segment the nuclei and save the label mask.
      - Measure the nuclei area and save the results in a table.
activities:
  - ["ImageJ Macro Scijava","batch_processing/activities/nuclei_measure_shape_scijava_imagejmacro.ijm", "Java"]

exercises:

assessment: >

  ### Fill in the blanks

    1. If you have thousands of images to process you should consider using a ___ .
    1. Batch processing refers to ____ processing many data sets.
    
    > ## Solution
    >   1. computer cluster (HPC)
    >   1. automatically
    {: .solution}

learn_next:

external_links:
  - "[Batch processing in ImageJ](https://imagej.net/scripting/batch)"
---
