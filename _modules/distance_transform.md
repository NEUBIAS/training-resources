---
title: Distance transform
layout: module
tags: ["draft"]
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Data types](../datatypes)"
  - "[Segmentation](../segmentation)"
objectives:
  - Understand how to use distance transform to quantify morphology of objects 
  - Understand how to use distance transform to quantify distance between objects
  - Understand approximate nature of distance transform
  
motivation: |
  We use distance transform to quantify how a structure of interest is away from object boundaries or other structures. The distance transform is also use to characterize the morphology of an object in 2D and 3D, find its center, dimensions, etc.. Finally distance transform can be used as a pre-processing step to improve the segmentation results and split touching objects. 
 
concept_map: >
  graph TD
    B[Binary image] --> DT(Distance transform)
    DT --> D["Distance map image"]
    D -- contains --- DN("Distances to nearest background pixel")
    D -- is --- A("Approximation of euclidian distance")
    DT -- has --- VI("Various implementations")


figure: /figures/distance_transform.png
figure_legend: Upper panel - Binary image and the corresponding distance map. The distance map has three local maxima, which are very useful for object splitting and defining object centers. Lower panel - Inverted binary image and corresponding distance map, which is useful to compute distances to closest objects.

activity_preface: |
  ### Distance transform basics
    - Open label mask [xy_8bit_binary__dist_trafo_a.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__dist_trafo_a/xy_8bit_binary__dist_trafo_a.tif).
    - Perform a distance transform.
    - Invert the binary input image.
    - Perform another distance transform on the new binary image.
    - Observe that the datatype (in particular 8-bit) of the distance transform image limits the distances.
    - Discuss different metrics.
    - Add a calibration to the inverted image and recompute the distance transform.
    - Observe whether the image calibration is considered for the distances.
  
  ### Distance measurements
    - Open label mask: [xy_8bit_labels__dist_trafo_b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__dist_trafo_b.tif).
    - Create an inverted binary mask for one of the labels (e.g. label 1)
    - Compute the distance transform
    - Measure intensity (= distances to nearest other objects) of objects in the distance map
    - Show that the measured values correspond to the distance of label 2 and 3 to label 1. 
    
  ### Region selection by distance gating
    - Open reference object image: [xy_8bit_binary__single_object.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__single_object.tif).
    - Invert the binary
    - Compute the distance transform
    - Perform an intensity gating on the distance map, e.g. by thresholding, to create a mask with all pixels of a certain distance, e.g. between 100-120, to the reference object.
  
activities:
  - ["Basics, ImageJ GUI MorpholibJ", "distance_transform/activities/distance_transform_basics_imagejgui.md", "markdown"]
  - ["Basics, ImageJ Macro MorpholibJ", "distance_transform/activities/distance_transform_basics_imagejmacro.ijm", "java"]
  - ["Measure, ImageJ Macro MorpholibJ", "distance_transform/activities/distance_transform_measure_imagejmacro.ijm", "java"]
  - ["Region selection, ImageJ Macro MorpholibJ", "distance_transform/activities/distance_transform_region_selection_imagejmacro.ijm", "java"]
  - ["Python Napari", "distance_transform/activities/distance_transform_napari_skimage.py", "python"]

exercise_preface: |
  ### Measure distance to center of cell
   We would like to measure the distance within a binary mask to a specific point in the cell. This is called Geodesic distance. 
   
    * Use [xy_8bit_glialcell.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__glialcell.tif) and the corresponding binary image [xy_8bit_binary__glialcell.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__glialcell/xy_8bit_binary__glialcell.tif)
    * Compute the geodesic distance map of the binary image with respect to a reference point close to the soma of the cell (approx x_pixel = 88, y_pixel = 74)
    
  ### Measure thickness of glial branches
   The goal is to combine skeletonization and distance map computation to measure skeleton branch length and thickness. For this exercise you need the binary image [xy_8bit_binary__glialcell.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__glialcell/xy_8bit_binary__glialcell.tif) and the skeletonized and normalized version [xy_8bit_binary__glialcell_skeleton.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__glialcell/xy_8bit_binary__glialcell_skeleton.tif)
    
   - Compute the distance transform of the binary
   - Normalize the skeleton image and multiply it with the distance map
   - Perform an analyze of the skeleton

exercises:
  - ["Distance to center, ImageJ GUI", "distance_transform/exercises/distance_transform_geodesic_imagejgui.md"]
  - ["Glial thickness, ImageJ GUI", "distance_transform/exercises/distance_transform_skeldist_imagejgui.md"]

assessment: >
 ### Discuss with your neighbor 

  1. Knowing the image calibration, how could we convert a 2D distance map to physical values?
  2. Knowing the image calibration, how could we convert a 3D distance map to physical values? Is it important if the image is isotropic sampled or not?

   
learn_next: >

external_links:
  - "[Wikipedia: Dist](https://en.wikipedia.org/wiki/Binary_image)"
  - "[MorpholibJ manual v1.4.0](https://github.com/ijpb/MorphoLibJ/releases/download/v1.4.0/MorphoLibJ-manual-v1.4.0.pdf)"
  - "[Borgefors 1984](https://www.sciencedirect.com/science/article/pii/0734189X84900355)"
  - "[Borgefors 1986](https://www.sciencedirect.com/science/article/pii/S0734189X86800470)"
---

#### Chamfer distance (modified from MorpholibJ Manual)

<img src="../figures/chamfer_weights.png" align ="center" width="100%" >

Several methods (metrics) exist for computing distance maps. The MorphoLibJ library implements
distance transforms based on chamfer distances. Chamfer distances approximate Euclidean
distances with integer weights, and are simpler to compute than exact Euclidean distance
(Borgefors, 1984, 1986). As chamfer weights are only an approximation of the real Euclidean
distance, some differences are expected compared to the actual Euclidean distance map.

Several choices for chamfer weights are illustrated in above Figure (showing the not normalized distance). 

 - The "Chessboard" distance, also named Chebyshev distance, gives the number of moves that an imaginary Chess-king needs to reach a specific pixel. A king can move one pixel in each direction. 
 - The "City-block" distance, also named Manhattan metric, weights diagonal moves differently. 
 - The “Borgefors” weights were claimed to be best approximation when considering the 3-by-3 neighborhood.
 - The “Chess knight” distance also takes into account the pixels located at a distance from
(±1, ±2) in any direction. It is usually the best choice, as it considers a larger neighborhood.

To remove the scaling effect due to weights > 1, it is necessary to perform a normalization step. In MorphoLibJ this is performed by dividing the resulting image by the first weight (option `Normalize weights`).


