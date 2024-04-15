# Beginners course for python based image analysis using skimage and napari

## Why take this course

Fiji and the ImageJ macro language have served the life sciences for many years very well in terms of bioimage data inspection and analysis. However, there are some downsides to this ecosystem. One issue being that the ImageJ macro language is very specific to ImageJ and will not help you anywhere else. In addition, the ImageJ macro language misses many features of standard programming languages. Another issue is that many new image analysis algorithms, especially deep-learning based, are implemented in python, which is outside the Java based Fiji eco-system.

In this course, you will be introduced to essential concepts of image analysis. You will learn how to use python for image analysis and take advantage of the large and growing number of specialized python libraries. Learning python is useful in general because it is currently the most popular language for scientific computing and data science. In addition, since a few years a python based image visualisation tool, namely napari, exists that allows powerful and flexible n-dimensional image data visualisation, including overlay of segmentation and annotation layers.

## Prerequisites

* A computer for the online and the hands-on sessions. For the hands-on sessions ideally a laptop. 

* Basic knowledge of the python programming language
  * Concretely, please go through all the topics mentioned in the **Learn the Basics** section of the [Learn Python](https://www.learnpython.org/en/Welcome) website (you may skip "Classes and Objects" and "Modules and Packages").
  * In addition, please practice running code in a Jupyter Notebook. You can follow this [guide](https://jupyter.org/try-jupyter/retro/notebooks/?path=notebooks/Intro.ipynb).

If you want to use your own python installation for the course you need to perform the [tool installation](https://neubias.github.io/training-resources/tool_installation/index.html). Go to the `Show Activity` drop down menu and follow the instructions in `install skimage napari`. Test your installation. If you need help reach out to the corresponding trainer from your institute (see below).

You can use your own computer but we will also try to provide cloud computing with preinstalled software (TBA). 

## Dates

#### Course days

2024 TODO  June 6, 7, 13

## Schedule

Morning sessions (zoom lectures, zoom link will be announced)
- 10:00 - 11:00 Lecture and demo
- 11:00 - 11:15 Break
- 11:15 - 12:00 Lecture and demo

Afternoon sessions (in person at your institute, rooms will be announced)
- 14:00 - 16:00 Hands-on practicals

## Trainers

[Slide with pictures](https://docs.google.com/presentation/d/1duVwHr7owPKwSKBZYdprRaSHfELsJH--PmtUeJcrJAk/edit?usp=sharing)

- Antonio Politi (MPI Multidisciplinary Sciences)
- Tim-Oliver Buchholz (FMI Basel)
- Nicola Gritti (EMBL Barcelona)
- Luca Rappez (EMBL Barcelona)
- Jia Le Lim (EMBL Barcelona)
- Jonas Albers (EMBL Hamburg)
- Alvaro Crevenna (EMBL Rome)
- Daniele Ancora (EMBL Rome)
- Christian Tischer (EMBL Heidelberg)
- Arif Khan (EMBL Heidelberg)
- Sebastian Gonzalez (EMBL Heidelberg)
- Nima Vakili (EMBL Heidelberg)

## Teaching content

### Image inspection basics (day 1)

1. [Digital image basics](https://neubias.github.io/training-resources/pixels/index.html)
1. [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)
1. [Spatial image calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html) 
2. [N-dimensional images](https://neubias.github.io/training-resources/multidimensional_image_basics/index.html)
3. [Image data types](https://neubias.github.io/training-resources/datatypes/index.html) 
4. [Image projections](https://neubias.github.io/training-resources/projections/index.html)

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
