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

  When viewing the data, different dimensions can be included or excluded, to visualize different aspects of the data. Furthermore, multidimensional image data processes can be applied to one or more dimensions. When doing so, it is important to keep in mind that the different spatial dimensions are not necessarily isotropic. This means that the pixel sizes can be different in X, Y, or Z.

concept_map: >
  graph TD
    ND("N-Dimensional image") --> S("Show on")
    S --> M("2D monitor")

figure: /figures/volume_slicing.png
figure_legend: Schematic representation of 2D, 3D, and 5D image data. 2D images are made up of tiny squares called pixels, whereas 3D images are made up of cubes called voxels. Pixels and voxels are not necessarily isotropic, as shown here by squares versus rectangles. In order to see a different part of the image data on a 2D monitor, the image has to be sliced and sometimes rotated.

activity_preface: |
  - GUI only: open the 3D image [xyz_8bit_sphere_calibrated.tif] (https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_sphere_calibrated.tif). Use the 'orthogonal views' options to view the data in XY, YZ, and XZ. What happens to this way of viewing the data when you turn off the calibration?
  - Open the multidimensional image [xyzc_8bit_beads_p_open.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif).
  - Use the sliders to inspect the different dimensions in this image. Which dimensions are present in this data? How can one turn on both channel simultaneously?
  - View the properties of this image. Are the XYZ dimensions isotropic or anisotropic in this image?
  - Subset the data such, that a new image is created that contains only the green bead.
  - Reslice the green bead, such that the bead is shown from the top. What happens when you tick or untick the 'avoid interpolation' box?

activities:
  - ["ImageJ GUI", "volume_slicing/activities/volume_slicing_gui.md", "markdown"]
  - ["ImageJ Macro", "volume_slicing/activities/volume_slicing_macro.ijm", "IJ macro"]
  - ["ImageJ Jython", "volume_slicing/activities/volume_slicing_jython.py", "Jython"]

exercises:
  - ["ImageJ GUI", "volume_slicing/exercises/volume_slicing_gui.md"]
  - ["ImageJ Macro", "volume_slicing/exercises/volume_slicing_macro.md"]
  - ["ImageJ Jython", "volume_slicing/exercises/volume_slicing_jython.md"]

assessment: >

  ### Fill in the blanks

    - 2D ______ placed on top of each other form a 3D _____.

    > ## Solution
    >   - 2D **slices** placed on top of each other from a 3D **stack**.
    {: .solution}

  ### Choose the correct answer
    - In a non-calibrated image, a spherical object will appear **compressed/round/stretched** in the z-dimension when the sampling in Z is lower than in XY.
    - In a calibrated image, a spherical object will appear **compressed/round/stretched** in the z-dimension when the sampling in Z is lower than in XY.

    > ## Solution
    > - In a non-calibrated image, a spherical object will appear **compressed** in the z-dimension when the sampling in Z is lower than in XY.
    > - In a calibrated image, a spherical object will appear **round** in the z-dimension when the sampling in Z is lower than in XY. However, keep in mind that this may depend on the settings of the software that you are using to view the data. In ImageJ, using the 'orthogonal views' command will scale and interpolate the data according to the calibration, thereby stretching the z-dimension to match with the true proportions of the object.
    {: .solution}

  ### True or False
    - Isotropic image data has voxels of equal XYZ dimensions.
    - Slicing is the process in which an image is divided in smaller images.
    - Reslicing is a term used to indicate repeated slicing.

    > ## Solution
    > - Isotropic image data has voxels of equal XYZ dimensions. **True**
    > - Slicing is the process in which a multidimensional image is divided in smaller images. **True**
    > - Reslicing is a term used to indicate repeated slicing. **False. Typically, the term reslicing refers to resampling volumetric data from a different direction, such that the resulting image stack is a rotated version of the original stack.**
    {: .solution}

learn_next:
  - "[Projections of 3D data](../projections)"
  - "[Volume viewer](../volume_viewer)"
---


The word 'slice' is often used in different ways. The different 'layers' in the z-dimension are referred to as z-slices. Slicing (or subsetting) image data means that part of the image data is selected and 'sliced out' to form a new image. This can include selecting one or more dimensions, or just part of a dimension, for example selecting slice 6-12 of the Z-dimension. You can also rotate the data in one of the spatial dimensions and resample the data set to see that data from a different angle, which is sometimes referred to as 'reslicing'.
