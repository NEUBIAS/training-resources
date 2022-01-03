---
title:     Image file formats     
layout:    module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Data types (unsigned 8-bit)](../datatypes)"
  - "[Image calibration](../spatial_calibration)"
objectives:
  - "Open and save various image files formats" 
  - "Understand the difference between image voxel data and metadata"
  - "Understand that converting between image file formats likely leads to loss of information"
motivation: |
  There are numerous ways how to save image data on disk. Virtually every microscope vendor has their own file format. It is thus very important to understand how to open those files and inspect their content. Moreover, some softwares will open only specific image file formats and thus it sometimes is necessary to re-save the data. During such image file format conversions information can be lost; it is important to be aware of this and avoid such information loss as much as possible.
  
concept_map: >
  graph LR
    IF("Image file") -->|contains| PD("Pixel data")
    IF -->|contains| MD("Metadata")
    MD --> "Image calibration, Microscope setttings, ..."
    IF -->|has| FF("File format")
    FF --> "TIFF, PNG, JPEG, CZI, ND2, LIF, ..."

figure: /figures/image_file_formats.png 
figure_legend: Image pixel data and metadata

activity_preface: |
  
### Image opening
  - For each image:
    - Open
    - Inspect pixel data
    - Inspect image metadata

### Image saving
  - Open image
  - Save image as JPEG
  - Reopen the image and compare the data and metadata to the original file


activities:
  - ["ImageJ GUI", "image_file_formats/activities/open_save_image.md", "markdown"]

exercises:

  ### Fill in the blanks

    - Saving an image in another format may ___ information.
    
    > ## Solution
    >   - Saving an image in another format may **loose** information.
    {: .solution}
    
learn_next:

external_links:
  - "[Bio-Formats](https://www.openmicroscopy.org/bio-formats/)"
  
---

