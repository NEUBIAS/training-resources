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
- Tuesday, 9:30 – 16:00, May 06, 2025 day 4

This includes a lunch break (1 hr) and two coffee breaks (20 minutes), resulting in approximately 5 hr of teaching time.

As there are 6 modules per day that makes ~45 minutes per module.

## Venue

- EMBL Heidelberg

## Trainers and organisers

- Severina Klaus (Uni Heidelberg)
- Ehud Sivan (Weizmann)
- Felix Schneider (EMBL)
- Dominik Kutra (EMBL)
- Christian Tischer (EMBL)
- Arif Khan (EMBL)
- Julian Hennies (EMBL)
- Alessandro Ulivi (Uni Heidelberg)

## Teaching content

The whole course will be guided hands-on sessions. 

### Image inspection basics (day 1, 28. April 2025)

Trainers: Christian Tischer, Julian Hennies, Felix Schneider

1. Welcome & trainer introduction
    - Felix, Julian, Christian
1. [Installing python software via conda](https://neubias.github.io/training-resources/tool_installation/index.html)
    - T: Christian, A: Felix, Julian, 
1. [Digital image basics](https://neubias.github.io/training-resources/pixels/index.html)
    - T: Felix, A: Julian, Christian
1. [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)
    - T: Felix, A: Julian, Christian
1. [Spatial image calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html) 
    - T: Julian, A: Christian, Felix
    - Activities
       - [3-D spatial calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html#explore3D)
1. [N-dimensional images](https://neubias.github.io/training-resources/multidimensional_image_basics/index.html)
    - T: Julian, A: Christian, Felix
1. [Image data types](https://neubias.github.io/training-resources/datatypes/index.html) 
    - T: Christian, A: Julian, Felix
    - Activities
       - [Inspect an 8 bit image](https://neubias.github.io/training-resources/datatypes/index.html#saturation_8bit)
       - [Inspect a 12 bit image](https://neubias.github.io/training-resources/datatypes/index.html#saturation_12bit)
1. [Image projections](https://neubias.github.io/training-resources/projections/index.html)
    - T: Christian, A: Julian, Felix
    - [Max and sum projections of an anisotropic image]()

### Image analysis basics (day 2, 29. April 2025)

Trainers: Felix Schneider, Julian Hennies, Severina Klaus

1. [Segmentation](https://neubias.github.io/training-resources/segmentation/index.html)
    - Julian
    - Just show the figure!
1. [Workflow: Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
    - Julian
    - Just show the figure!
    - Only discuss the figure to motivate the day:
        - The most basic segmentation workflow
        - The components of this workflow will be taught now
1. [Manual thresholding](https://neubias.github.io/training-resources/binarization/index.html)
    - Julian
1. [Automated thresholding](https://neubias.github.io/training-resources/auto_threshold/index.html) 
    - Severina
1. [Connected component labeling](https://neubias.github.io/training-resources/connected_components/index.html)
    - Severina
1. [Object shape measurements](https://neubias.github.io/training-resources/measure_shapes/index.html)
    - Felix
1. [Workflow: Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
    - Felix: Ask students to try on their own! 

### Image analysis basics (day 3, 5. May 2025)

Trainers: Severina Klaus (in the morning), Arif Khan, Alessandro Ulivi

1. [Object intensity measurements](https://neubias.github.io/training-resources/measure_intensities/index.html)
    - Severina 
1. [Image neighborhood filtering](https://neubias.github.io/training-resources/filter_neighbourhood/index.html)
    - Severina 
1. [Median filter](https://neubias.github.io/training-resources/median_filter/index.html)
    - Alessandro 
1. [Local background subtraction](https://neubias.github.io/training-resources/local_background_correction/index.html)
    - Alessandro 
1. [Morphological filters](https://neubias.github.io/training-resources/filter_morphological/index.html)
    - Arif
1. [Workflow: 2D noisy object segmentation and filtering](https://neubias.github.io/training-resources/workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/index.html)
    - Arif, Ask students to work through themselves...


### Batch image analysis basics (day 4, 6. May 2025)

Trainers: Dominik Kutra, Ehud Sivan, Arif Khan, Alessandro Ulivi

1. Introduce the general idea of batch processing
    - Arif
    - Ingredients: Loops, File paths, Functions, Data management, Results QC
1. [Loops](https://neubias.github.io/training-resources/script_for_loop/index.html)
    - Arif
    - Ehud
1. [String and path manipulations](https://neubias.github.io/training-resources/string_concat/index.html)
    - Alessandro
    - Ehud
1. [Functions](https://neubias.github.io/training-resources/script_functions/index.html)
    - Alessandro
    - Ehud
1. Discuss good practices for file and folder names
    - Dominik 
    - Discuss https://git.embl.de/grp-cba/astrocyte-differentiations/-/blob/main/data_management.md
1. [Batch analysis](https://neubias.github.io/training-resources/batch_processing/index.html)
    - Dominik
    - Ehud
1. Batch inspection with MoBIE
    - Dominik 
    - [Install Fiji/MoBIE](https://github.com/mobie/mobie-viewer-fiji?tab=readme-ov-file#install)
    - Ideally use the results from the above "batch analysis" module, alternatively [download and unzip these files](https://github.com/NEUBIAS/training-resources/raw/master/image_data/batch_process/inputs_and_outputs.zip)
    - Inspect the results table (e.g., drag and drop onto Fiji)
    - Open the data with MoBIE
        - `Plugins › MoBIE › Open › Open Table...`
        - If you downloaded the results you need to apply a path mapping
        - `IJ.run("Open Table...", "table=/Users/tischer/Downloads/batch_processing_in_and_output/batch_processing_results.csv images=image labels=labels pathmapping=/media/julian/Data/courses/2024_3_batch_processing,/Users/tischer/Downloads/batch_processing_in_and_output spatialcalibration=FromImage gridtype=Transformed");`

