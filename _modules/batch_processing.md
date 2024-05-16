---
title: Batch processing
layout: module
tags: ["scripting"]
prerequisites:
  - "[Working with Strings](../string_concat)"
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

multiactivities:
  - ["batch_processing/measure_nuclei_shapes.md", [["ImageJ SciJava Macro", "batch_processing/batch_measure_nuclei_shape_scijava_ijmacro.md"]]]

exercises_preface: |
  - Download those two images
    - [xy_8bit__nuclei_noisy_small.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_small.tif)
    - [xy_8bit__nuclei_noisy_large.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_large.tif)
  - Modify the script given in the exercise to enable the batch processing of those two images.

exercises:
  - ["ImageJ Macro Scijava","batch_processing/exercises/imagejmacro.md"]

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
