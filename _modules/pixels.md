---
title: Basics properties of images and pixels
layout: module

prerequisites:

objectives:
  - Understand that an image is composed of pixels.
  - Understand what pixels and voxels are.
  - Examine the values and indices of pixels in an image.

motivation: >
  Although the technical [definition](https://mathworld.wolfram.com/Image.html) an image is more general, in practice images are very often represented as an array of pixels (voxels). Pixel stands for "picture element". In 3-D, a pixel is sometimes also called a voxel, which stands for "volume element". For image analysis it is crucial to know how to examine the pixels (voxels) in an image.

concept_map: >
  graph TD
    Im("Image") -->|has many| P("Pixel/Voxel")
    P -->|has| Va("Value")
    P -->|has| I("Indices")

figure: /figures/pixels_2.png
figure_legend:

activity_preface: |
  - Open image: [xy_8bit__nuclei_noisy_different_intensity.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif)
  - Explore different ways to inspect pixel values and indices, e.g.,
    - Examine individual (or a range of) pixel values
    - Plot line profiles
    - Compute and plot pixel value histograms

activities:
  - ["ImageJ GUI", "pixels/activities/pixels_imagejgui.md", "markdown"]

exercises:

assessment: >

  ### 2D image inspection
    Open image 
    [xy_8bit__nuclei_noisy_different_intensity.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif).
    Hint: For certain exercises the inspection of the histogram will help
    1. What is the value of the pixel at the indices (20,20)?
    1. What is the highest value in the image?
    1. What is the most frequently occuring value in the image?
    1. Where is this pixel with the indices (0,0)? Why is this potentially confusing?
    1. How many pixels does this image have in the horizontal direction?
    1. What is the highest pixel index in the horizontal direction?
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
    1. What is the value of the voxel at the indices (93,124,13)?
    1. Whats is the highest value in the image?
    
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

---
