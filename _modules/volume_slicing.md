---
title:     Slice viewing
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
  Viewing such multi-dimensional data is challenging, because a computer monitor can only render a (multi-color) 2D representation of such data. Thus it is important to learn how to efficiently visualise subsets ("slices") of such high-dimensional data.

concept_map: >
  graph TD
    ND("N-dimensional image") --> S("Slice")
    S --> M("2D image")

figure: /figures/volume_slicing.png
figure_legend: Schematic representation of 2D, 3D, and 5D image data. 2D images are made up of tiny squares called pixels, whereas 3D images are made up of cubes called voxels. Pixels and voxels are not necessarily isotropic, as shown here by squares versus rectangles. In order to see a different part of the image data on a 2D monitor, the image has to be sliced and sometimes rotated.

multiactivities:
  - ["volume_slicing/volume_slicing_act1.md", [["ImageJ GUI", "volume_slicing/volume_slicing_act1_imagejgui.md", "markdown"], ["ImageJ Macro", "volume_slicing/volume_slicing_act1_imagejmacro.ijm", "java"], ["ImageJ Python", "volume_slicing/volume_slicing_act1_imagejpython.py", "python"]]]
  - ["volume_slicing/volume_slicing_act2.md", [["ImageJ GUI", "volume_slicing/volume_slicing_act2_imagejgui.md", "markdown"], ["ImageJ Macro", "volume_slicing/volume_slicing_act2_imagejmacro.ijm", "java"], ["ImageJ Python", "volume_slicing/volume_slicing_act2_imagejpython.py", "python"]]]

assessment: >

  ### Fill in the blanks

    1. A set of 2D \_\_\_\_ placed on top of each other form a 3D \_\_\_\_.
    2. An \_\_\_\_ voxel size can cause the image to appear \_\_\_\_ when viewing it at an angle.

    > ## Solution
    >   1. 2D **slices** placed on top of each other from a 3D **stack**.
    >   2. An **anisotropic** voxel size can cause the image to appear **deformed** when viewing at a certain angle.
    {: .solution}

  ### True or False
    1. Isotropic image data has voxels of equal XYZ dimensions.
    2. Slicing is the process of sectioning the data, that has more than two dimensions, along defined axes and dimensions.
    3. Reslicing is a term used to indicate repeated slicing.
    4. Images can have 5 dimensions.

    > ## Solution
    > 1. **True**
    > 2. **True**
    > 3. **False** - Typically, the term reslicing refers to resampling volumetric data from a different direction, such that the resulting image stack is a rotated version of the original stack.
    > 4. **True** - If we denote width by `x`, height by `y`, depth by `z`, time by `t` and channel by `c`, we could have images with dimensions such as: [`xy` -> 2D], [`xyz` -> 3D, `xyt` -> 3D: 2D time-lapse, `xyc` -> 3D: 2D multi-channel], or [`xyzt` -> 4D: 3D time-lapse, `xyzc` -> 4D: 3D multi-channel], or [`xyztc` -> 5D: 3D time-lapse  multi-channel]
    {: .solution}

learn_next:
  - "[Projections of 3D data](../projections)"
  - "[Volume viewer](../volume_viewer)"

external_links:
  - "[ImageJ z-functions](https://imagej.net/imaging/z-functions)"
---


The word 'slice' is often used in different ways. The different 'layers' in the z-dimension are referred to as z-slices. Slicing (or subsetting) image data means that part of the image data is selected and 'sliced out' to form a new image. This can include selecting one or more dimensions, or just part of a dimension, for example selecting slice 6-12 of the Z-dimension. You can also rotate the data in one of the spatial dimensions and resample the data set to see that data from a different angle, which is sometimes referred to as 'reslicing'.
