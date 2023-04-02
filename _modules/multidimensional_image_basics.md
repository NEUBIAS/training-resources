---
title:     N-dimensional images
layout:    module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Spatial calibration](../spatial_calibration)"
objectives:
- "Explore and view the different dimensions image data can have."
motivation: |
  Apart from the X and Y dimensions, visible in the width and height of an image, image data can have additional dimensions. The most common additional dimensions include:
  - the Z dimension, providing depth to image data,
  - different channels, showing data recorded with different detectors or detector settings,
  - the time dimension.
  Viewing multi-dimensional data can be challenging, because a computer monitor can only render a (multi-color) 2D representation. Therefore, it is important to know how to visualize and navigate through multi-dimensional data.

concept_map: >
  graph TD
    XY("2D(XY)-image") --> ND("N-dimensional image")
    S("Z-slices") --> ND("N-dimensional image")
    C("Channels") --> ND("N-dimensional image")
    T("Time Points") --> ND("N-dimensional image")

figure: /figures/multi_dimensional_image.png
figure_legend: Schematic representation of 2D, 3D, and 5D image data. 2D images are made up of tiny squares called pixels, whereas 3D images are made up of cubes called voxels.

multiactivities:
  - ["multidimensional_images/multidimensional_images_act1.md", [["ImageJ GUI", "multidimensional_images/multidimensional_images_act1_imagejgui.md", "markdown"], ['Napari GUI/Python', multidimensional_images/multidimensional_images_act1_napari.md]]]
  - ["multidimensional_images/multidimensional_images_act2.md", [["ImageJ GUI", "multidimensional_images/multidimensional_images_act2_imagejgui.md", "markdown"], ['Napari GUI/Python', multidimensional_images/multidimensional_images_act2_napari.md]]]
  - ["multidimensional_images/multidimensional_images_act3.md", [["ImageJ GUI", "multidimensional_images/multidimensional_images_act3_imagejgui.md", "markdown"], ['Napari GUI/Python', multidimensional_images/multidimensional_images_act3_napari.md]]]

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
    2. Image data can have up to 5 dimensions.

    > ## Solution
    > 1. **True**
    > 4. **False** - While the dimensions X, Y, Z, channel and time are the most common dimensions, there is nothing that prevents an image from having additional dimensions. In medical imaging, additional dimensions can be used to hold information such as the age of a patient, or physiological parameters like heart rate. In astronomy, images of the universe may also have additional dimensions, such as light polarization.
    {: .solution}

learn_next:
  - "[Projections of 3D data](../projections)"
  - "[3D slicing](../volume_slicing)"
  - "[Volume viewer](../volume_viewer)"
---
