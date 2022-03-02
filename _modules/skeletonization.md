---
title: Skeletonization
layout: module
tags: ["segmentation", "binarization"]
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Data types (unsigned 8-bit)](../datatypes)"
  - "[Binarization](../binarization)"
  - "[Image segmentation](../segmentation)"
  - "[Morphological filters](../filter_morphological)"

objectives:
  - "Apply a skeletonization algorithm to a binary image to view its internal skeleton"
  - "Count the number of branches and branch lengths to obtain morphological information from the image"
motivation: |
  For objects that contain protrusions, it can be helpful to look at the object's internal skeleton. This reveals the inner branches that make up the object. Measuring the number of branches and their lengths can provide useful morphological information of irregularly shaped objects with protrusions, such as glial cells. Skeletonization algorithms work by applying sequential erosions to remove pixels from the boundary of the objects to the center, stopping when the remaining structure is only one pixel wide.

concept_map: >
  graph TD
    BI("Binary image") --> S("Skeletonize")
    S --> SI("Skeleton image")
    SI --> M("Measure branch properties")

figure: /figures/skeletonization.png
figure_legend: Image before and after skeletonization.

activity_preface: |
  - Open the binary image [xy_8bit_glialcells.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_glialcells.tif).
  - Perform skeletonization.
  - Analyze branch properties in the two different cells.

activities:
  - ["ImageJ GUI", "skeletonization/activities/skeletonization_imagejgui.md", "markdown"]
  - ["ImageJ Macro", "skeletonization/activities/skeletonization_imagejmacro.ijm", "java"]
  - ["ImageJ Jython", "skeletonization/activities/skeletonization_imagej-jython.py", "python"]

exercise_preface: |
  Perform skeletonization and skeleton analysis in one of the following exercises:

exercises:
  - ["ImageJ GUI", "skeletonization/exercises/skeletonization_imagejgui.md", "markdown"]
  - ["ImageJ Macro", "skeletonization/exercises/skeletonization_imagejmacro.md", "java"]
  - ["ImageJ Jython", "skeletonization/exercises/skeletonization_imagej-Jython.md", "python"]

assessment: >

  ### True or False
    - Skeleton pixels never overlap with boundary pixels in the original binary image.
    - Branches in the skeleton can be more than 1 pixel thick.
    - The longest shortest path is the longest branch in the skeleton.

    > ## Solution
    >   - Skeleton pixels never overlap with boundary pixels in the original binary image. **True**
    >   - Branches in the skeleton can be more than 1 pixel thick. **False. They can be longer than 1 pixel, but the branch thickness is always 1 pixel.**
    - The longest shortest path is the longest branch in the skeleton. **False**
    {: .solution}

learn_next:

external_links:
  - "[Imagej.net: AnalyzeSkeleton](https://imagej.net/plugins/analyze-skeleton/)"
  - "[Imagej.net: Skeletonize3D](https://imagej.net/plugins/skeletonize3d)"

---
