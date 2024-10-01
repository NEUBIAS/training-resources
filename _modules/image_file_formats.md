---
title: Image data formats
layout: module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Data types](../datatypes)"
  - "[Image calibration](../spatial_calibration)"
objectives:
  - Open and save various image files formats
  - Understand the difference between image voxel data and metadata
  - Understand that converting between image file formats likely leads to loss of information

motivation: |
  There are numerous ways how to save image data on disk. Virtually every microscope vendor has their own file format. It is thus very important to understand how to open those files and inspect their content. Moreover, some software will open only specific image file formats and thus it is sometime necessary to re-save the data. During such image file format conversions information can be lost; it is important to be aware of this and avoid such information loss as much as possible.

concept_map: >
  graph TD
    F("TIFF, JPEG, XML/HDF5, CZI, LIF, ...")
    F --> PD("Pixel data")
    PD --> Values
    PD --> Dimensions
    F --> MD("Metadata")
    MD --> IC("Image calibration")
    MD --> MS("Microscope settings")
    MD --> DS("Display settings")
    MD --> NA("...")

figure: /figures/image_file_formats.png
figure_legend: "Image pixel data are saved as binary data on disk. Essential metadata is needed to load the binary data into an image array."

multiactivities:
  - ["image_file_formats/open_tif.md", [["ImageJ GUI", "image_file_formats/open_tif_imagejgui.md"],["python BioIO", "image_file_formats/open_tif_bioio.py"]]]
  - ["image_file_formats/open_czi.md", [["ImageJ GUI", "image_file_formats/open_czi_imagejgui.md"],["python BioIO", "image_file_formats/open_czi_bioio.py"]]]
  - ["image_file_formats/open_em_tiff_series.md", [["ImageJ GUI", "image_file_formats/open_em_tiff_series_imagejgui.md"],["python BioIO", "image_file_formats/open_em_tiff_series_bioio.py"]]]
  - ["image_file_formats/open_diverse_file_formats.md", [["ImageJ GUI", "image_file_formats/open_diverse_file_formats_imagejgui.md"],["python BioIO", "image_file_formats/open_diverse_file_formats_bioio.py"]]]
  - ["image_file_formats/resaving_images.md", [["ImageJ GUI", "image_file_formats/resaving_images_imagejgui.md", "markdown"]]]

assessment: >

  ### True or false

    1. One could use Excel's XLSX file format for saving image data.

    > ## Solution
    >   1. One could use Excel's XLSX file format for saving image data. **True**, the matrix of each sheet could represent one image plane and one could use the first sheet to store metadata and the mapping of each sheet (image plane) to the zct coordinates, e.g. `sheet 12  c 2  z 3  t 1`.
    {: .solution}


  ### Discuss
    1. What are the pros and cons of converting an image into another format? 
    1. What are the pros and cons of splitting metadata and image pixel data into separate files?
    1. Do you know any good file formats for image metadata? 

    > ## Solution
    >   1. (A) Sometimes it is necessary to convert to another format to be able to open the image in a specific software. (B) Converting an image to another format typically loose information, e.g. because the file format that you are saving to cannot represent all the metadata of the original image file. Thus, it is in general recommened to keep to original image file. (C) Converting to a file format with good compression may save you considerable disk space.
    >   1. (A) Metadata typically is much smaller than the pixel data. Thus, it can be a good idea to keep metadata in a separate file that can be readily inspected (inspecting the potentially TB sized pixel data files can be tricky). (B) The best file formats for metadata and pixel data can be very different due to the nature of the data, thus splitting can make sense. (C) Having separate files always bares the risk that you loose one of them, e.g. you may forget to copy both to a new folder.  
    >   1. TXT, XML, and JSON are good formats for image metadata, because they are human readable standard formats that can be openend with any text editor.  
    {: .solution}

learn_next:

external_links:
  - "[Bio-Formats](https://www.openmicroscopy.org/bio-formats/)"
  - "[OME-TIFF](https://docs.openmicroscopy.org/ome-model/5.6.3/ome-tiff/)"
  - "[OME-NGFF](https://github.com/ome/ngff)"
---
