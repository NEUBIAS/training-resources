---
title: OME-TIFF
layout: module
tags: ["draft"]
prerequisites:
  - "[Digital image basics](../pixels)"
objectives:
  - "Understand the basic concept of the TIFF image data format"
  - "Understand that there are various TIFF variants, such as ImageJ-TIFF and OME-TIFF"
  - "Create OME-TIFF files"
  - "Convert other image data into OME-TIFF files"
  - "Inspect OME-TIFF image data and metadata"
motivation: |
  - Representing microscopy image data on disk is essential
  - Understanding the pros and cons as well how to work with different image data formats is essential
  - TIFF is among the most wide-spread microscopy image file formats
  - TIFF is tricky, because the internal content of a .tiff file can vary substantially
  - OME-TIFF is an attempt to create a TIFF standard for bioimaging

concept_map: >
  graph TD
    T("TIFF") --- I("Image data and metadata")
    T --- P("Planar image data model")
    T --- V("Variants exist")
    V --- OT("OME-TIFF is an important variant")

figure: /figures/tiff.png
figure_legend: TODO

multiactivities:
  - ["ome_tiff/lif2ometiff.md", [["Fiji & NGFF-Converter", "ome_tiff/lif2ometiff_fiji_ngff-converter.md"]]]

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
  - "[Converting an image series to OME-TIFF](https://forum.image.sc/t/tiff-series-to-ome-ngff/101081/7)"
  - "[Wikipedia: TIFF](https://en.wikipedia.org/wiki/TIFF)"
  - "[TODO: Add OME-TIFF link]()"
---
