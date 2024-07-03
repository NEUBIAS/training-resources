# Beginners course for python based image analysis using skimage and napari

## Why take this course

Fiji and the ImageJ macro language have served the life sciences for many years very well in terms of bioimage data inspection and analysis. However, there are some downsides to this ecosystem. One issue being that the ImageJ macro language is very specific to ImageJ and will not help you anywhere else. In addition, the ImageJ macro language misses many features of standard programming languages. Another issue is that many new image analysis algorithms, especially deep-learning based, are implemented in python, which is outside the Java based Fiji eco-system.

In this course, you will be introduced to essential concepts of image analysis. You will learn how to use python for image analysis and take advantage of the large and growing number of specialized python libraries. Learning python is useful in general because it is currently the most popular language for scientific computing and data science. In addition, since a few years a python based image visualisation tool, namely napari, exists that allows powerful and flexible n-dimensional image data visualisation, including overlay of segmentation and annotation layers.

## Prerequisites

* You should know all the topics mentioned in the **Learn the Basics** section of the [Learn Python](https://www.learnpython.org/en/Welcome) website (you may skip "Classes and Objects" and "Modules and Packages").
* Please practice running code in a Jupyter Notebook. You can follow this [guide](https://jupyter.org/try-jupyter/retro/notebooks/?path=notebooks/Intro.ipynb).

### IT Setup

Please, before the course use the `conda` platform to install skimage and napari on your laptop, following [these instructions](https://neubias.github.io/training-resources/tool_installation/index.html#skimage_napari). 

## Schedule

The whole course will be guided hands-on sessions.

- Day, Month, Year, Times

This includes a lunch break (1 hr) and two coffee breaks (20 minutes), resulting in approximately 5 hr of teaching time.
As there are 6 modules per day that makes ~45 minutes per module.

## Venue

- Country, City, Street, Institute, Room
- Zoom link

## Trainers and organisers

- Name (Institute)
- ...

## Teaching tips

Dear Trainers, please consider checking these [teaching tips](https://github.com/NEUBIAS/training-resources/blob/master/TEACHING_TIPS.md).

## Teaching content

### Image inspection basics (day 1)

1. Introduction
    - Trainers introduce themselves, where they work and how they are competent
    - Participants introduce themselves, where they work, why they joined the course, and what previous experience they have
        - Depending on the number of participants, one could distribute the introductions across the course, e.g. do some in the morning and some in the afternoon
1. [Digital image basics](https://neubias.github.io/training-resources/pixels/index.html)
    - Trainer 
1. [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)
    - Trainer
1. [Spatial image calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html) 
    - Trainer
1. [N-dimensional images](https://neubias.github.io/training-resources/multidimensional_image_basics/index.html)
    - Trainer
1. [Image data types](https://neubias.github.io/training-resources/datatypes/index.html) 
    - Trainer
1. [Image projections](https://neubias.github.io/training-resources/projections/index.html)
    - Trainer

### Image analysis basics (day 2)

1. [Segmentation](https://neubias.github.io/training-resources/segmentation/index.html)
    - Trainer
1. [Manual thresholding](https://neubias.github.io/training-resources/binarization/index.html)
    - Trainer
1. [Automated thresholding](https://neubias.github.io/training-resources/auto_threshold/index.html) 
    - Trainer
1. [Connected component labeling](https://neubias.github.io/training-resources/connected_components/index.html)
    - Trainer
1. [Object shape measurements](https://neubias.github.io/training-resources/measure_shapes/index.html)
    - Trainer
1. [Workflow: Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
    - Trainer

### Image analysis basics (day 3)

1. [Object intensity measurements](https://neubias.github.io/training-resources/measure_intensities/index.html)
    - Trainer
1. [Image neighborhood filtering](https://neubias.github.io/training-resources/filter_neighbourhood/index.html)
    - Trainer
1. [Median filter](https://neubias.github.io/training-resources/median_filter/index.html)
    - Trainer
1. [Local background subtraction](https://neubias.github.io/training-resources/local_background_correction/index.html)
    - Trainer 
1. [Morphological filters](https://neubias.github.io/training-resources/filter_morphological/index.html)
    - Trainer
1. [Workflow: 2D noisy object segmentation and filtering](https://neubias.github.io/training-resources/workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/index.html)
    - Trainer


## What to learn/teach next?

- It could make sense to follow this course up (or extend it) with some modules about batch analysis

