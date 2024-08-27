---
title: Big image data formats
layout: module
tags: ["chunking","multi-scale"]
prerequisites:
  - "[Slice viewing](../volume_slicing.md)"
objectives:
  - "Understand the concepts of lazy-loading, chunking and scale pyramids"
  - "Know some file formats that implement chunking and scale pyramids"
motivation: |
  Modern microscopy frequently generates image data in the GB-TB range. Such data cannot be naively opened. First, the data may not fit into the working memory (RAM) of your computer. Second, it would take a lot of time to load the data into the memory. Thus, it is important to know about dedicated concepts and implemenations that enable swift interaction with such big image data.

concept_map: >
  graph TD
    BIG("Big image data") -->|saved as| RP("Scale pyramids")
    RP -->|saved as| C("Chunks on disk")
    C -->|lazy-load| PC("Computer memory")

figure: /figures/big_image_data_file_formats.jpg
figure_legend: "Top left: For high-resolution or large image data there can be situations where there are less pixels in the viewer window than in the data, thus only a subset can be loaded, which is hard to do in practice such that typically all data needs to be loaded, which is expensive. Having one or more downsampled versions of the data solves this issue. Bottom left: Also when zooming in there are more pixels in data space than are currently needed in viewer space. Chunked data storage allows to restrict the data loading to a smaller region in data space. Right: Examples of chunks and scale pyramids."

activity_preface: |
  - Inspect the size of a large TIFF file on disk.
  - Compare the file size to the size of your computer's memory.
  - Open this file in an image viewer.
    - Observe that this takes some time.
    - Observe that your memory fills up.
  - Open a big image (several GB) from a TIFF file.
  - Lazy-load a big image (several GB) from a TIFF file.
    - Observe that TIFF chunking is plane-wise.
      - Observe that slicing "at an angle" requires loading everything.
  - Lazy-load from a file format with resolution pyramid and 3-D chunking (e.g. OME-Zarr, BDV/XML/HDF5)
    - Observe that it opens very quickly (thanks to resolution pyramid and chunking).
    - Observe that one can swiftly slice the data at all angles (thanks to 3-D chunking).
    - Inspect the file format to see the resolution pyramid and chunks.
    - Only load one specific resolution level.
      - This is useful as most software does not support multi-resolution data for computations.

activities:
  - ["ImageJ GUI", "big_image_file_formats/activities/big_image_file_formats_imagejgui.md", "markdown"]

exercises:

assessment: >

  ### Fill in the blanks

    1. Opening data piece-wise on demand is also called ___ .
    1. Storing data piece-wise is also called ___ .
    1. In order to enable fast inspection of spatial data at different scales (like on Google maps) one can use ___ .

    > ## Solution
    >   1. lazy-loading
    >   1. chunking
    >   1. resolution pyramids
    {: .solution}

learn_next:

external_links:
---

