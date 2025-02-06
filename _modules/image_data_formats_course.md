---
title: Image data formats course overview
layout: module
prerequisites:
  - "Familiarity with using [Fiji](https://fiji.sc/)'s graphical user interface"
  - "[Basics of python scripting](https://swcarpentry.github.io/python-novice-inflammation/)"
  - "[Digital image basics](https://neubias.github.io/training-resources/pixels/index.html)"
  - "[Spatial calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html)"
  - "[Image data types](https://neubias.github.io/training-resources/datatypes/index.html)"
  - "[Volume slicing](https://neubias.github.io/training-resources/volume_slicing/index.html)"
  - "[Label mask (segmentation) images](https://neubias.github.io/training-resources/connected_components/index.html)"
objectives:
  - "Know and open various common image files formats"
  - "Understand important concepts and implementations of big image file formats: lazy-loading, chunking and scale pyramids"
  - "Open and create OME-TIFF"
  - "Open and create OME-Zarr"

motivation: |
  Performing modern microscopy one is exposed to many different image data formats. Almost all microscope vendors have their own format. In addition, there are a few formats that are developed by the scientific community. Navigation this sea of formats is very challenging. In this course you will learn how to read most image formats and how to write a few recommened formats. In addition, you will learn about reading and writing big image data, which includes learning about the concepts of chunking and scale pyramids.

concept_map: >
  graph TD
    PD("Pixel data") --> FF("Image data format")
    MD("Image metadata") --> FF

figure: /figures/image_data_formats_course.png
figure_legend: "Microscopy image data can be represented as a number of different file formats. OME-TIFF and OME-Zarr are two standard formats used in bioimaging."

learn_next:

external_links:
  - "[Bio-Formats](https://www.openmicroscopy.org/bio-formats/)"
  - "[OME-TIFF](https://docs.openmicroscopy.org/ome-model/5.6.3/ome-tiff/)"
  - "[OME-NGFF](https://github.com/ome/ngff)"
---

### General comments

The material for this course consists of the following training modules:

1. [Image data formats](https://neubias.github.io/training-resources/image_file_formats/index.html)
1. [Big image data formats](https://neubias.github.io/training-resources/big_image_file_formats/index.html)
1. [OME-TIFF](https://neubias.github.io/training-resources/tiff/index.html)
1. [OME-Zarr](https://neubias.github.io/training-resources/ome_zarr/index.html)

As usual, each training module contains several activities that can be executed in various compute platforms. As a trainer, it is necessary to familiarise yourself with the material and decide what to teach.

It is also highly recommended to consider our [TEACHING TIPS](https://github.com/NEUBIAS/training-resources/blob/master/TEACHING_TIPS.md).

### Installation instructions

In order to conduct the activities it is required to perform the below installations before the course.

- [Install Fiji](https://fiji.sc/)
- [Install NGFF Converter](https://www.glencoesoftware.com/products/ngff-converter/)
- [Download big image data (~4GB)](https://zenodo.org/api/records/14591118/files-archive)

#### Install the python and command line environment

- Install the [Miniforge3](https://github.com/conda-forge/miniforge) conda package manager
- Create the environment `conda env create -f https://raw.githubusercontent.com/NEUBIAS/training-resources/refs/heads/master/_includes/tool_installation/image_data_formats_conda_env.yml`
- Activate the environment: `conda activate image_data_formats`
- Test the environment: `napari`
  - The napari image viewer should open; if this fails, check the below troubleshooting section or contact the instructors

##### Conda installation troubleshooting

- Remove the environment: `conda env remove -n image_data_formats`
- Delete any caches: `conda clean -all`
- Also remove cached packages: `rm -r ~/miniforge3/pkgs`
- Then try installing the environment again following the instructions above

### How to run this course

The current material allows to teach this course using Fiji and then command line interface, or using python. In our experience it works well to teach this course in 2 days. One day one, go through all modules using Fiji's graphical user interface, on day two repeat the material using python. Day two could be optional, only for people that are interested in python scripting.

### Previous editions of this course

For more details on how you may teach this course please check the detailed schedule of previous courses:

- [2025 EMBL Heidelberg](https://github.com/NEUBIAS/training-resources/blob/master/courses/2025_01_EMBL_image_data_formats.md)