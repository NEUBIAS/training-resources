# Image data formats

## Why take this course

Performing modern microscopy one is exposed to many different image data formats. Almost all microscope vendors have their own format. In addition, there are a few formats that are developed by the scientific community. Navigation this sea of formats is very challenging. In this course you will learn how to read most image formats and how to write a few recommened formats. In addition, you will learn about reading and writing big image data, which includes learning about the concepts of chunking and scale pyramids.

## Prerequisites

* This is a practical course that will be conducted using the Fiji GUI and python scripting. It is helpful if you have used Fiji and have done some basic python scripting before taking this course. However, while it may be a bit challenging, you may also be able to follow without this prior knowledge.
* Please be familiar, at least conceputally, with the content of these modules:
  * [Digital image basics](https://neubias.github.io/training-resources/pixels/index.html)
  * [Spatial calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html)
  * [Image data types](https://neubias.github.io/training-resources/datatypes/index.html)
  * [Volume slicing](https://neubias.github.io/training-resources/volume_slicing/index.html)

### IT Setup

You will conduct the practical part of the course on your own computer.

It is required to perform the below installations before the course:

1. [Install Fiji with a few update sites](https://neubias.github.io/training-resources/tool_installation/index.html?id_activity_platform-1=conda-activity-1&id_activity_platform-0=fiji-activity-0#imagej)
1. [Install and test the python dependencies skimage and napari](https://neubias.github.io/training-resources/tool_installation/index.html?id_activity_platform-1=conda-activity-1#skimage_napari)


## Schedule 

The whole course will be guided hands-on sessions.

- 2025 Jan 16, 9:30 - 17:00
- 2025 Jan 17, 9:30 - 17:00

## Venue

- Germany, Heidelberg, Meyerhofstr. 1, EMBL, Room: IC Lecture hall
- Zoom link: Has been sent by mail

## Trainers and organisers

- Bugra Oezdemir (EMBL)
- Felix Schneider (EMBL)
- Christian Tischer (EMBL)

## Teaching tips

Dear Trainers, please consider checking these [teaching tips](https://github.com/NEUBIAS/training-resources/blob/master/TEACHING_TIPS.md).

## Teaching content

### Introduction

- Trainers introduce themselves, where they work and how they are competent
- Participants introduce themselves, where they work, why they joined the course, and what previous experience they have
    - Depending on the number of participants, one could distribute the introductions across the course, e.g. do some in the morning and some in the afternoon

### Modules


#### Day 1: GUI/CLI: Fiji / NGFF Converter / Bftools

Trainers: Christian Tischer, Bugra Oezdemir, Felix Schneider

1. [Image data formats](https://neubias.github.io/training-resources/image_file_formats/index.html)
    - Open a number of file formats in Fiji (Tischi)
1. [Big image data formats](https://neubias.github.io/training-resources/big_image_file_formats/index.html)
    - DONE: Tischi: Upload somewhere a somewhat large TIFF file series (ask EMCF)
    - TODO: Felix: Implementation Lazy load from TIFF file series in python
    - DONE: Tischi: add activity for opening BDV HDF5
        - DONE: Tischi: implementation HDFView
        - DONE: Tischi: implementation Fiji GUI for BDV 
        - TODO: Felix: implementation opening BDV in python
1. [OME-TIFF](https://neubias.github.io/training-resources/tiff/index.html)
    - TODO: Felix: https://github.com/NEUBIAS/training-resources/issues/729
    - DONE: Tischi: implementation save image as OME.TIFF in Fiji
        - Boats sample image, including manually adding pixel sizes
    - Convert:
        - bfconvert (Bugra) TODO
1. [OME-Zarr](https://neubias.github.io/training-resources/ome_zarr/index.html)
    - Open 
        - mc inspection
        - ome-zarr validator
        - n5-ij
        - n5-viewer
    - Save
        - TODO: Bugra: n5 saving from Fiji
    - Convert
        - TODO: Tischi: NGFF converter tool
        - BatchConvert  
  
#### Day 2: Python (optional)

Same modules as first day but with python implementations.

Trainers: Bugra Oezdemir, Felix Schneider, Christian Tischer

1. [Image data formats](https://neubias.github.io/training-resources/image_file_formats/index.html)
    - Open a number of file formats in python (Felix)
1. [Big image data formats](https://neubias.github.io/training-resources/big_image_file_formats/index.html)
    - TODO: Lazy load TIFF series (Felix)
    - TODO: Lazy load BDV (Felix)
1. [OME-TIFF](https://neubias.github.io/training-resources/tiff/index.html)
    - Open with bioio (Felix)
    - Save with bioio (Felix)
        - TODO: T and XYZ units 
    - Convert (Felix)
        - TODO: Remove indirect conversion
1. [OME-Zarr](https://neubias.github.io/training-resources/ome_zarr/index.html)
    - Open (Bugra)
        - napari
        - zarr
        - ome-zarr
        - n5-viewer
    - Save (Bugra)
        - ome-zarr
        - optional: rendering metadata