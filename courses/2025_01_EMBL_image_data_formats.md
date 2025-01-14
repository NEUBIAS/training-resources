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

### Installation instructions

You will conduct the practical part of the course on your own computer.

It is required to perform the below installations before the course.

#### Download big image example data

https://zenodo.org/api/records/14591118/files-archive

#### Fiji

[Install Fiji on your computer.](https://fiji.sc/)

#### NGFF Converter

[Install the NGFF Converter on your computer.](https://www.glencoesoftware.com/products/ngff-converter/)

#### Python and CLI environment

Install Miniforge3 on your computer according to these instructions: \
https://github.com/conda-forge/miniforge

Now create the environment by running:

```bash
conda env create -f /path/to/environment.yml
```

Once the environment has been created, activate it by running:

```bash
conda activate image_data_formats
```

```bash
napari
```

Now the napari image viewer should open. If that is not the case, please check the below trouble shooting section or contact the instructors.

##### Troubleshooting

Remove the environment again

```bash
conda env remove -n image_data_formats
```

Delete any caches by running 

```bash
conda clean -all
```

Also remove cached packages

```bash
rm -r `~/miniforge3/pkgs`
```

Then install the environment again (see above).

## Schedule 

The whole course will be guided hands-on sessions.

- 2025 Jan 16, 9:30 - 16:00
- 2025 Jan 17, 9:30 - 16:00

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
    - Open TIFF stack in Fiji (Tischi)
    - Inspect BDV XML/HDF5 using h5ls (Demo Tischi)
    - Open BDV XML/HDF5 in Fiji with Bio-Formats (Tischi)
    - Open BDV XML/HDF5 in Fiji with BDV (Tischi)
1. [OME-TIFF](https://neubias.github.io/training-resources/tiff/index.html)
    - Open OME-TIFF in Bio-Formats Fiji (Tischi)
    - Save as OME-TIFF in Bio-Formats Fiji (Tischi)
    - Convert an image file to OME-TIFF
        - NGFF Converter (Tischi)
        - bfconvert (Bugra)
1. [OME-Zarr](https://neubias.github.io/training-resources/ome_zarr/index.html)
    - Open (Bugra)
        - ome-zarr inspection
        - ome-zarr validator
        - n5-ij
        - n5-viewer
    - Save (Bugra)
        - n5 saving from Fiji
    - Convert
        - NGFF Converter (Tischi)
        - BatchConvert local file (Bugra)
  
#### Day 2: Python (optional)

Same modules as first day but with python implementations.

Trainers: Bugra Oezdemir, Felix Schneider, Christian Tischer

1. [Image data formats](https://neubias.github.io/training-resources/image_file_formats/index.html)
    - Open a number of file formats in python (Felix)
1. [Big image data formats](https://neubias.github.io/training-resources/big_image_file_formats/index.html)
    - Lazy load TIFF stack (Felix)
    - Lazy load BDV (Felix)
1. [OME-TIFF](https://neubias.github.io/training-resources/tiff/index.html)
    - Open with bioio (Felix)
    - Save with bioio (Felix)
        - T and XYZ units 
    - Convert with bioio (Felix)
1. [OME-Zarr](https://neubias.github.io/training-resources/ome_zarr/index.html)
    - Open (Bugra)
        - napari
        - zarr
        - ome-zarr
        - n5-viewer
    - Save (Bugra)
        - ome-zarr
        - optional: rendering metadata