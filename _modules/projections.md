---
title: Projections
layout: module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "Volume slicing (TODO)"

objectives:
  - "Project multi-dimensional image data into lower dimensions"
  - "Understand the differences between projection modes such as max, sum, and mean"

motivation: |
  Viewing image data that has more than two dimensions is difficult, because computer monitors are 2-D. Thus, it often is very useful to project the data into a 2-D representation. Of course, doing such a projection will loose information. Thus, performinig projections without compromising the scientific integrity of the data is not easy and should be only done with a sufficient understanding of the various methods.

concept_map: >
  graph TD
    ND("N dimensional image") --> PM("Projection")
    PM -->|has| A("Axis")
    PM -->|has| M("Method: max, sum, ...")
    PM -->|creates| LD("N-1 dimensional image")

figure: /figures/projections.png
figure_legend: 

activity_preface: |
  - Open [xyz_16bit__spots.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif)
  - Project along the z axis
  - Compare maximum and sum projection
  - Project along the x and y axis
  - Resample the x and y projections for correct appearance in physical space

  ![](/figures/projections_activity.png)

activities:
  - ["ImageJ GUI", "projections/activities/projections_imagejgui.md", "markdown"]

exercises:
  - ["ImageJ GUI", "projections/exercises/projections_imagejgui.md"]

assessment: >

  ### Fill in the blanks

    1. A projection ___ the number of dimensions in an image.
    1. The pixel values in a sum projection will typically be much ___ than in a mean projection.

    > ## Solution
    >   1. **decreases**
    >   2. **larger**
    {: .solution}

  ### True or False
    1. Image projections are always along the z-axis.
    1. The data type of the projected image must be the same as the data type of the original image.
    
    > ## Solution
    >   1. **False** You can project along any axis.
    >   1. **False** In sum projections the pixel values are larger than in the original data and a different data type might be needed to represent them. For maximum projections however the data type needs not be changed. For mean projections it depends on the accuracy your science requires (decimal places need a floating point data type).
    {: .solution}

learn_next:
  - "Volume rendering (TODO)"

external_links:

---
