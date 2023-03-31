---
title: Access S3 hosted OME-Zarr
layout: module
tags: ["draft","format"]
prerequisites:
  - "[Big image data file formats](../big_image_file_formats)"
objectives:
  - Render cloud (S3 object store) hosted OME-Zarr image data.
  - Access the pixel values of cloud hosted OME-Zarr image data.
motivation: |
  Storing TB-sized image data locally and in multiple copies is either not possible or inefficient. Cloud storage enables efficient concurrent access to the same image data by multiple clients (scientists). OME-Zarr is the emerging community standard image file format for cloud (S3 object store) compatible image data storage. Thus it is important to know how to access S3 hosted OME-Zarr in various image analysis and visualisation platforms.

concept_map: >
  graph TD
    S3("S3 object store") ---|publicly hosts| C("Multi-scale image data chunks")
    C -->|read into| IV("Image viewer")

figure: /figures/ome-zarr-s3.jpg 
figure_legend: 

activity_preface: |
  - Visualise S3 hosted OME-Zarr images
  - Appreciate that the data can be multi-scale and chunked
  - Example data:
    - URL: `https://s3.embl.de/i2k-2020/em-raw.ome.zarr`
      - Content: 3-D EM with label mask
      - Metadata: [https://s3.embl.de/i2k-2020/platy-raw.ome.zarr/.zattrs](https://s3.embl.de/i2k-2020/platy-raw.ome.zarr/.zattrs)

activities:
  - ["MoBIE", "ome_zarr_s3/activities/ome_zarr_s3_mobie.md", "markdown"]
  - ["Neuroglancer", "ome_zarr_s3/activities/ome_zarr_neuroglancer.md", "markdown"]

exercises:

assessment: >

learn_next:

external_links:
  - "[OME-NGFF, Nature Methods, 2021](https://www.nature.com/articles/s41592-021-01326-w)"
---
