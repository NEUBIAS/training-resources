---
title: OME-Zarr
layout: module
tags: ["format"]
prerequisites:
  - "[Big image data file formats](../big_image_file_formats)"
objectives:
  - Understand the OME-Zarr image file format
  - Render cloud (S3 object store) hosted OME-Zarr image data
  - Access the pixel values of cloud hosted OME-Zarr image data
motivation: |
  Storing TB-sized image data locally and in multiple copies is either not possible or inefficient. Cloud storage enables efficient concurrent access to the same image data by multiple clients (scientists). OME-Zarr is the emerging community standard image file format for cloud (S3 object store) compatible image data storage. Thus it is important to know how to access S3 hosted OME-Zarr in various image analysis and visualisation platforms.

concept_map: >
  graph TD
    S3("S3 object store") ---|publicly hosts| C("Multi-scale image data chunks")
    C -->|read into| IV("Image viewer")

figure: /figures/ome-zarr.png
figure_legend: 

multiactivities:
  - ["ome_zarr/ome_zarr_creation.md", [["BatchConvert", "ome_zarr/ome_zarr_creation_batch-script.md"]]]
  - ["ome_zarr/ome_zarr_inspection.md", [["minio-client", "ome_zarr/ome_zarr_inspection_minio-client.md"], ["ome-zarr-py","ome_zarr/ome_zarr_inspection_ome-zarr-py.md"]]]
  - ["ome_zarr/ome_zarr_visualisation.md", [ ["napari","ome_zarr/ome_zarr_visualisation_napari.md"], ["Fiji/MoBIE", "ome_zarr/ome_zarr_visualisation_s3_mobie.md"], ["Neuroglancer","ome_zarr/ome_zarr_visualisation_s3_neuroglancer.md"], ["vizarr","ome_zarr/ome_zarr_visualisation_s3_vizarr.md"]]]
  - ["ome_zarr/ome_zarr_segmentation.md", [["ZarrSeg", "ome_zarr/ome_zarr_segmentation_zseg.md"]]]





assessment: >

learn_next:

external_links:
  - "[OME-NGFF, Nature Methods, 2021](https://www.nature.com/articles/s41592-021-01326-w)"
---
