---
title: Watershed
layout: module
tags: ["draft"]
prerequisites:
  - "[Connected-component analysis](../connected_components)"
  - "[Distance transform](../distance_transform)"
objectives:
  - "Understand the concept of watersheds in image analysis."
  - "Understand that a watershed algorithm is often applied to a distance map to split objects by their shape."
  - "Be able to run a watershed algorithm in an image analysis platform."
motivation: |
  The segmentation of touching objects often is a challenge in image analysis. The watershed algorithm is a very common operation to split touching objects and is available in most image analysis frameworks.

concept_map: >
  graph TD
    T("Image") --> W("Watershed algorithm")
    W --> S("Segmented image")
    S --- B("Boundaries/Watersheds: Intensity ridges")
    S --- R("Regions/Basins: Local intensity minima")


figure: /figures/watershed.png
figure_legend: Examples of watersheds, including distance transform.

activity_preface: |
  - Basic watershed
    - Open [xy_8bit__touching_objects.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__touching_objects.tif).
    - Appreciate that you cannot segment the three objects using a simple threshold.
    - Anyway find a threshold that segments the image into foreground (objects) and background (keep this binary image).
    - Invert the original image and perform a watershed algorithm.
    - Appreciate that the image is now split into three regions (watershed image).
    - Use the binary mask (s.a.) and the watershed image to segment the three objects.
  - Shape watershed
     - Open [xy_8bit__touching_objects_same_intensity.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__touching_objects_same_intensity.tif).
    - Appreciate that you cannot segment the three objects using a simple threshold.
    - Appreciate that also a watershed algorithm does not help here, because there is no "intensity ridge" bewteen the two touching objects.
    - Create a binary mask
    - Create a distance map within objects

activities:
- ["ImageJ Macro: MorpholibJ basic watershed", "watershed/activities/morpholibj_basic_watershed.ijm", "java"]
- ["ImageJ Macro: MorpholibJ shape watershed", "watershed/activities/morpholibj_shape_watershed.ijm", "java"]

exercise_preface: |
  - Dealing with noise
    - Open [xy_8bit__few_separate_nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__few_separate_nuclei.tif)
    - There are 6 (partially visible) nuclei.
    - Apply the watershed algorithm to segment the image into 6 regions.
    - Hint: You will need to preprocess (invert and smooth) the image.

exercises:
  - ["ImageJ Macro: MorpholibJ: Dealing with noise", "watershed/exercises/morpholibj_watershed_noise.md"]

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .
    
    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:

external_links:
  - "[Wikipedia: Watershed image processing](https://en.wikipedia.org/wiki/Watershed_(image_processing))"
---

