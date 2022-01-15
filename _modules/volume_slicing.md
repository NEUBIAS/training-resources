---
title:     Volume slicing
layout:    module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Spatial calibration](../spatial_calibration)"
objectives:
- "Describe the different dimensions image data can have."
- "View and slice images in different dimensions."
motivation: |
  Apart from the X and Y dimensions, visible in the width and height of an image, image data can have additional dimensions. The most common additional dimensions include:
  - the Z dimension, providing depth to image data,
  - different channels, showing data recorded with different detectors or detector settings,
  - the time dimension.
  When viewing the data, different dimensions can be included or excluded, to visualize different aspects of the data. Furthermore, multidimensional image data processes can be applied to one or more dimensions, depending on the needs. It is important to note that the different spatial dimensions are not necessarily isotropic. This means that the pixel sizes are different in X, Y, or Z. It is important to take this into account when viewing data or when applying image data analysis processes.

concept_map: >
  graph TD
    DM("Image data dimensions") --> S("Spatial dimensions")
    S --> X("X (width)")
    S --> Y("Y (height)")
    S --> Z("Z (depth)")
    DM --> T("Temporal dimension")
    DM --> C("Image channels")

figure: /figures/volume_slicing.png
figure_legend: Schematic representation of 2D, 3D, and 5D image data. 2D images are made up of tiny squares called pixels, whereas 3D images are made up of cubes called voxels. Pixels and voxels are not necessarily isotropic, as shown here by squares versus rectangles.

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
