---
title: Big image data formats
layout: module
tags: ["chunking","multi-scale"]
prerequisites:
  - "[Slice viewing](../volume_slicing.md)"
objectives:
  - "Understand the concepts of lazy-loading, chunking and scale pyramids"
  - "Understand some file formats that implement chunking and scale pyramids"
motivation: |
  Modern microscopy frequently generates image data in the GB-TB range. Such data cannot be naively opened. First, the data may not fit into the working memory (RAM) of your computer. Second, it would take a lot of time to load the data into the memory. Thus, it is important to know about dedicated concepts and implemenations that enable swift interaction with such big image data.

concept_map: >
  graph TD
    BIG("Big image data") --- RP("Resolution pyramids")
    BIG --- C("Chunking")
    C --- LL("Lazy loading")

figure: /figures/big_image_file_formats.png
figure_legend: "Big image data formats typically support flexible chunking of data and resolution pyramids. Chunking enables efficient loading of image subregions. Resolution pyramids prevent loading useless details when being zoomed out."

multiactivities:
  - ["big_image_file_formats/lazy_load_tiff_stack.md", [["ImageJ GUI", "big_image_file_formats/lazy_load_tiff_stack_imagej_gui.md"]]]

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

### Analogy of big image data with Google Maps

When thinking about big image data it is helpful to think about Google Maps. There, you often don't want to see the whole image (planet earth) but rather zoom in on a region (e.g., country). And, if you are zoomed out (e.g., on a continent) you don't care about seeing individual houses in a city; in fact, your computer monitor would not have enough pixels do display all these details while still showing a whole continent, and it would probably not have enough memory to even download all this data.

Thus, to offer you a smooth experience, Google Maps **lazy loads** only the part of the world (**chunk**) that you currently look at, at an **resolution level** that is approriate for the number of pixels of your viewing device (phone or computer monitor).

### Chunking

The efficiency with which parts (chunks) of image data can be loaded from your hard disk into your computer memory depends on how the image data is layed out (chunked) on the hard disk. This is a longer, very technical, discussion and what is most optimal probably also depends on the exact storage medium that you are using. Essentially, you want to have the size of your chunks small enough such that your hardware can load one chunk very fast, but you also want the chunks big enough in order to minimise the number of chunks that you need to load. The reason for the latter is that for each chunk your software has to tell your computer "please go and load this chunk", which in itself takes time even if the chunk is very small. Thus, big image data formats typically offer you to choose the chunking such that you can optimise it for your hardware and access patterns.

### Resolution pyramids

TODO



