---
title: Remote (image) data access
layout: module
tags: ["draft"]
prerequisites:
  - "[TODO](../remote_data_access)"
objectives:
  - "TODO"
motivation: |
  TODO

concept_map: >
  graph TD
    WWW("WWW") --- WWWP("WWW Protocols")
    
figure: /figures/remote_data_access.png
figure_legend: Accessing remote (cloud hosted) data typically relies on specific protocols, such as HTTP and FTP.

multiactivities:
  - ["remote_data_access/act01.md", [["ImageJ GUI", "remote_data_access/act01_imagejgui.md"], ["skimage napari", "remote_data_access/act01_skimage_napari.py"]]]

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .
    
    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:
  - "[TODO](../auto_threshold)"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"
---

#### Cloud compatible serving of big image data

Aim: sharing big image data with collaborators at different institutions or the general public.

Considerations that let to the implementation of (OME-)Zarr
- Security: A simple URL download link is an easy and safe way to share data via the web
- Efficiency: Downloading the whole image can be slow and inefficient if it is large (>10 GB)
- Chunking and multi-resolution are established methods for accessing parts of large image data
- "One chunk = one file = one download URL" seemed the simplest web compatible implementation of chunking
  - This let to the development of Zarr (not specifically for image data, but generic arrays of numerical data)  
  - OME-Zarr is Zarr with bioimaging specific metadata
- **S3 Object Stores** are a well established web server technology to efficiently serve many files in parallel, thus OME-Zarr is often hosted on S3 object stores
  - Technically, the **efficient parallelisation** is important, because HTTP requests typically have ~100 ms overhead. Thus, accessing chunks sequentially would be slow (slower than on a hard-disk where where the overhead per read is less)

