---
title:     Volume slicing
layout:    module
prerequisites:
  - "edit this [Basic properties of images and pixels](../pixels)"
  - "edit this [Data types (unsigned 8-bit)](../datatypes)"
objectives:
  - "Describe the different dimensions image data can have."
  - "View and slice images in different dimensions."
motivation: |
  Apart from the X and Y dimensions, visible in the width and height of an image, image data can have additional dimensions. The most common additional dimensions include:
  the Z dimension, providing depth to image data,
  different channels, showing data recorded with different detectors or detector settings,
  the time dimension.
  When viewing the data, different dimensions can be included or excluded, to visualize different aspects of the data. Furthermore, multidimensional image data processes can be applied to one or more dimensions, depending on the needs. It is important to note that the different spatial dimensions are not necessarily isotropic. This means that the pixel sizes are different in X, Y, or Z. It is important to take this into account when viewing data or when applying image data analysis processes.

concept_map: >
  graph TD
    DM("Image data dimensions") --> S(Spatial dimensions)
    S --> X("X (width)")
    S --> Y("Y (height)")
    S --> Z("Z (depth)")
    DM --> T(Temporal dimension)
    DM --> C(Image channels)

figure: /figures/volume_slicing.png
figure_legend: Schematic representation of 2D, 3D, and 5D image data. 2D images are made up of tiny squares called pixels, whereas 3D images are made up of cubes called voxels. Pixels and voxels are not necessarily isotropic, as shown here by squares versus rectangles.

activity_preface: |
  - Open the multidimensional image [xyzc_8bit_beads_p_open.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif).
  - Use the sliders to inspect the different dimensions in this image. Which dimensions are present in this data? How can one turn on both channel simultaneously?
  - View the image using the 'Orthogonal views' function. Are the XYZ dimensions isotropic or anisotropic in this image?

activities:
  - ["ImageJ GUI", "volume_slicing/activities/volume_slicing_gui.md", "markdown"]
  - ["ImageJ Macro", "volume_slicing/activities/volume_slicing_macro.ijm", "IJ macro"]
  - ["ImageJ Jython", "volume_slicing/activities/volume_slicing_jython.py", "Jython"]

exercises:
  - ["ImageJ GUI", "volume_slicing/exercises/volume_slicing_gui.md"]
  - ["ImageJ Macro", "volume_slicing/exercises/volume_slicing_macro.md"]
  - ["ImageJ Jython", "volume_slicing/exercises/volume_slicing_jython.md"]

assessment: >
  ### True or False
    - Isotropic image data has voxels of equal XYZ dimensions.
    - Reslicing volumetric data is essentially similar to rotating a 3D object and viewing it from a different angle.

    > ## Solution
    >   - Isotropic image data has voxels of equal XYZ dimensions. **True**
        - Reslicing volumetric data is essentially similar to rotating a 3D object and viewing it from a different angle. **True**
        {: .solution}

learn_next:
  - "[Projections of 3D data](../projections)"
  - "[3D volume rendering]"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"
