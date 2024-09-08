---
title: TIFF
layout: module
tags: ["draft"]
prerequisites:
  - "[Digital image basics](../pixels)"
objectives:
  - "Understand the basic concept of the TIFF image data format"
  - "Create TIFF files"
  - "Convert other image data into TIFF files"
  - "Inspect TIFF image data and metadata"
  - "Understand that there are various TIFF variants, such as ImageJ-TIFF and OME-TIFF"
motivation: |
  - Representing microscopy image data on disk is essential
  - Understanding the pros and cons as well how to work with different image data formats is essential
  - TIFF is among the most wide-spread microscopy image file formats
  - TIFF is tricky, because the internal content of a .tiff file can vary substantially

concept_map: >
  graph TD
    T("TIFF") --- I("Image data and metadata")
    T --- P("Planar image data model")
    T --- V("Variants exist")

figure: /figures/tiff.png
figure_legend: TODO

multiactivities:
  - ["tiff/act01.md", [["ImageJ GUI", "tiff/act01_imagejgui.md"], ["skimage napari", "tiff/act01_skimage_napari.py"]]]

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .
    
    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:
  - "[OME-Zarr](../ome-zarr)"

external_links:
  - "[Wikipedia: TIFF](https://en.wikipedia.org/wiki/TIFF)"
---
