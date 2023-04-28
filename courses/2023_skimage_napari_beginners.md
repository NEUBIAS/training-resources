# Beginners course for python based image analysis using skimage and napari

## Why take this course

Fiji and the ImageJ macro language have served the life sciences for many years very well in terms of bioimage data inspection and analysis. However, there are some downsides to this ecosystem. One issue being that the ImageJ macro language is very specific to ImageJ and will not help you anywhere else. In addition, the ImageJ macro language misses many features of standard programming languages. Another issue is that many new image analysis algorithms, especially deep-learning based, are implemented in python, which is outside the Java based Fiji eco-system.

Taking this course will introduce you to using python for image analysis. This is useful because there is an already large and still growing number of python libraries for image analysis that you will get access to. In addition, learning python is useful in general as it currently is the most popular language for scientific computing and data science. Moreover, since a few years a python based image visualisation tool, namely napari, exists that allows powerful and flexible n-dimensional image data visualisation, including overlay of segmentation and annotation layers.

## Prerequisites

Basic knowledge of the python programming language.

For example you should know how to
- use conda environments ???
- assign variables
- call functions
- allocate and index simple numpy arrays
- use a Jupyter Notebook to run some python code

Concretely, you should be able to run and understand this script: TODO

Such knowledge could be acquired for example here:

- [Learn Python](https://www.learnpython.org/en/Welcome)
- [Software carpentry](https://swcarpentry.github.io/python-novice-inflammation/)
- https://wiki.python.org/moin/BeginnersGuide/Programmers, this is an extensive list of sites for learning python

If you want to use your own computer for the course you need to perform the [tool installation](https://neubias.github.io/training-resources/tool_installation/index.html). Go to the `Show Activity` drop down menu and follow the instructions in `install skimage napari`. Test your installation. 

In addition, we are working on providing you with cloud computers where all software is preinstalled.

## Dates

#### Installation day

Each institute decides on their own.

#### Course days

2023 June 6, 7, 13

## Schedule

Morning sessions (zoom lectures, zoom link will be announced)
- 10:00 - 11:00 Lecture and demo
- 11:00 - 11:15 Break
- 11:15 - 12:00 Lecture and demo

Afternoon sessions (in person at your institute, rooms will be announced)
- 14:00 - 16:00 Hands-on practicals

## Trainers

- Antonio Politi (MPI Multidisciplinary Sciences)
- Tim-Oliver Buchholz (FMI Basel)
- Nicola Gritti (EMBL Barcelona)
- Luca Rappez (EMBL Barcelona)
- Jonas Albers (EMBL Hamburg)
- Alvaro Crevenna (EMBL Rome)
- Daniele Ancora (EMBL Rome)
- Christian Tischer (EMBL Heidelberg)
- Arif Khan (EMBL Heidelberg)
- Sebastian Gonzalez (EMBL Heidelberg)
- Nima Vakili (EMBL Heidelberg)

## Compute resources

You can use your own computer but we will also try to provide cloud computing with preinstalled software (TBA).

## Teaching content

### Image inspection basics (day 1)

1. [Digital image basics](https://neubias.github.io/training-resources/pixels/index.html)
1. [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)
1. [Spatial image calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html) 
1. [Image data types](https://neubias.github.io/training-resources/datatypes/index.html) 
1. [Image projections](https://neubias.github.io/training-resources/projections/index.html)

### Image analysis basics (day 2)

1. [Segmentation](https://neubias.github.io/training-resources/segmentation/index.html)
1. [Manual thresholding](https://neubias.github.io/training-resources/binarization/index.html)
1. [Automated thresholding](https://neubias.github.io/training-resources/auto_threshold/index.html) 
1. [Connected component labeling](https://neubias.github.io/training-resources/connected_components/index.html)
1. [Object shape measurements](https://neubias.github.io/training-resources/measure_shapes/index.html)
1. [Workflow: Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)

### Image analysis basics (day 3)

1. [Image neighborhood filtering](https://neubias.github.io/training-resources/filter_neighbourhood/index.html)
1. [Median filter](https://neubias.github.io/training-resources/median_filter/index.html)
1. [Object intensity measurements](https://neubias.github.io/training-resources/measure_intensities/index.html)
1. [Local background subtraction](https://neubias.github.io/training-resources/local_background_correction/index.html)
1. [Morphological filters](https://neubias.github.io/training-resources/filter_morphological/index.html)
1. [Workflow: 2D noisy object segmentation and filtering](https://neubias.github.io/training-resources/workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/index.html)
