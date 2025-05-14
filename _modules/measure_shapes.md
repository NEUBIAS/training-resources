---
title:     Object shape measurements
layout:    module

prerequisites:
  - "[Connected component analysis](../connected_components)(for practicals that use label masks)"
    
objectives:
  - Understand shape measurements and their limitations
  - Perform shape measurements on objects
  
motivation: >
  Our eyes are extremely good in distinguishing forms and patterns and this has proven to be a powerful tool for characterizing different  cell-types, functions, phenotypes, and more. In image processing, we use shape measurements (e.g. area,  volume, elongation, ...) for an automated and objective characterization of forms. Consequently, one can address scientific questions or filter objects that should be used for further processing.

concept_map: >
  graph TD
    li[Object regions] --> sa("Shape Analysis")
    sa --> table["Object table<br>oid | area | perimeter | circularity <br>001 | 222 | 56 | 0.9 <br> 002 | 500 | 101 | 0.2 "]
    style table text-align:left

figure: /figures/measure_shapes.png
figure_legend: "Left: Fluorescence microscopy of nuclei showing various shapes with three nuclei manually delineated. Right: Label mask image of all nuclei. Bottom: Table with some shape measurements of the manually delineated nuclei." 

multiactivities:
  - ["measure_shapes/measure_shapes_act1.md", [["ImageJ GUI ROI", "measure_shapes/measure_shapes_act1_imagejgui_rois.md"],["ImageJ GUI MorphoLibJ", "measure_shapes/measure_shapes_act1_imagejgui.md", "markdown"], ["skimage napari", "measure_shapes/measure_shapes_act1_skimage_napari.py", "python"]]]
  - ["measure_shapes/measure_shapes_act2.md", [["ImageJ GUI", "measure_shapes/measure_shapes_act2_imagejgui.md", "markdown"], ["skimage napari", "measure_shapes/measure_shapes_act2_skimage_napari.py", "python"]]]



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
  - "[Object intensity measurements](../measure_intensities)"

external_links:
  - "[ImageJ: Measurements](https://imagej.net/ij/docs/menus/analyze.html#set)"
  - "[ImageJ: MorphoLibJ](https://imagej.net/MorphoLibJ#Region_analysis)"
  - "[ImageJ: Results visualisation](https://imagej.net/MorphoLibJ#Grayscale_morphological_filters). Label visualization in 3D viewer"
  - "[ImageJ: Overlay label IDs](https://forum.image.sc/t/overlay-numbers-on-image/35604/6)"
  - "[Python: Segmentation and regionprops tutorial](https://jni.github.io/i2k-skimage-napari/lectures/2_segmentation_and_regionprops.html)"
  - "[Coastal line paradox](https://en.wikipedia.org/wiki/Coastline_paradox). Effect of Sampling and resolution on the measurements"
---
