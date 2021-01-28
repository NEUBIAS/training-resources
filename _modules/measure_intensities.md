---
title:     Object intensity measurements
layout:    module


prerequisites:
  - "[Connected component analysis](../connected_components)"
    
objectives:
  - Understand the correct biophysical interpretation of the most common object intensity measurements
  - Perform object intensity measurements
  
motivation: >
  The measurement of intensities in biological images is very common, e.g. to quantify expression levels of certain proteins by means of immuno-histochemistry. However, performing correct intensity measurements is very tricky and there are a lot of pitfalls. It is thus of utmost important to understand very well what one is doing. Without in-depth understanding the chance to publish wrong results based on intensity measurements is rather high. 

concept_map: >
  graph LR
    li[Label Image] --> im("Intensity Measurement")
    li[Intensity Image] --> im("Intensity Measurement")
    li[Intensity Image] -->|may be|bc("Background corrected")
    im -.-> |"example <br> intensity features"| ex["mean <br>sum <br>max"]
    im --> table[]"Results table"]
    table --> object_rows["Rows are objects"]
    table --> feature_columns["Columns are intensity features"]

figure: /figures/measure_intensities.png
figure_legend: Object intensity measurements. 

activity_preface: |
  - Open image [xy_float__h2b_bg_corr.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_float__h2b_bg_corr.tif)
  - Appreciate that the mean intensity in the background is zero.
  - Open label mask [xy_8bit_labels__h2b_bg_corr](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b_bg_corr.tif)
 Explain simple shape features (area, volume, perimeter) and some more complexes
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
  - "[Workflow - Simple 2D object analysis](../workflow_segment_2d_nuclei_measure_shape)"
  - "[Object intensity meaurements](../measure_intensities)"


external_links:
    - "[Wikipedia coastal line paradox](https://en.wikipedia.org/wiki/Coastline_paradox). Effect of Sampling and resolution on the measurements"
    - "[Results visualisation](https://imagej.net/MorphoLibJ#Grayscale_morphological_filters). Label visualization in 3D viewer"

---
#### Background correction

In this module the images that we work are background corrected, meaning that the average intensity in regions without objects is zero. In general this is not the case and, in fact, proper background correction is a super important and very often also quite difficult task in bioimage analysis. There are thus several modules dedicated to background correction for intensity measurements. See below "Learn next" section.