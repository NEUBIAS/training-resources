---
title: Pixels
layout: module

prerequisites:

objectives:
  - Examine the values of pixels in an image.

motivation: >
  Images are very often composed of pixels. Pixel stands for "picture element". In 3-D, a pixel is sometimes also called a voxel, which stands for "volume element".
  To analyse images it is very important to know how to examine the pixels (voxels) in an image.

concept_map: >
  graph TD
    Im("Image") -->|has many| P("Pixel")
    P -->|has| V("Value")
    P -->|has| I("Indices")
    P -->|aka| V("Voxel")
    P -->|can have| S("Size")

figure: /figures/pixels.png
figure_legend:

activity_preface: >

  Explore the values, indices (and sizes) of pixels in an image.

activities:
  "ImageJ GUI": "pixels/activities/pixels_imagejgui.md"
#  "ImageJ Macro": "pixels/activities/pixels_ijmacro.md"
#  "Jython": "pixels/activities/pixels_jython.md"
#  "MATLAB": "pixels/activities/pixels_matlab.md"

exercises_preface: >
  True or false?
  * The lowest pixel index of a 2D image always is `[1,1]`.
  * When looking at a 2D image, the lowest pixel indices are always in the lower left corner.

exercises:
#  "ImageJ GUI": "pixels/exercises/pixels_imagejgui.md"
#  "ImageJ Macro": "pixels/exercises/pixels_imagejmacro.md"
#  "Jython": "pixels/exercises/pixels_jython.md"
#  "MATLAB": "pixels/exercises/pixels_matlab.md"

learn_next:
  - "[Image display](image_display)"
external_links:

---
