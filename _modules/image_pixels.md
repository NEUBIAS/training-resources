---
title:     Image pixels 
layout:    page
---

# Pixels

## Concept map

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    image -> pixel [label="  has many"];
    pixel -> value;
    pixel -> indices;
    pixel -> voxel [label="  3D"];
    pixel -> size [label="  can have"]
  }
'/>

## Activity: Explore pixel values and indices

* Open image: xy_8bit__nuclei_noisy_different_intensity.tif
* Explore different ways to inspect pixel values and indices
* Check where the lowest pixel indices are in the displayed image:
        * Most commonly: Upper left corner, which is different to conventional coordinate systems.

## Activity: Explore image calibration

* Open image: xyz_8bit_calibrated_anisotropic__mri_head.tif
* Check the calibration of this image
* Explore how image calibration affects spatial measurements, e.g.,
  * Measure the distance between two pixels in the image
  * Measure the size of an image region
* Appreciate that image calibration might be neccessary, e.g.
  * 3D distance measurements
* Appreciate that image calibration can be confusing, e.g.
  * not consistently used in image filter parameter specification

## Formative assessment

True or false?

* The lowest pixel index of a 2D image always is `[1,1]`.
* When looking at a 2D image, the lowest pixel indices are always in the lower left corner.

## Learn next

- display.md
