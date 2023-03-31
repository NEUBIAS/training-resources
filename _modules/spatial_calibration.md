---
title:  Spatial calibration
layout: module

prerequisites:
  - "[Basics properties of images and pixels](../pixels)"

objectives:
  - Understand that a pixel index is related to a physical coordinate.
  - Understand that a spatial calibration allows for physical size measurements.

motivation: >
  We would like to relate the image dimensions to a physical size. 
  The relation between pixels and physical size is referred to as spatial calibration. 
  Image calibration is dictated by acquisition and detection parameters of a microscope, such as magnification, 
  camera detector size, sampling, etc, and is  usually stored within the so-called image metadata. 
  Before performing quantitative measurements, e.g. volume, area, ...,
  you should make sure that the spatial calibration has been set appropriately.

concept_map: >
  graph TD
    Im("Image") -->|has many| P("Pixel/Voxel")
    Im --> |has| C("Calibration")
    P -->|has| Va("Value")
    P -->|has| I("Indices")
    P --> |has| RWC("Real world coordinate")
    C --> RWC
    I --> RWC

figure: /figures/spatial_calibration.png
figure_legend: Spatial calibration and size measurements

multiactivities:
  - ["spatial_calibration/activities/spatial_calibration.md", [["ImageJ GUI", "spatial_calibration/activities/spatial_calibration_imagejgui.md", "markdown"], ["skimage napari", "spatial_calibration/activities/spatial_calibration_skimage_napari.py", "python"]]]

exercises:
    - ["ImageJ GUI", "spatial_calibration/exercises/spatial_calibration_imagejgui.md"]
    
assessment: |
    ### Answer these questions

    - Given a 2D image with `pixel height` = `pixel width` = `dxy` = `0.13 micrometer`, what distance do the pixels at the (x,y) indices (10,10) and (9,21) have in micrometer units?
    - Given a 3D image with `dx` = `dy` = `0.13 micrometer` and `dz` = `1 micrometer`, what is the calibrated (micrometer units) distance of two pixels at the indices `(10,10,0)` and `(9,21,3)`?
    - What is the calibrated (micrometer units) area covered by 10 pixels, given a spatial calibration of `dx` = `dy` = `0.13 micrometer`?
    - What is the calibrated (micrometer units) volume covered by 10 voxels, given a spatial calibration of `dx` = `dy` = `0.13 micrometer` and `dz` = `1 micrometer`?
    
    > ## Solution
    >   - `sqrt( (x0*dxy-x1*dxy)^2 + (y0*dxy-y1*dxy)^2 )` = `sqrt( (x0-x1)^2 + (y0-y1)^2 ) * dxy` = `sqrt( (10-9)^2 + (10-21)^2 ) * 0.13` = `11.04536 * 0.13 micrometer = 1.435897 micrometer`. The fact that one can separate out the isotropic calibration `dxy` in the formula allows one to perform measurements in pixel units and convert the results to calibrated units later, by means of multiplication with `dxy`.
    >   - `sqrt( (x0*dx-x1*dx)^2 + (y0*dy-y1*dy)^2 + (z0*dz-z1*dz)^2  )` = `sqrt( (10*0.13-9*0.13)^2 + (10*0.13-21*0.13)^2 + (0*1.0-3*1.0)^2 ) micrometer` = `3.325928 micrometer`. Unfortunately, in an anisotropic 3D image one cannot separate out a calibration factor from the formula, making life more difficult.
    >   - `10 * 0.13 micrometer * 0.13 micrometer` = `10 * 0.0169 micrometer square` = `0.169 micrometer square`
    >   - `10 * 0.13 micrometer * 0.13 micrometer * 1.0 micrometer` = `10 * 0.0169 micrometer cube` = `0.169 micrometer cube`. This shows that measuring volumes in 3D can be done first in voxel units, as the calibration factor can easily taken into account later (in contrast to the distance measurements). Thus, somewhat surprisingly, is in practice easier to measure volumes than distances in 3D.
    {: .solution}

learn_next:

external_links:
  - "[Wikipedia: pixels](https://en.wikipedia.org/wiki/Pixel)"
  - "[A pixel is not a little square](http://alvyray.com/Memos/CG/Microsoft/6_pixel.pdf)"
---

## Isotropy

One speaks of **isotropic sampling** if the pixels have the same extent in all dimensions (2D or 3D).

While microscopy images typically are isotropic in 2D they are typically **anisotropic** in 3D with coarser sampling in the z-direction. 

It is very convenient for image analysis if pixels are isotropic, thus one sometimes resamples the image during image analysis such that they become isotropic.
 
