---
title: TIFF 
layout: module
tags: ["draft","format"]
prerequisites:
  - "[Image file formats](../image_file_formats)"
objectives:
  - Understand the TIFF file format
  - Read and write TIFF image data
  - Read and write TIFF metadata
motivation: |
  In bioimaging, TIFF is one of the most wide-spread image file formats. Thus there is a very high probability that you will need to deal with such files. It therefore is very important to understand how to read and write such files and also have some understanding about the actual file format, as this will help you to understand its benefits and limitations.

concept_map: >
  graph TD
    T("TIFF") --- P("Image planes")
    P --> M("Metadata")

figure: /figures/tiff.png
figure_legend: TIFF stores image data as a series of planes

multiactivities:
  - ["tiff/act01.md", [["ImageJ GUI", "tiff/act01_imagejgui.md"], ["python tifffile", "tiff/act01_tifffile.py"]]]

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .
    
    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:

external_links:
  - "[TIFF](https://en.wikipedia.org/wiki/TIFF)"
  - "[OME-TIFF](https://docs.openmicroscopy.org/ome-model/5.6.3/ome-tiff/)"
---

