---
title: Digital image basics
layout: module
permalink: /training-resources/pixels/
prerequisites:

objectives:
  - Understand that a digital image is typically stored as an N-dimensional array.
  - Learn that the image array elements are called pixels (2D) or voxels (3D).
  - Examine the values and locations of pixels/voxels in an image.

motivation: >
  Digital images are a very important subset of the more general [mathematical definition](https://mathworld.wolfram.com/Image.html) of an image. The vast majority of available algorithms and visualisation tools operate on digital images and all (as far as we know) scientific microscopes output digital images. Thus, for microscopy based science, it is crucial to understand the basic properties of digitial images and how to effectively inspect their content.


concept_map: >
  graph TD
    Im("Digital image") --- A("N-D array")
    A --- E("Elements/Pixels/Voxels")
    A --- DT("Data type")
    A --- D("Shape/Size/Dimensions")
    E --- V("Value")
    E --- I("Indices")

figure: /figures/pixels.jpg
figure_legend:  Digital image pixel array and gray-scale rendering. This array (image) has two dimensions with 21 x 21 elements (pixels). The pixel values (black numbers) can be addressed by their respective pixel indices (green numbers).


multiactivities:
  - ["pixels/pixels_act1.md", [["ImageJ GUI", "pixels/pixels_act1_imagejgui.md"], ["skimage napari", "pixels/pixels_act1_skimage_napari.py"], ["MATLAB", "pixels/pixels_act1_matlab.m"]]]
  - ["pixels/collagen_inspection.md", [["ImageJ GUI", "pixels/collagen_inspection_imagejgui.md"]]]
  
assessment: >

  ### 2-D image inspection
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

  ### 3-D image inspection
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
   - "[N-dimensional images](../multidimensional_image_basics)"
   - "[Data types](../datatypes)"

external_links:
   - "[Wikipedia: Digital images](https://en.wikipedia.org/wiki/Digital_image)"
   - "[Images in ImageJ: ImagePlus](https://imagej.nih.gov/ij/developer/api/ij/ij/ImagePlus.html)"
   - "[Images in ImgLib2: Accessible](https://imagej.net/libs/imglib2/accessibles)"
   - "[Images in skimage: numpy arrays](https://scikit-image.org/docs/dev/user_guide/numpy_images.html)"
---

### Digital image dimensions

There are several ways to describe the size of a digital image. For example, the following sentences describe the same image.

- The image has 2 dimensions, the length of dimension 0 is 200 and the length of dimension 1 is 100.
- The image has 2 dimensions, the length of dimension 1 is 200 and the length of dimension 2 is 100.
- The image has a size/shape of (200, 100).
- The image has 200 x 100 pixels.

Note that "images" in bioimaging can also have more than two dimensions and one typically specifies how to map those dimensions to the physical space (x,y,z, and t). For example, if you acquire a 2-D movie with 100 time points and each movie frame consisting of 256 x 256 pixels it is quite common to represent this as a 3-D array with a shape of ( 256, 256, 100 ) accompanied with metadata such as ( ("x", 100 nm), ("y", 100 nm), ("t", 1 s) ); check out the module on [spatial calibration](../spatial_calibration) for more details on this.

