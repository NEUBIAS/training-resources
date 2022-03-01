---
title: Access S3 hosted OME-Zarr 
layout: module
tags: ["draft","ome-zarr","cloud","big image data"]
prerequisites:
  - "OME-Zarr image file format (TODO)"
objectives:
  - Render cloud (S3 object store) hosted OME-Zarr image data.
  - Access the pixel values of cloud hosted OME-Zarr image data.
motivation: |
  Storing TB-sized image data locally and in multiple copies is either not possible or inefficient. Cloud storage enables efficient concurrent access to the same image data by multiple clients (scientists). OME-Zarr is the emerging community standard image file format for cloud (S3 object store) compatible image data storage. Thus it is important to know how to access S3 hosted OME-Zarr in various image analysis and visualisation platforms.

concept_map: >
  graph LR
    S3("S3 object store") --- O("Objects")
    O ---|are| C("Image parts/blocks/chunks")
    R("Read") -->|http| O

figure: /figures/ome-zarr-s3.jpg 
figure_legend: 

activity_preface: |
  - Example URLs:
    - https://s3.embl.de/i2k-2020/em-raw.ome.zarr (3D EM with label mask)

activities:
  - ["ImageJ GUI MoBIE", "ome_zarr_s3/activities/ome_zarr_s3_mobie.md", "markdown"]

exercises:

assessment: >

learn_next:

external_links:
  - "[OME-NGFF, Nature Methods, 2021](https://www.nature.com/articles/s41592-021-01326-w)"
---
