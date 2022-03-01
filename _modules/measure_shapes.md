---
title:     Object shape measurements
layout:    module

prerequisites:
  - "[Connected component analysis](../connected_components)"
    
objectives:
  - Understand shape measurements and their limitations
  - Perform shape measurements on objects. 
  
motivation: >
 Our eyes are extremely good in distinguishing forms and patterns and this has proven to be a powerful tool for characterizing different 
 cell-types, functions, phenotypes, etc. In image processing, we use shape measurements (e.g. area, 
 volume, elongation, ...) for an automated and objective characterization of forms. Consequently, one can address
 scientific questions or filter objects that should be used for further processing. 
 Typically, we apply shape measurements on a labeled image. The labeled image, as obtained after a connected component analysis, 
 defines a set of objects in 2D/3D. 

concept_map: >
  graph LR
    li[Label Image] --> sa("Shape Analysis")
    li -.-> |"example <br> shape features"| ex["area (volume) <br> perimeter (surface)<br>circularity = 4 Pi A/P^2"]
    sa --> table("Results table")
    table --> object_rows["Rows are objects"]
    table --> feature_columns["Columns are shape features"]

figure: /figures/measure_shapes.jpg
figure_legend: 

activity_preface: |
    Open an image and perform shape measurements. Explain simple shape features (area, volume, perimeter) and some more complexes
    like circularity, elongation. Show that results can also be represented as an image.
 
activities:
    - ["ImageJ GUI", "measure_shapes/activities/measure_shapes_imagejgui.md", "markdown"]

exercises:
    - ["ImageJ GUI", "measure_shapes/exercises/measure_shapes_imagejgui.md"]

assessment: >

    ### True or false? Discuss with your neighbour      
       * Circularity is independent of image calibration.
       * Area is independent of image calibration.
       * Perimeter can strongly depend on spatial sampling.
       * Volume can strongly depend on spatial sampling.
       * Drawing test images to check how certain shape parameters behave is a good idea.
       
     > ## Solution
     > - Circularity is independent of image calibration **True**
     > - Area is independent of image calibration. **False**
     > - Perimeter can strongly depend on spatial sampling. **True**
     > - Volume can strongly depend on spatial sampling. **True**
     > - Drawing test images to check how certain shape parameters behave is a good idea. **True**
     {: .solution}

learn_next:
  - "[Workflow: Simple 2D object analysis](../workflow_segment_2d_nuclei_measure_shape)"
  - "[Object intensity meaurements](../measure_intensities)"


external_links:
    
    - "[Segmentation Annotator](https://github.com/tischi/segmentation-annotator#segmentation-annotator). Label mask and measurements exploration and annotation in ImageJ"
    - "[Wikipedia coastal line paradox](https://en.wikipedia.org/wiki/Coastline_paradox). Effect of Sampling and resolution on the measurements"
    - "[Results visualisation](https://imagej.net/MorphoLibJ#Grayscale_morphological_filters). Label visualization in 3D viewer"

---


