---
title:     Image file formats     
layout:    module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Data types (unsigned 8-bit)](../datatypes)"
objectives:
  - "Understand the difference between image voxel data and metadata"
  - "Understand that converting from one image file format to another can lead to loss of information"
motivation: |
  There are numerous ways how to save image data on disk. Virtually every microscope vendor has their own file format. It is very important to understand how to open those files and inspect their content.
  
concept_map: >
  graph TD
    PV("Pixel values") --> BA(Binarization algorithm)
    BA --> BPV("Binarized pixel values")
    BPV --> BG("Background (0)")
    BPV --> FG("Foreground (1)")

figure: 
figure_legend: 

activity_preface: |
  
### Image opening
  - Open the images:
  - Inspect the metadata
  - Inspect the data

### Image saving
  - Open image
  - Save image as JPEG
  - Reopen the image and compare the data and metadata to the original file


activities:
  - ["ImageJ GUI", "image_file_formats/activities/open_save_image.md", "markdown"]

exercises:

  ### Fill in the blanks

    - Saving an image in another format can only ___ information.
    
    > ## Solution
    >   - Saving an image in another format can only **loose** information.
    {: .solution}
    
learn_next:

external_links:
  - "[Bio-Formats](https://www.openmicroscopy.org/bio-formats/)"
  
---

