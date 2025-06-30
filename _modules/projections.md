---
title: Projections
layout: module
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[N-dimensional images](../multidimensional_image_basics)"

objectives:
  - "Project multi-dimensional image data into lower dimensions"
  - "Understand the differences between projection modes such as max, sum, and mean"

motivation: |
  Viewing image data that has more than two dimensions is difficult, because computer monitors are 2-D. 
  Thus, it often is very useful to project the data into a 2-D representation. 
  Of course, doing such a projection will loose information. Thus, performing projections without compromising the scientific 
  integrity of the data is not easy and should only be done with a sufficient understanding of the various methods.

concept_map: >
  graph TD
    ND("N dimensional image") --> PM("Simple projection")
    PM -->|has| A("Axis")
    PM -->|has| M("Method: max, sum, ...")
    PM -->|creates| LD("N-1 dimensional image")

figure: /figures/projections.png
figure_legend: 

activity_preface: |
  - Open [xyz_16bit__spots.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif)
  - Project along the z axis
  - Compare maximum and sum projection
    - Understand that the data type of the sum projection may need to be adapted
  - Project along the x and y axis
  - Resample the x and y projections for correct appearance in physical space

  ![](/figures/projections_activity.png)

multiactivities:
  - ["projections/projections_act1.md", 
      [
        ["ImageJ GUI Reslice", "projections/projections_act1_imagejgui_reslice.md", "markdown"],
        ["ImageJ GUI CLIJ2", "projections/projections_act1_imagejgui_clij2.md", "markdown"],
        ["ImageJ GUI TransformJ", "projections/projections_act1_imagejgui_transformj.md", "markdown"],
        ["skimage napari", "projections/projections_act1_skimage_napari.py", "python"]
  ]]
  - ["projections/projections_act2.md", 
      [
        ["ImageJ GUI Reslice", "projections/projections_act2_imagejgui_reslice.md"],
        ["ImageJ GUI CLIJ2", "projections/projections_act2_imagejgui_clij2.md", "markdown"]
  ]]

assessment: >

  ### Fill in the blanks

    1. A projection ___ the number of dimensions in an image.
    1. The pixel values in a sum projection will typically be much ___ than in a mean projection.
    1. If you have an unsigned 8-bit image with dimensions x=10, y=10, z=5; the highest value that you can possibly get in a **maximum** projection along the **z** axis is ___?
    1. Same image as above, the highest value you could possibly get in a **sum** projection along the **z** axis is ___?
    1. Same image as above, the highest value you could possibly get in a **sum** projection along the **x** axis is ___?
    1. Same image as above, the highest value you could possibly get in a **mean** projection along the **y** axis is ___?

    > ## Solution
    >   1. decreases
    >   1. larger
    >   1. 255 (highest value in a unsigned 8-bit image)
    >   1. 5 * 255 = 1275
    >   1. 10 * 255 = 2550
    >   1. 10 * 255 / 10 = 255
    {: .solution}

  ### True or False
    1. Image projections are always along the z-axis.
    1. The data type of the projected image must be the same as the data type of the original image.
    
    > ## Solution
    >   1. **False**, you can project along any axis.
    >   1. **False**, in sum projections the pixel values are larger than in the original data and a different data type might 
    be needed to represent them. For maximum projections however the data type needs not be changed. 
    For mean projections it depends on the accuracy your science requires (decimal places need a floating point data type, 32-bit in IJ).
    {: .solution}

learn_next:
  - "Volume rendering (TODO)"

external_links:

---
