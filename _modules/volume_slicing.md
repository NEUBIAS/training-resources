---
title:     Volume slicing
layout:    module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Data types (unsigned 8-bit)](../datatypes)"
objectives:
- "Describe the different dimensions image data can have."
- "View and slice images in different dimensions."
motivation: |
  One strategy to detect objects or specific regions in images is to first distinguish so-called background pixels,
  which do not contain objects or interesting regions,  from foreground pixels, which mark the areas of interest.
  This process is called **two class semantic segmentation** and is often referred to as **image binarization**.
  The foreground regions can then be further processed, e.g to detect objects or perform intensity measurements.

concept_map: >
  graph TD
    PV("Pixel values") --> BA(Binarization algorithm)
    BA --> BPV("Binarized pixel values")
    BPV --> BG("Background (0)")
    BPV --> FG("Foreground (1)")

figure: /figures/binarization.png
figure_legend: Images before and after binarization

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
Depending on the software the foreground value can be different (e.g. 1 in MATLAB or 255 in ImageJ). At any pixel (x,y):

`p_im(x,y) < t` -> `p_bin(x,y) = 0`

`p_im(x,y) >= t` -> `p_bin(x,y) = 1`

where, p_im and p_bin are the intensity and binary images respectively.

It is also possible to define an interval of threshold values, i.e. a lower and upper threshold value. Pixels with intensity values
within this interval belong to the foreground and vice versa.
