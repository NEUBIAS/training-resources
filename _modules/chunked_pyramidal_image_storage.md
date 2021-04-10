---
title:     Chunked pyramidal image storage
layout:    module

prerequisites:
  - "[Basic properties of images and pixels](../pixels)"

objectives:
  - Understand the concept of chunked pyramidal image storage and its relevance for big image data analysis and visualisation
  - Store an image in a chunked pyramidal format and inspect its layout on disk

motivation: >
  Microscopy modalities such as light sheet or volume EM can generate images in the TB range. For such images, it is not efficient/ possible to load the whole image into RAM for analysis or visualisation. Thus it is important to store the image such that only the parts ("chunks") can be efficiently loaded that are currently being displayed or analysed. In addition, storing several versions of the image at different ("pyramidal") resolution levels ("google maps style") is advantageous for smooth browsing of the image data.

concept_map: >
  graph TD
    I("Image") --> R("Resolution levels")
    R --> C("Chunks")

figure: figures/global_background_correction.png
figure_legend: TODO: Image before and after background correction

activity_preface: |
  - TODO: Open image [xy_16bit__nuclei_high_dynamic_range_with_offset](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__nuclei_high_dynamic_range_with_offset.tif)
  - Save image in a pyramidal chunked image data format
  - Inspect the image on disk (identify the resolution levels and chunks)

activities:
    - IDEA: inspect an image on disk and determine the number of resolution levels and the chunk size
    - IDEA: store an image with different amount of resolution levels and check the file size
	- ["TODO: ImageJ Macro & GUI", "global_background_correction/activities/global_background_correction.ijm", "java"]

exercises:
    - ["TODO: ImageJ Macro & GUI", "global_background_correction/exercises/global_background_correction.md"]

assessment: |
    ### True or false? 
      1. The size of an image increases by a factor of XYZ when saving additional resolution levels in 2D/3D.
      2. More (i.e. smaller) chunks will increase the size of the image on disk.
      3. The optimal chunk size....
      4. Downsampling by powers of 2 or 3.....
        
    > ## Solution
    >  1. TODO: The datatype is irrelevant for background subtraction. **FALSE**
    >  2. TODO: Background subtraction using a unsigned integer image will always lead to a positive valued background. **TRUE**
    >  3. TODO: Global background subtraction is important for ratiometric computations. **TRUE**
    >  4. TODO: Global background subtraction affects differences in intensities. **FALSE**       
    {: .solution}

learn_next:


external_links:
---