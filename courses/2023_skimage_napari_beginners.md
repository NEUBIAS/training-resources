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

- Nicola Gritti
- Christian Tischer
- Antonio Politi
- Tim-Oliver Buchholz
- Arif Khan
- Sebastian Gonzalez
- Nima Vakili
- Luca Rappez

## Compute resources

Own computer or:

- EMBL: Jupyter Desktop (download all course material before) or own computer
- EMBL: BAND ??!!
- MPI-NAT: VMs 

## Teaching tips ??? REMOVE

Spent more time on motivating why one learns something. 

- Each module contains a "Motivation" section. Make sure to go through this and ask for questions!
- For Image Analysis, consider starting by giving an overview by means of a workflow [such as this one](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html); explain the biological context, and then teach the individual steps, the complete workflow could be homework.
- Maybe we also have such an idea for the Image Inspection teaching? A biologically motivated workflow that would require a sequence of image inspection skills to ve executed?! Maybe starting from some raw data and creating a visualisation to quantitatively compare some images, along with a folder of TIFF images with proper metadata and file and folder names?

## Content

### Image inspection basics

1. [Digital image basics](https://neubias.github.io/training-resources/pixels/index.html)
	- [issue](https://github.com/NEUBIAS/training-resources/issues/453)
2. [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)
    - Ready to merge  [PR #493](https://github.com/NEUBIAS/training-resources/pull/493)
    - Done Multiactivity PR 493
    - Done Exercise skimage napari PR 493
3. [Spatial image calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html) DONE
4. [Image data types](https://neubias.github.io/training-resources/datatypes/index.html) DONE
5. REMOVE? [Image file formats](https://neubias.github.io/training-resources/image_file_formats/index.html)
	- [PR #462](https://github.com/NEUBIAS/training-resources/pull/462)
	- TODO add activity that explains our `open_tiff` function (BO)
6. REMOVE? [Volume slicing](https://neubias.github.io/training-resources/volume_slicing/index.html)
	- [issue](https://github.com/NEUBIAS/training-resources/issues/409)
	- we could move some of this content to the `digital image basics`
7. KEEP? [Image projections](https://neubias.github.io/training-resources/projections/index.html)
8. REMOVE? [Volume rendering](https://neubias.github.io/training-resources/volume_viewer/index.html)

### Image analysis basics

1. EXPLANATION ONLY:[Segmentation](https://neubias.github.io/training-resources/segmentation/index.html) DONE. Just generic concept.
1. REMOVE? [Manual segmentation](https://neubias.github.io/training-resources/manual_segmentation/index.html)
	- TODO work on Napari 2D/3D manual segmentation from scratch (AP) 
	- Add exercise for correction of labels (AP)
1. [Thresholding (Foreground background segmentation)](https://neubias.github.io/training-resources/binarization/index.html) DONE
 	- Needs merge into master of [PR #313](https://github.com/NEUBIAS/training-resources/pull/313) 
3. [Automatic thresholding (histogram-based)](https://neubias.github.io/training-resources/auto_threshold/index.html) DONE
4. [Connected component labeling](https://neubias.github.io/training-resources/connected_components/index.html)
	- TODO test activity (AP)
	- TODO exercise (AP)
	- TODO migrate to new multiactivity (AP)
	- WIP [PR #485](https://github.com/NEUBIAS/training-resources/pull/485)
5. [Object shape measurements](https://neubias.github.io/training-resources/measure_shapes/index.html)
	- TODO create skimage part (DK)
	- TODO migrate to new multiactivity (DK)
6. Workflow: [Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html) DONE
7. [Image neighborhood filtering ](https://neubias.github.io/training-resources/filter_neighbourhood/index.html)
	- TODO create skimage part (DK)
8. [Median filter](https://neubias.github.io/training-resources/median_filter/index.html)
	- TODO create skimage part (DK)
9. [Object intensity measurements](https://neubias.github.io/training-resources/measure_intensities/index.html)
	- TODO create skimage-image part (NG)
10. [Local background subtraction](https://neubias.github.io/training-resources/local_background_correction/index.html)
	- TODO create skimage part (NV)
11. [Morphological filters](https://neubias.github.io/training-resources/filter_morphological/index.html)
	- TODO create skimage-image (NG)

### Maybe

1. Workflow: [2D noisy object segmentation and filtering](https://neubias.github.io/training-resources/workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/index.html)
	- TODO skimage part
