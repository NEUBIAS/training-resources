---
title:     Volume slicing
layout:    module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Spatial calibration](../spatial_calibration)"
objectives:
- "Create slice views of volumetric image data"
- "Master different ways of dealing with anisotropic voxels"

motivation: |
  Volumetric data is intrinsically difficult to visualise, especially on a 2D computer monitor. Various volume rendering techniques, including VR, exist, however for quantitative image inspection, where it is critical to access the gray value of individual voxels, extracting one 2-D slice of a volume is the method of choice. Thus, such volume slicing is implemented in almost all image analysis software packages. A conceptual challenge is that microscopes often produce anisotropic data, where the voxel spacing along the z-axis is typically larger than in the x and y axes. Thus, creating a slice, e.g., in the zy plane needs to be done with special care.


concept_map: >
  graph TD
    V["Volume data"] --> S("Slicing")
    V --- A["Anisotropic"]
    S --> M["2D image"]
    M -.- A 

figure: /figures/volume_slicing.png
figure_legend: "Volume slicing: Extracting 2-D slices from a 3-D volume, e.g. to be visualised on a computer monitor. Anisotropy: The measured data points have a different spacing in pixel vs. physical space, which poses a practical challenge for the rendering." 

multiactivities:
  - ["volume_slicing/volume_slicing_act1.md", [["ImageJ GUI", "volume_slicing/volume_slicing_act1_imagej-gui.md", "markdown"], ["ImageJ Macro", "volume_slicing/volume_slicing_act1_imagej-macro.ijm", "java"], ["ImageJ Jython", "volume_slicing/volume_slicing_act1_imagej-jython.py", "python"]]]

assessment: >

  ### Fill in the blanks

    1. A set of 2D \_\_\_\_ placed on top of each other form a 3D \_\_\_\_.
    2. An \_\_\_\_ voxel size can cause the image to appear \_\_\_\_ when viewing it at an angle.
    3. Rendering anisotropic voxels can be done in various ways, such as \_\_\_\_, \_\_\_\_, or \_\_\_\_.

    > ## Solution
    >   1. 2D **slices** placed on top of each other from a 3D **stack**.
    >   2. An **anisotropic** voxel size can cause the image to appear **deformed** when viewing at a certain angle.
    >   3. One can render anisotropic voxels, by (i) isotropic resampling, (ii) just showing them as a square anyway, (iii) showing them as a rectangle.
    {: .solution}

  ### True or False
    1. Isotropic image data has voxels of equal XYZ dimensions.
    2. Slicing is the process of sectioning the data, that has more than two dimensions, along defined axes and dimensions.
    3. Reslicing is a term used to indicate repeated slicing.

    > ## Solution
    > 1. **True**
    > 2. **True**
    > 3. **False** - Typically, the term reslicing refers to resampling volumetric data from a different direction, such that the resulting image stack is a rotated version of the original stack.
    {: .solution}

learn_next:
  - "[Projections of 3D data](../projections)"
  - "[Volume viewer](../volume_viewer)"

external_links:
  - "[ImageJ: Z-functions](https://imagej.net/imaging/z-functions)"
---


The word 'slice' is often used in different ways. The different 'layers' in the z-dimension are referred to as z-slices. Slicing (or subsetting) image data means that part of the image data is selected and 'sliced out' to form a new image. This can include selecting one or more dimensions, or just part of a dimension, for example selecting slice 6-12 of the Z-dimension. You can also rotate the data in one of the spatial dimensions and resample the data set to see that data from a different angle, which is sometimes referred to as 'reslicing'.
