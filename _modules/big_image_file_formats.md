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
  - ["big_image_file_formats/lazy_load_tiff_stack.md", [["ImageJ GUI", "big_image_file_formats/lazy_load_tiff_stack_imagej_gui.md"],
  ["python bioio","image_file_formats/open_tif_bioio.py"]]]
  - ["big_image_file_formats/lazy_load_bdv_hdf5.md", [["h5ls", "big_image_file_formats/lazy_load_bdv_hdf5_h5ls.md"], ["ImageJ GUI BigDataViewer & Bio-Formats", "big_image_file_formats/lazy_load_bdv_hdf5_imagej_bdv.md"],
  ["python bioio","big_image_file_formats/open_BDV_bioio.py"]]]

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
  - "[Imaris file format](https://imaris.oxinst.com/support/imaris-file-format)"
---

### Similarities of big microscopy data with Google maps

We can think of the data in Google maps as one very big 2D image. Loading all the data in Google maps into your phone or computer is not possible, because it would take to long and your device would run out of memory. 

Another important aspect is that if you are currently looking at a whole country, it is not useful to load very detailed data about individual houses in one city, because the monitor of your device would not have enough pixels to display this information.

Thus, to offer you a smooth browsing experience, Google Maps **lazy loads** only the part of the world (**chunk**) that you currently look at, at an **resolution level** that is approriate for the number of pixels of your phone or computer monitor.

### Chunking

The efficiency with which parts (chunks) of image data can be loaded from your hard disk into your computer memory depends on how the image data is layed out (chunked) on the hard disk. This is a longer, very technical, discussion and what is most optimal probably also depends on the exact storage medium that you are using. Essentially, you want to have the size of your chunks small enough such that your hardware can load one chunk very fast, but you also want the chunks big enough in order to minimise the number of chunks that you need to load. The reason for the latter is that for each chunk your software has to tell your computer "please go and load this chunk", which in itself takes time, even if the chunk is very small. Thus, big image data formats typically offer you to choose the chunking such that you can optimise it for your hardware and access patterns.

### Resolution pyramids

If the image data is big and one is zoomed out, the data may have more pixels that the viewing window of your computer monitor. In this case it makes no sense to load all the data, but a lower resolution (down-sampled) version of the same data would give you the same displayed information and, since it is less data, it could be loaded  faster. Thus, for big image data one typically saves the data multiple times at different levels of downsampling in a so-called resolution pyramid. If you use appropriate viewing software it will automatically load the data from the appropriate resolution level, depending on your zoom level and the number of pixels of your viewing device. Note that is not only useful for fast visualisation, but can be also handy for image analysis purposes, where certain computations may not need to be performed on the full resolution data.

See also an introduction to [resolution pyramids on Wikipedia](https://en.wikipedia.org/wiki/Pyramid_%28image_processing%29)


### TIFF chunking

![Lazy load from 3D TIFF](../figures/tiff_chunking.png)

TIFF files are chunked as **planes** and as **strips** within the planes.
One can therefore efficiently lazy load XY planes from a TIFF file. However, in particular lazy loading of YZ planes is very inefficient. The reason is that for typical storage systems (e.g., hard disks) data that resides close together can be swiftly fetched in **one read** operation. However, data that is distributed must be read in **several  seek and read** operations, which is much slower, because each operation needs time. Note that often it is actually faster to just read everything in one go, even if not all data is needed.



