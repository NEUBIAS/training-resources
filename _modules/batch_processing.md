---
title: Batch processing
layout: module
tags: ["scripting"]
prerequisites:
  - "[Strings and paths](../string_concat)"
  - "[For loops](../script_for_loop)"
objectives:
  - "Automatically process a number of images"
motivation: |
  Scientific discovery is based on reproducibility. Thus, it is very common to apply the same analysis workflow to a number of images, possibly comprising different biological conditions. To achieve this, it is very important to know how to efficiently "batch process" many images.

concept_map: >
  graph TD
    I1("Image 1") --> S("Analysis workflow")
    I2("Image 2") --> S
    IN("...") --> S
    S --> R1("Result 1")
    S --> R2("Result 2")
    S --> RN("...")

figure: /figures/batch_processing.png
figure_legend: Batch processing of several images, yielding as many segmentations and object measurement tables.

multiactivities:
  - ["batch_processing/batch_measure_nuclei_shapes.md", [["ImageJ SciJava Macro", "batch_processing/batch_measure_nuclei_shape_scijava_ijmacro.md"],["skimage python", "batch_processing/batch_measure_nuclei_shape.py"]]]

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
  - [MoBIE](https://github.com/mobie/mobie-viewer-fiji)
  - [ImageDataExplorer](https://git.embl.de/heriche/image-data-explorer)
---
