---
title: Digital image basics
layout: module

prerequisites:

objectives:
  - Understand that a digital image is typically stored as an N-dimensional array.
  - Understand that the array elements are called pixels (2D) or voxels (3D).
  - Examine the values and locations of pixels/voxels in an image.

motivation: >
  Digital images are a very important subset of the more general [mathematical definition](https://mathworld.wolfram.com/Image.html) of an image. The vast majority of available algorithms and visualisation tools operate on digital images and all (as far as we know) scientific microscopes output digital images. Thus, for microscopy based science, it is crucial to understand the basic properties of digitial images and how to effectively inspect their content.


concept_map: >
  graph TD
    Im("Digital image") --- A("N-D array")
    A --- E("Elements/Pixels/Voxels")
    A --- DT("Data type")
    A --- D("Dimensions")
    E --- V("Value")
    E --- I("Indices")

figure: /figures/pixels.jpg
figure_legend:  Digital image pixel array and gray-scale rendering. This array (image) has two dimensions with 21 x 21 elements (pixels). The pixel values (black numbers) can be addressed by their respective pixel indices (green numbers).

activity_preface: |
  - Open image: [xy_8bit__nuclei_noisy_different_intensity.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif)
  - Explore different ways to inspect pixel values and indices, e.g.,
    - Examine individual (or a range of) pixel values
    - Plot line profiles
    - Compute and plot pixel value histograms

activities:
  - ["ImageJ GUI", "pixels/activities/pixels_imagejgui.md", "markdown"]
  - ["MATLAB", "pixels/activities/pixels2D_matlab.m", "matlab"]
exercises:

assessment: >

  ### 2D image inspection
    Open image
    [xy_8bit__nuclei_noisy_different_intensity.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif).
    Hint: For certain exercises the inspection of the histogram will help
    1. What is the value of the pixel at the indices (x=20,y=20)?
    1. What is the highest value in the image?
    1. What is the most frequently occurring value in the image?
    1. Where is this pixel with the indices (x=0,y=0)? Why is this potentially confusing?
    1. How many pixels does this image have in the x direction?
    1. What is the highest pixel index in the x direction?
    1. If you were to rotate the image by 90 degrees, would it change the image histogram?

    > ## Solution
    > 1. 82
    > 1. 129
    > 1. 55
    > 1. Top left; normally x/y coordinate systems have their origin at the bottom left
    > 1. 59
    > 1. 58
    > 1. No, the gray value histogram is independent of the pixel locations
  {: .solution}

  ### 3D image inspection
    Open image: [xyz_8bit__mri_head.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mri_head.tif)
    1. What is the value of the voxel at the indices (x=93,y=124,z=13)?
    1. Which is the highest value in the image?

    > ## Solution
    > 1. 47
    > 1. 255
    {: .solution}

exercises:

learn_next:
   - "[Lookup tables](../lut)"
   - "[Spatial calibration](../spatial_calibration)"
   - "[Data types](../datatypes)"

external_links:
   - "[Wikipedia: Digital images](https://en.wikipedia.org/wiki/Digital_image)"
   - "[Images in ImageJ: ImagePlus](https://imagej.nih.gov/ij/developer/api/ij/ij/ImagePlus.html)"
   - "[Images in ImgLib2: Accessible](https://imagej.net/libs/imglib2/accessibles)"
   - "[Images in skimage: numpy arrays](https://scikit-image.org/docs/dev/user_guide/numpy_images.html)"
---
