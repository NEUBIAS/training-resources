# Beginners course for python based image analysis using skimage and napari

## Why take this course

Fiji and the ImageJ macro language have served the life sciences for many years very well in terms of bioimage data inspection and analysis. However, there are some downsides to this ecosystem. One issue being that the ImageJ macro language is very specific to ImageJ and will not help you anywhere else. In addition, the ImageJ macro language misses many features of standard programming languages. Another issue is that many new image analysis algorithms, especially deep-learning based, are implemented in python, which is outside the Java based Fiji eco-system.

In this course, you will be introduced to essential concepts of image analysis. You will learn how to use python for image analysis and take advantage of the large and growing number of specialized python libraries. Learning python is useful in general because it is currently the most popular language for scientific computing and data science. In addition, since a few years a python based image visualisation tool, namely napari, exists that allows powerful and flexible n-dimensional image data visualisation, including overlay of segmentation and annotation layers.

## Prerequisites

* Ideally, you should know all the topics mentioned in the **Learn the Basics** section of the [Learn Python](https://www.learnpython.org/en/Welcome) website (you may skip "Classes and Objects" and "Modules and Packages").
* If you have time, please practice running code in a Jupyter Notebook. You can follow this [guide](https://jupyter.org/try-jupyter/retro/notebooks/?path=notebooks/Intro.ipynb).

### IT Setup

Please, before the course use the `conda` platform to install skimage and napari on your laptop, following [these instructions](https://neubias.github.io/training-resources/tool_installation/index.html#skimage_napari). 

## Schedule

The course is combining these three courses:

- https://neubias.github.io/training-resources/basic-image-inspection-course/index.html
- https://neubias.github.io/training-resources/basic-image-analysis-course/index.html
- https://neubias.github.io/training-resources/basic-batch-analysis-course/index.html

The course is also [announced on the EMBL bio-it website](https://bio-it.embl.de/events/basics-of-bioimage-analysis-in-python-3/).

- Monday, 9:30 – 16:00, April 28, 2025 day 1
- Tuesday, 9:30 – 16:00, April 29, 2025 day 2
- Monday, 9:30 – 16:00, May 05, 2025 day 3
- Tuesday,9:30 – 16:00, May 06, 2025 day 4

This includes a lunch break (1 hr) and two coffee breaks (20 minutes), resulting in approximately 5 hr of teaching time.

As there are 6 modules per day that makes ~45 minutes per module.

## Venue

- EMBL Heidelberg

## Trainers and organisers

- Severina Klaus (Uni Heidelberg)
- Felix Schneider (EMBL)
- Dominik Kutra (EMBL)
- Christian Tischer (EMBL)
- Arif Khan (EMBL)
- Julian Hennies (EMBL)

## Teaching content

The whole course will be guided hands-on sessions. 

### Image inspection basics (day 1)

1. [Digital image basics](https://neubias.github.io/training-resources/pixels/index.html)
    - Felix Schneider 
1. [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)
    - Felix Schneider
1. [Spatial image calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html) 
    - Christian Tischer
    - Activities
       - [3-D spatial calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html#explore3D)
1. [N-dimensional images](https://neubias.github.io/training-resources/multidimensional_image_basics/index.html)
    - Arif Khan
1. [Image data types](https://neubias.github.io/training-resources/datatypes/index.html) 
    - Christian Tischer
    - Activities
       - [Inspect an 8 bit image](https://neubias.github.io/training-resources/datatypes/index.html#saturation_8bit)
       - [Inspect a 12 bit image](https://neubias.github.io/training-resources/datatypes/index.html#saturation_12bit)
1. [Image projections](https://neubias.github.io/training-resources/projections/index.html)
    - Christian Tischer
    - [Max and sum projections of an anisotropic image]()

### Image analysis basics (day 2)

1. [Segmentation](https://neubias.github.io/training-resources/segmentation/index.html)
    - Arif Khan
1. [Workflow: Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
    - Arif Khan
    - Only discuss the figure:
        - The most basic segmentation workflow
        - The components of this workflow will be taught now
1. [Manual thresholding](https://neubias.github.io/training-resources/binarization/index.html)
    - Arif Khan
1. [Automated thresholding](https://neubias.github.io/training-resources/auto_threshold/index.html) 
    - Julian Hennies
1. [Connected component labeling](https://neubias.github.io/training-resources/connected_components/index.html)
    - Julian Hennies
1. [Object shape measurements](https://neubias.github.io/training-resources/measure_shapes/index.html)
    - Christian Tischer
1. [Workflow: Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
    - Christian Tischer

### Image analysis basics (day 3)

1. [Object intensity measurements](https://neubias.github.io/training-resources/measure_intensities/index.html)
    - Severina Klaus
1. [Image neighborhood filtering](https://neubias.github.io/training-resources/filter_neighbourhood/index.html)
    - Severina Klaus
1. [Median filter](https://neubias.github.io/training-resources/median_filter/index.html)
    - Julian Hennies
1. [Local background subtraction](https://neubias.github.io/training-resources/local_background_correction/index.html)
    - Julian Hennies 
1. [Morphological filters](https://neubias.github.io/training-resources/filter_morphological/index.html)
    - Julian Hennies
1. [Batch processing](https://neubias.github.io/training-resources/batch_processing/index.html)
    - Julian Hennies
1. [Workflow: 2D noisy object segmentation and filtering](https://neubias.github.io/training-resources/workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/index.html)
    - Julian Hennies


### Batch image analysis basics (day 4)

1. Introduce the general idea of batch processing
    - Christian Tischer
    - Ingredients: Loops, File paths, Functions, Data management, Results QC
1. [Loops](https://neubias.github.io/training-resources/script_for_loop/index.html)
    - Felix Schneider
1. [String and path manipulations](https://neubias.github.io/training-resources/string_concat/index.html)
    - Dominik Kutra
1. [Functions](https://neubias.github.io/training-resources/script_functions/index.html)
    - Christian Tischer
1. Discuss good practices for file and folder names
    - Christian Tischer
    - Discuss https://git.embl.de/grp-cba/astrocyte-differentiations/-/blob/main/data_management.md
1. [Batch analysis](https://neubias.github.io/training-resources/batch_processing/index.html)
    - Julian Hennies
1. Batch inspection with MoBIE
    - Christian Tischer
    - [Install Fiji/MoBIE](https://github.com/mobie/mobie-viewer-fiji?tab=readme-ov-file#install)
    - Ideally use the results from the above "batch analysis" module, alternatively [download and unzip these files](https://github.com/NEUBIAS/training-resources/raw/master/image_data/batch_process/inputs_and_outputs.zip)
    - Inspect the results table (e.g., drag and drop onto Fiji)
    - Open the data with MoBIE
        - `Plugins › MoBIE › Open › Open Table...`
        - If you downloaded the results you need to apply a path mapping
        - `IJ.run("Open Table...", "table=/Users/tischer/Downloads/batch_processing_in_and_output/batch_processing_results.csv images=image labels=labels pathmapping=/media/julian/Data/courses/2024_3_batch_processing,/Users/tischer/Downloads/batch_processing_in_and_output spatialcalibration=FromImage gridtype=Transformed");`

