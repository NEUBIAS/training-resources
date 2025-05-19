# Image analysis course for beginners

## Why take this course

In this course, you will be introduced to essential concepts of image analysis.

### Motivation for python-based course
You will learn how to use python for image analysis and take advantage of the large and growing number of specialized python libraries. Learning python is useful in general because it is currently the most popular language for scientific computing and data science. In addition, since a few years a python based image visualisation tool, namely napari, exists that allows powerful and flexible n-dimensional image data visualisation, including overlay of segmentation and annotation layers.


### Motivation for Fiji-based course

## Prerequisites


### Python skimage napari
* Ideally, you should know all the topics mentioned in the **Learn the Basics** section of the [Learn Python](https://www.learnpython.org/en/Welcome) website (you may skip "Classes and Objects" and "Modules and Packages").
* If you have time, please practice running code in a Jupyter Notebook. You can follow this [guide](https://jupyter.org/try-jupyter/retro/notebooks/?path=notebooks/Intro.ipynb).

#### IT Setup
Please, before the course use the `conda` platform to install skimage and napari on your laptop, following [these instructions](https://neubias.github.io/training-resources/tool_installation/index.html#skimage_napari).


### Fiji macro/GUI

#### IT Setup

## Course overview



## Schedule

The course is comprised of:

- https://neubias.github.io/training-resources/basic-image-inspection-course/index.html
- https://neubias.github.io/training-resources/basic-image-analysis-course/index.html
- https://neubias.github.io/training-resources/basic-batch-analysis-course/index.html

The course is also [announced on the EMBL bio-it website](https://bio-it.embl.de/events/).  (Replace this with correct web address after creating a BIO IT course event)

- Day, hh:mm – hh:mm, Month DD, Year day 1
- Day, hh:mm – 16:00, Month DD, Year day 2
  .....
  .....


### Breaks
- This includes a lunch break (X hrs) and two coffee breaks (XX minutes), resulting in approximately X hr of teaching time.

As there are n modules per day that makes ~XX minutes per module.

## Venue

- e.g. EMBL Heidelberg

## Trainers and organisers

- Christian Tischer (EMBL)


## Teaching content

The whole course will be guided hands-on sessions.

### Image inspection basics (day 1)

Overview:

Trainers:

1. Welcome & trainer introduction
    -
1. [Installing image analysis software](https://neubias.github.io/training-resources/tool_installation/index.html)
    -
1. [Digital image basics](https://neubias.github.io/training-resources/pixels/index.html)
    -
1. [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)
    -
1. [Spatial image calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html)
    - Activities
       - [3-D spatial calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html#explore3D)
1. [N-dimensional images](https://neubias.github.io/training-resources/multidimensional_image_basics/index.html)
    -
1. [Image data types](https://neubias.github.io/training-resources/datatypes/index.html)
    - Activities
       - [Inspect an 8 bit image](https://neubias.github.io/training-resources/datatypes/index.html#saturation_8bit)
       - [Inspect a 12 bit image](https://neubias.github.io/training-resources/datatypes/index.html#saturation_12bit)
1. [Image projections](https://neubias.github.io/training-resources/projections/index.html)
    - [Max and sum projections of an anisotropic image]()

### Image analysis basics (day 2)

Overview:

Trainers:

1. [Segmentation](https://neubias.github.io/training-resources/segmentation/index.html)
    -
1. [Workflow: Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
    -
1. [Manual thresholding](https://neubias.github.io/training-resources/binarization/index.html)
    -
1. [Automated thresholding](https://neubias.github.io/training-resources/auto_threshold/index.html)
    -
1. [Connected component labeling](https://neubias.github.io/training-resources/connected_components/index.html)
    -
1. [Object shape measurements](https://neubias.github.io/training-resources/measure_shapes/index.html)
    -
1. [Workflow: Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
    - Ask students to try on their own!

### Image analysis basics (day 3)

Overview:

Trainers:

1. [Object intensity measurements](https://neubias.github.io/training-resources/measure_intensities/index.html)
    -
1. [Image neighborhood filtering](https://neubias.github.io/training-resources/filter_neighbourhood/index.html)
    -
1. [Median filter](https://neubias.github.io/training-resources/median_filter/index.html)
    -
1. [Local background subtraction](https://neubias.github.io/training-resources/local_background_correction/index.html)
    -
1. [Morphological filters](https://neubias.github.io/training-resources/filter_morphological/index.html)
    -
1. [Workflow: 2D noisy object segmentation and filtering](https://neubias.github.io/training-resources/workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/index.html)
    - Ask students to work through themselves...


### Batch image analysis basics (day 4)

Overview:

Trainers:

1. Introduce the general idea of batch processing
    - Ingredients: Loops, File paths, Functions, Data management, Results QC
1. [Loops](https://neubias.github.io/training-resources/script_for_loop/index.html)
    -
1. [String and path manipulations](https://neubias.github.io/training-resources/string_concat/index.html)
    -
1. [Functions](https://neubias.github.io/training-resources/script_functions/index.html)
    -
1. Discuss good practices for file and folder names
    -
1. [Batch analysis](https://neubias.github.io/training-resources/batch_processing/index.html)
    -
1. Batch inspection with MoBIE
    - Dominik
    - [Install Fiji/MoBIE](https://github.com/mobie/mobie-viewer-fiji?tab=readme-ov-file#install)
    - Ideally use the results from the above "batch analysis" module, alternatively [download and unzip these files](https://github.com/NEUBIAS/training-resources/raw/master/image_data/batch_process/inputs_and_outputs.zip)
    - Inspect the results table (e.g., drag and drop onto Fiji)
    - Open the data with MoBIE
        - `Plugins › MoBIE › Open › Open Table...`
        - If you downloaded the results you need to apply a path mapping
        - `IJ.run("Open Table...", "table=/Users/tischer/Downloads/batch_processing_in_and_output/batch_processing_results.csv images=image labels=labels pathmapping=/media/julian/Data/courses/2024_3_batch_processing,/Users/tischer/Downloads/batch_processing_in_and_output spatialcalibration=FromImage gridtype=Transformed");`
        
### Notes
- Trainers go slowly with workflow using GUI, answer questions
- Trainers go through it second time and have the macro recorder on
