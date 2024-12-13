---
title: OME-TIFF
layout: module
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
figure_legend: "TIFF is a planar file format, where one TIFF file can contain multiple image planes of different sizes and different data types, which are specified in the respective IFD block. OME-TIFF features an additional OME-XML metadata block, which describes additional important microscopy metadata such as the mapping of IFDs to channel, time-point, and z-plane. In addition, OME-TIFF supports storing different image series within one TIFF file. Within an images series the image datatype, width and height are the same for all planes. In the figure, the OME-TIFF contains two image series, where the first is a z-stack and the second is a multi-channel image." 

multiactivities:
  - ["ome_tiff/open_ometiff.md", [["Fiji Bio-Formats", "ome_tiff/open_ometiff_fiji_bioformats.md"],["Python/BioIO", "ome_tiff/open_ome_tif_bioio.py"]]]
  - ["ome_tiff/save_ometiff.md", [["Python/BioIO", "ome_tiff/save_ome_tif_bioio.py"]]]
  - ["ome_tiff/convert_to_ometiff.md", [["NGFF-Converter", "ome_tiff/convert_to_ometiff_ngff-converter.md"],["Python/BioIO", "ome_tiff/convert_lif_to_ome_tif_bioio.py"]]]


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
  - "[OME-TIFF metadata specification](https://www.openmicroscopy.org/Schemas/Documentation/Generated/OME-2016-06/ome_xsd.html#TiffData)"
---

#### General comments

The TIFF file format is already complex and the OME-TIFF variant is adding even more metadata on top. To fully understand everything is way beyond the aim of this training material. We will just scratch the surface to understand the most important concepts.

#### IFDs and image planes

TIFF is a planar image data format. Internally there are always pairs of IFD and data blocks. IFD stands for "Image File Directory" and contains information about where the corresponding image data block can be found in the file, the image width and height, as well as its datatype.

One TIFF file can contain many IFD/data pairs.

The IFD/data pairs may contain images of different sizes and different datatypes.

#### Physical pixel size

The TIFF format does natively support storing pixel size metadata, typically in units of centimetre or inches. 

#### Resolution pyramids and chunking

The TIFF format supports the concept of resolution pyramids, and chunked storage of pixels within one plane. However there is no 3-D chunking available. Thus, TIFF can in fact be used as a 2-D big image data format.

#### Channels, z-planes, and time points 

The TIFF format does **not** natively support storing information about which channel, z-plane or time-point an IFD/data pair belongs to. This bioimaging specific information is handled by additional metadata of TIFF variants, such as OME-TIFF.