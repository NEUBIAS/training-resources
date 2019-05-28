---
title:     Image calibration
layout:    page
---

## Image calibration

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    pixel -> indices;
    pixel -> coordinates;
    indices -> calibration;
    calibration -> coordinates;
    calibration -> anisotropic [label="  can be"];
    image -> calibration [label="  can have"];
  }
'/>


### Activity: Explore image calibration

* Open image: xy_8bit__nuclei_noisy_different_intensity.tif
* Add image calibration
* Explore whether and how this affects image display and measurements (e.g. distance between two points)


### Activity: Explore anisotropic 3D image data

* Open image: xy_8bit_calibrated_anisotropic__mri_stack.tif
        * Appreciate that the pixels are anisotropic


### Formative assessment

True or false?

* Changing the image calibration changes the pixel values.
* Pixel coordinates depend on image calibration.


