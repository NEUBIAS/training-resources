# Beginners course for python based image analysis using skimage and napari

## Why take this course


Fiji and the ImageJ macro language have served the life sciences for many years very well in terms of bioimage data inspection and analysis. However, there are some downsides to this ecosystem. One issue being that the ImageJ macro language is very specific to ImageJ and will not help you anywhere else. In addition, the ImageJ macro language misses many features of standard programming languages. Another issue is that many new image analysis algorithms, especially deep-learning based, are implemented in python, which is outside the Java based Fiji eco-system.

Taking this course will introduce you to using python for image analysis. This is useful because there is an already large and still growing number of python libraries for image analysis that you will get access to. In addition, learning python is useful in general as it currently is the most popular language for scientific computing. Moreover, since a few years a python based image visualisation tool, namely napari, exists that allows powerful and flexible n-dimensional image data visualisation, including overlay of segmentation and annotation layers.

## Prerequisites

Basic knowledge of the python programming language.

For example you should know how to

- assign variables
- call functions
- use arrays
- use a Jupyter Notebook to run some code

Such knowledge could be acquired for example here:

- TODO
- TODO

## Dates

2023 June 14, 15, 21, 22

## Location

TODO

## Trainers

- Nicola Gritti
- Christian Tischer
- Antonio Politi
- Tim-Oliver Buchholz


## Audience

- EMBL internal (all sites)
- MPI-NAT
- FMI-Basel??

## Content

### Image inspection basics

1. [Digital image basics](https://neubias.github.io/training-resources/pixels/index.html)
	- [issue](https://github.com/NEUBIAS/training-resources/issues/453)
1. [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)
1. [Spatial image calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html)
1. [Image data types](https://neubias.github.io/training-resources/datatypes/index.html)
1. [Image file formats](https://neubias.github.io/training-resources/image_file_formats/index.html)
	- [PR](https://github.com/NEUBIAS/training-resources/pull/462)
1. [Volume slicing](https://neubias.github.io/training-resources/volume_slicing/index.html)
	- [issue](https://github.com/NEUBIAS/training-resources/issues/409)
	- we could move some of this content to the `digital image basics`
1. [Image projections](https://neubias.github.io/training-resources/projections/index.html)
1. [Volume rendering](https://neubias.github.io/training-resources/volume_viewer/index.html)

### Image analysis basics

1. [Segmentation](https://neubias.github.io/training-resources/segmentation/index.html) DONE. Just generic concept.
1. [Manual segmentation](https://neubias.github.io/training-resources/manual_segmentation/index.html)
	- TODO work on Napari 2D/3D manual segmentation from scratch (AP) 
	- Add exercise for correction of labels (AP)
1. [Thresholding (Foreground background segmentation)](https://neubias.github.io/training-resources/binarization/index.html)
	- TODO test activity (AP)
	- Add more exercises (AP)
	- Migrate to new format multi activity (AP)
1. [Automatic thresholding (histogram-based)](https://neubias.github.io/training-resources/auto_threshold/index.html)
	- TODO create skimage part. (SG) #477
1. [Connected component labeling](https://neubias.github.io/training-resources/connected_components/index.html)
	- TODO test activity (AP)
	- TODO exercise (AP)
	- TODO migrate to new multiactivity (AP)
1. [Object shape measurements](https://neubias.github.io/training-resources/measure_shapes/index.html)
	- TODO create skimage part (DK)
	- TODO migrate to new multiactivity (DK)
1. Workflow: [Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
	- TODO create skimage part
1. [Image neighborhood filtering ](https://neubias.github.io/training-resources/filter_neighbourhood/index.html)
	- TODO create skimage part (DK)
1. [Median filter](https://neubias.github.io/training-resources/median_filter/index.html)
	- TODO create skimage part (DK)
1. [Object intensity measurements](https://neubias.github.io/training-resources/measure_intensities/index.html)
	- TODO create skimage-image  part
1. [Local background subtraction](https://neubias.github.io/training-resources/local_background_correction/index.html)
	- TODO create skimage part (NV)
1. [Morphological filters](https://neubias.github.io/training-resources/filter_morphological/index.html)
	- TODO create skimage-image  

### Maybe

1. Workflow: [2D noisy object segmentation and filtering](https://neubias.github.io/training-resources/workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/index.html)
	- TODO skimage part
