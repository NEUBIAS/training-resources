# Beginners course for python based image analysis using skimage and napari

## Why take this course

Fiji and the ImageJ macro language have served the life sciences for many years very well in terms of bioimage data inspection and analysis. However, there are some downsides to this ecosystem. One issue being that the ImageJ macro language is very specific to ImageJ and will not help you anywhere else. In addition, the ImageJ macro language misses many features of standard programming languages. Another issue is that many new image analysis algorithms, especially deep-learning based, are usually first implemented in python, which is outside the Java based Fiji eco-system.

In this course, you will be introduced to essential concepts of image analysis. You will learn how to use python for image analysis and take advantage of the large and growing number of specialized python libraries. Learning python is useful in general because it is currently the most popular language for scientific computing and data science. In addition, since a few years a python based image visualisation tool, namely napari, exists that allows powerful and flexible n-dimensional image data visualisation, including overlay of segmentation and annotation layers.

## Prerequisites

* Ideally, you should know all the topics mentioned in the **Learn the Basics** section of the [Learn Python](https://www.learnpython.org/en/Welcome) website (you may skip "Classes and Objects" and "Modules and Packages").
* If you have time, please practice running code in a Jupyter Notebook. 

### IT Setup

You will be guided on how to set up your python platform and how to install the necessary modules on day 0 of the course.  

If you are already proficient with python and do not need to revisit the basics, please make sure to use the `conda` platform to install skimage and napari on your laptop before the course, following [these instructions (Install skimage & napari)](https://neubias.github.io/training-resources/tool_installation/index.html#skimage_napari). 

## Schedule

The whole course will be guided hands-on sessions.

- Monday 06.10.2025 10:00 - 17:00
- Tuesday 07.10.2025 10:00 - 17:00
- Monday 13.10.2025 10:00 - 17:00
- Tuesday 14.10.2025 10:00 - 17:00 

This includes a lunch break (1 hr) and two coffee breaks (20 minutes), resulting in approximately 5 hr of teaching time, covering 5-7 modules of different lengths.

## Venue

- Big seminar room in the ground floor of the Center for Integrative Infectious Disease Research, Uni Heidelberg, INF 344, Heidelberg, Germany
- This workshop will be in person only

## Trainers and organisers

- Severina Klaus (Uni Heidelberg)
- Charlotte Kaplan (Uni Heidelberg)
- Alessandro Ulivi (Uni Heidelberg)
- Felix Schneider (EMBL)
- Christian Tischer (EMBL)
- Arif Khan (EMBL)
- Julian Hennies (EMBL)

## Teaching content

### Python and image inspection basics (day 1)

The first half of the day is organized as an onboarding and refresh session to bring everyone to the same level on basic python programming. If you are already proficient with python, you may skip this part. In this case, please make sure to use the `conda` platform to install skimage and napari on your laptop before the course, following [these instructions (Install skimage & napari)](https://neubias.github.io/training-resources/tool_installation/index.html#skimage_napari). 

1. Participants introduce themselves, where they work, why they joined the course, and what previous experience they have
1. Trainers introduce themselves, where they work and how they are competent
1. Introduction to python and basic environment management
1. [Tool installations](https://neubias.github.io/training-resources/tool_installation/index.html#skimage_napari).
   - Severina Klaus
1. [Basics of python programming](https://heibox.uni-heidelberg.de/d/da0a61ef203347c7aff2/)
   - Charlotte Kaplan
       - Jupyter notebook/ lab
       - Data types: integer, float, lists
       - Basic operations
       - Variables
       - Modules
1. [Digital image basics](https://neubias.github.io/training-resources/pixels/index.html)
    - tbd
1. [Image data types](https://neubias.github.io/training-resources/datatypes/index.html) 
    - tbd
1. [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)
    - tbd

### Image inspection and analysis basics (day 2)

1. Introduction
    - New trainers introduce themselves at the start of their modules
1. [Spatial image calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html) 
    - tbd
1. [N-dimensional images](https://neubias.github.io/training-resources/multidimensional_image_basics/)
    - tbd
1. [Image projections](https://neubias.github.io/training-resources/projections/index.html)
    - tbd
1. [Image neighborhood filtering](https://neubias.github.io/training-resources/filter_neighbourhood/index.html)
    - tbd
1. [Statistical (rank) filtering](https://neubias.github.io/training-resources/filter_statistical/index.html)
    - tbd
1. [Local background subtraction](https://neubias.github.io/training-resources/local_background_correction/index.html)
    - tbd

### Image analysis basics (day 3)
1. Introduction
    - New trainers introduce themselves at the start of their modules
1. [Segmentation](https://neubias.github.io/training-resources/segmentation/index.html)
    - tbd
1. [Workflow: Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
    - tbd
    - Only discuss the figure:
        - The most basic segmentation workflow
        - The components of this workflow will be taught now
1. [Manual thresholding](https://neubias.github.io/training-resources/binarization/index.html)
    - tbd
1. [Automated thresholding](https://neubias.github.io/training-resources/auto_threshold/index.html) 
    - tbd
1. [Connected component labeling](https://neubias.github.io/training-resources/connected_components/index.html)
    - tbd
1. [Morphological filters](https://neubias.github.io/training-resources/filter_morphological/index.html)
    - tbd
1. [Object shape measurements](https://neubias.github.io/training-resources/measure_shapes/index.html)
    - tbd
1. [Object intensity measurements](https://neubias.github.io/training-resources/measure_intensities/index.html)
    - tbd
1. [Practical exercise - Workflow: Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
    - tbd

### Image analysis and batch processing (day 4)
1. Introduction
    - New trainers introduce themselves at the start of their modules
1. [Batch processing](https://neubias.github.io/training-resources/batch_processing/index.html)
    - Introduce the general idea of batch processing
    - tbd
1. [Loops](https://neubias.github.io/training-resources/script_for_loop/index.html)
    - tbd
1. [Strings and path manipulation](https://neubias.github.io/training-resources/string_concat/index.html)
    - tbd
1. [Functions](https://neubias.github.io/training-resources/script_functions/index.html)
    - tbd
1. [Saving images]
    - tbd
1. [Practical exercise - Workflow: Batch processing](https://neubias.github.io/training-resources/batch_processing/index.html)
    - tbd
1. [Summary of what was learned]




