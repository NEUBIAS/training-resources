---
title: Thresholding
layout: module
tags: ["segmentation", "binarization"]
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[Data types](../datatypes)"
  - "[Segmentation](../segmentation)"
objectives:
  - "Describe the relationship between an intensity image and a derived binary image"
  - "Apply threshold to segment an image into foreground and background regions"
motivation: |
  One strategy to detect objects or specific regions in images is to first distinguish so-called background pixels,
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
figure_legend: Image before and after applying a threshold of 73 gray values.

multiactivities:
  - ["binarization/binarization_act1.md", [["ImageJ GUI", "binarization/binarization_act1_imagejgui.md"], ["ImageJ Macro", "binarization/binarization_act1_imagejmacro.ijm"], ["ImageJ Jython", "binarization/binarization_act1_jython.py"], ["skimage napari", "binarization/binarization_act1_skimage_napari.py", "python"],["Galaxy", "binarization/binarization_act1_galaxy.md"]]]
  - ["binarization/binarization_act2.md", [["ImageJ GUI", "binarization/binarization_act2_imagejgui.md"], ["ImageJ Macro", "binarization/binarization_act2_imagejmacro.ijm"], ["ImageJ Jython", "binarization/binarization_act2_jython.py"], ["ImageJ Jython + input parameters", "binarization/binarization_act2_jython_inputparameters.py"], ["skimage napari", "binarization/binarization_act2_skimage_napari.py"],["Galaxy", "binarization/binarization_act2_galaxy.md"]]]
  - ["binarization/binarization_act3.md", [["ImageJ GUI", "binarization/binarization_act3_imagejgui.md"]]]


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
  - "[Automatic thresholding](../auto_threshold)"
  - "[Connected component labeling](../connected_components)"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"

---
A common algorithm for binarization is thresholding. A threshold value `t` is chosen, either manually or automatically,
and all pixels with intensities below `t` are set to 0, whereas pixels with intensities `>= t` are set to the value for the foreground.
Depending on the software the foreground value can be different (e.g. 1 in MATLAB or 255 in ImageJ). At any pixel `(x,y)`:

`p_im(x,y) < t` `->` `p_bin(x,y) = 0`

`p_im(x,y) >= t` `->` `p_bin(x,y) = 1`

where, p_im and p_bin are the intensity and binary images respectively.

It is also possible to define an interval of threshold values, i.e. a lower and upper threshold value. Pixels with intensity values
within this interval belong to the foreground and vice versa.
