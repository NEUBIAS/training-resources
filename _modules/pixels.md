---
title: Pixels
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
    Im("Image") -->|has many| P("Pixel")
    P -->|has| Va("Value")
    P -->|has| I("Indices")
    P -->|aka| Vo("Voxel")

figure: /figures/pixels.png
figure_legend:

activity_preface: |
  - Open image: xy_8bit__nuclei_noisy_different_intensity.tif
  - Explore different ways to inspect pixel values and indices, e.g.,
    - Examine individual (or a range of) pixel values
    - Plot line profiles
    - Compute and plot pixel value histograms

activities:
#  "ImageJ GUI": "pixels/activities/pixels_imagejgui.md"
#  "ImageJ Macro": "pixels/activities/pixels_ijmacro.md"
#  "Jython": "pixels/activities/pixels_jython.md"
#  "MATLAB": "pixels/activities/pixels_matlab.md"

exercises_preface: |

  - Inspect a 2D image: xy_8bit__nuclei_noisy_different_intensity.tif¶
  1. What is the value of the pixel at the indices (20,20)?
  1. What is the highest value in the image?
  1. What is the most frequently occuring value in the image?
  1. What are the lowest pixel indices (?,?) and where is this pixel?
  1. How many pixels does this image have in the horizontal direction?
  1. What is the highest pixel index in the horizontal direction?
  1. If you were to rotate the image by 90 degrees, would it change the image histogram?
    
  > ## Solution
  > 1. TODO
  {: .solution}

  - Inspect a 3D image: TODO¶
  1. What is the value of the voxel at the indices (100,100,100)?
  1. Whats is the highest value in the image?
  1. What is the most frequently occuring value in the image?
  1. Where is the voxel with the lowest indices and what are those indices (?,?,?) ?¶
  
  > ## Solution
  > 1. TODO
  {: .solution}
  

exercises:

learn_next:
  - "[Image display](image_display)"
external_links:

---
