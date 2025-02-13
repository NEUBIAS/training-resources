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
  - Apply basic image processing on cloud hosted OME-Zarr image data
motivation: |
  Storing TB-sized image data locally and in multiple copies is either not possible or inefficient. Cloud storage enables efficient concurrent access to the same image data by multiple clients (scientists). OME-Zarr is the emerging community standard image file format for cloud (S3 object store) compatible image data storage. Thus it is important to know how to access S3 hosted OME-Zarr in various image analysis and visualisation platforms.

concept_map: >
  graph TD
    S3("S3 object store") ---|publicly hosts| C("Multi-scale image data chunks")
    C -->|read into| IV("Image viewer")

figure: /figures/ome-zarr.png
figure_legend: 


multiactivities:
  - ["ome_zarr/open_ome_zarr.md", [
            ["Inspect OME-Zarr datasets using minio-client", "ome_zarr/ome_zarr_inspection_minio-client.md"], 
            ["Inspect OME-Zarr from IDR using minio-client", "ome_zarr/ome_zarr_work_with_idr_bucket_minio-client.md"],
            ["Inspect OME-Zarr datasets using ome_zarr_py client","ome_zarr/ome_zarr_inspection_ome-zarr-py.md"],
            ["Inspect and validate OME-Zarr in Python using ome-zarr-validator","ome_zarr/validate_ome_zarr_ome-zarr-validator.md"],
            ["Open local OME-Zarr in Python using zarr-python","ome_zarr/open_local_ome_zarr_zarr-python.md"],
            ["Open remote OME-Zarr in Python using zarr-python","ome_zarr/open_remote_ome_zarr_zarr-python.md"],
            ["Open OME-Zarr in Python using ome-zarr-py","ome_zarr/open_ome_zarr_ome-zarr-py.md"],
            ###
            ["Open OME-Zarr in Fiji using MoBIE", "ome_zarr/ome_zarr_open_java_mobie.md"],
            ["Open OME-Zarr in Fiji using n5-ij", "ome_zarr/ome_zarr_open_java_n5-ij.md"],
            ["Open OME-Zarr in Fiji using n5-viewer", "ome_zarr/ome_zarr_open_java_n5-viewer.md"],
            ["Open OME-Zarr in napari","ome_zarr/ome_zarr_visualisation_napari.md"],
            ["Open OME-Zarr in the browser using vizarr","ome_zarr/ome_zarr_visualisation_s3_vizarr.md"],
            ["Open OME-Zarr in the browser using neuroglancer","ome_zarr/ome_zarr_visualisation_s3_neuroglancer.md"],
            ["Open OME-Zarr in the browser using webKnossos","ome_zarr/ome_zarr_visualisation_s3_webknossos.md"],
            ["Open OME-Zarr in the browser using ITK viewer","ome_zarr/ome_zarr_visualisation_s3_itk_viewer.md"],
            ["Open OME-Zarr in the browser using BioImage Archive tools","ome_zarr/ome_zarr_visualisation_s3_bia.md"]
        ]
  ]
  - ["ome_zarr/save_ome_zarr.md", [
            ["Export OME-Zarr from Python using ome-zarr-py","ome_zarr/save_ome_zarr_ome-zarr-py.md"],
            ["Export an image from Fiji as OME-Zarr","ome_zarr/save_ome_zarr_fiji.md"],           
            ["Update the rendering metadata using zarr and ome-zarr-py","ome_zarr/update_rendering_metadata.md"],
        ] 
  ]
  - ["ome_zarr/ome_zarr_creation.md", [
            ["BatchConvert", "ome_zarr/ome_zarr_creation_BatchConvert.md"]
        ]
  ]

assessment: >

learn_next:

external_links:
  - "[OME-NGFF, Nature Methods, 2021](https://www.nature.com/articles/s41592-021-01326-w)"

---


#### Cloud compatible serving of big image data

Aim: sharing big image data with collaborators at different institutions or the general public.

Considerations that let to the implementation of OME-Zarr
- Security: A simple URL download link is an easy and safe way to share data via the web
- Efficiency: Downloading the whole image can be slow and inefficient if it is large (>10 GB)
- Chunking and multi-resolution are established methods for accessing parts of large image data
- "One chunk = one file = one download URL" seemed the simplest web compatible implementation of chunking
  - This let to the development of Zarr (not specifically for image data, but generic arrays of numerical data)  
  - OME-Zarr is Zarr with bioimaging specific metadata
- "S3 Object Stores" are a well established web server technology to efficiently serve many files in parallel, thus OME-Zarr is often hosted on S3 object stores
  - Technically, this efficient parallelisation is important, because http requests typically have around ~100 ms overhead. Thus, accessing the chunks sequentially would be slow (much slower than on a hard-disk where mere access only takes nanoseconds)







