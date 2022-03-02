---
title: Skeletonization
layout: module
tags: ["segmentation", "binarization"]
prerequisites:
  -"[Basic properties of images and pixels](../pixels)"
  -"[Data types (unsigned 8-bit)](../datatypes)"
  -"[Binarization](../binarization)"
  -"[Image segmentation](../segmentation)"
  -"[Morphological filters](../filter_morphological)"
  -
objectives:
  - "Apply a skeletonization algorithm to a binary image to view its internal skeleton"
  - "Count the number of branches and branch lengths to obtain morphological information from the image"
motivation: |
  For objects that contain protrusions, it can be helpful to look at the object's internal skeleton. This reveals the inner branches that make up the object. Measuring the number of branches and their lengths can provide useful morphological information of irregularly shaped objects with protrusions, such as glial cells. Skeletonization algorithms work by applying sequential erosions to remove pixels from the boundary of the objects to the center, stopping when  One strategy to detect objects or specific regions in images is to first distinguish so-called background pixels,
  which do not contain objects or interesting regions from foreground pixels, which mark the areas of interest.
  This process is called **two class semantic segmentation** and is often referred to as **image binarization**.
  The foreground regions can then be further processed, e.g. to detect objects or perform intensity measurements.

concept_map: >
  graph TD
    I("Image") --> T("Threshold")
    T --> BI("Binary image / Binary mask")
    BI --- BG("Background pixels (false, 0)")
    BI --- FG("Foreground pixels (true, 1, 255)")

figure: /figures/binarization.png
figure_legend: Image before and after binarization

activity_preface: |
  - Open the binary image [xy_8bit_binary__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei.tif).
  - Discuss the image data type and the pixel values.
  - Open the image [xy_8bit__two_cells.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif) and binarize it by applying a manually defined threshold.

activities:
  - ["ImageJ GUI", "binarization/activities/binarization_imagejgui.md", "markdown"]
  - ["ImageJ Macro", "binarization/activities/binarization_imagejmacro.ijm", "java"]
  - ["ImageJ Jython", "binarization/activities/binarization_jython.py", "python"]
  - ["MATLAB", "binarization/activities/binarization_matlab.m", "matlab"]
  - ["KNIME", "binarization/activities/binarization_knime.md", "markdown"]
  - ["Python", "binarization/activities/binarization.py", "python"]

exercise_preface: |
  Perform one of the following exercises.

exercises:
  - ["ImageJ GUI", "binarization/exercises/binarization_imagejgui.md"]
  - ["ImageJ Macro", "binarization/exercises/binarization_imagejmacro.md"]
  - ["ImageJ Jython", "binarization/exercises/binarization_jython.md"]

assessment: >

  ### Fill in the blanks

    - Pixels in a binary image can have maximally ___ different values.
    - If the threshold is larger than the maximal pixel value in the intensity image, all pixels in the binary image have a value of ___.

    > ## Solution
    >   - Pixels in a binary image can have maximally **2** different values.
    >   - If the threshold is larger than the maximal pixel value in the intensity image,
    > all pixels in the binary image have a value of **0**.
    {: .solution}

  ### True or False
    - There is only one correct threshold value in order to convert an intensity image into a binary image.
    - Binary images are always unsigned 8-bit where the foreground is 255.

    > ## Solution
    >   - There is only one correct threshold value in order to convert an intensity image into a binary image. **False**
    >   -  Binary images are always unsigned 8-bit where the foreground is 255. **False**
    {: .solution}

learn_next:
  - "[Automatic threshold for binarization](../auto_threshold)"
  - "[Finding objects in a binary image](../connected_components)"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"

---
#### Image thresholding
A common algorithm for binarization is thresholding. A threshold value `t` is chosen, either manually or automatically,
and all pixels with intensities below `t` are set to 0, whereas pixels with intensities `>= t` are set to the value for the foreground.
Depending on the software the foreground value can be different (e.g. 1 in MATLAB or 255 in ImageJ). At any pixel `(x,y)`:

`p_im(x,y) < t` `->` `p_bin(x,y) = 0`

`p_im(x,y) >= t` `->` `p_bin(x,y) = 1`

where, p_im and p_bin are the intensity and binary images respectively.

It is also possible to define an interval of threshold values, i.e. a lower and upper threshold value. Pixels with intensity values
within this interval belong to the foreground and vice versa.
