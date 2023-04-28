---
title: OME-Zarr
layout: module
tags: ["draft","format"]
prerequisites:
  - "[Big image data file formats](../big_image_file_formats)"
objectives:
  - Understand the OME-Zarr image file format
  - Read and write OME-Zarr
  - Render cloud (S3 object store) hosted OME-Zarr image data.
  - Access the pixel values of cloud hosted OME-Zarr image data.
motivation: |
  Storing TB-sized image data locally and in multiple copies is either not possible or inefficient. Cloud storage enables efficient concurrent access to the same image data by multiple clients (scientists). OME-Zarr is the emerging community standard image file format for cloud (S3 object store) compatible image data storage. Thus it is important to know how to access S3 hosted OME-Zarr in various image analysis and visualisation platforms.

concept_map: >
  graph TD
    S3("S3 object store") ---|publicly hosts| C("Multi-scale image data chunks")
    C -->|read into| IV("Image viewer")

figure: /figures/ome-zarr.png
figure_legend: The OME-Zarr format consists of a folder structure where image chunks are stored as binary files

multiactivities:
  - ["ome_zarr/render_ome_zarr_s3.md", [ ["Fiji/MoBIE", "ome_zarr/ome_zarr_s3_mobie.md"], ["Neuroglancer", "ome_zarr/ome_zarr_neuroglancer.md"]]]

exercises:

assessment: >

learn_next:

external_links:
  - "[OME-NGFF, Nature Methods, 2021](https://www.nature.com/articles/s41592-021-01326-w)"
---
