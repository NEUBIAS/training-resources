---
title: Pixels calibration
layout: module

prerequisites:
  - "[Pixels](../pixels)"
  
objectives:
  - Understand that an pixel are related to a physical size.
  - Understand what pixels and voxels are.
  - Examine the values and indices of pixels in an image.

motivation: >
  For microscopy systems, we would like to relate the image dimensions to a physical size. 
  The relation between pixels and physical size is referred to as calibration. 
  Image calibration is dictated by acquisition and detection parameters such as magnification, camera detector size, sampling, etc, 
  and is  usually stored within the so-called image metadata. Before performing quantitative measurements, e.g. volume, area, ..., 
  you should make sure that the calibration has been set appropriately. 
   
concept_map: >
  graph TD
    Im("Image") -->|has many| P("Pixel/Voxel")
    Im --> |has| C("Calibration")
    P -->|has| Va("Value")
    P -->|has| I("Indices")
    P --> |has| RWC("Real world coordinate")
    C --> RWC
    I --> RWC

activity_preface: |


activities:
    - ["ImageJ GUI", "pixels_calibration/activities/pixels_calibration_imagejgui.md", "markdown"]

exercises:

assessment: >

  

exercises:

learn_next:

external_links:

---
