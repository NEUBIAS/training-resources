---
title:  Object intensity measurements
layout: module

prerequisites:
  - "[Connected component analysis](../connected_components)"

objectives:
  - Understand the correct biophysical interpretation of the most common object intensity measurements
  - Perform object intensity measurements

motivation: >
  The measurement of intensities in biological images is very common, e.g. to quantify expression levels of certain proteins by means of immuno-histochemistry. However, performing correct intensity measurements is very tricky and there are a lot of pitfalls. It is thus of utmost important to understand very well what one is doing. Without in-depth understanding the chance to publish wrong results based on intensity measurements is rather high.

concept_map: >
  graph TD
    li[Label image] --> im("Intensity measurement")
    ii[Intensity image] --> bc("Background corrected image")
    bc --> im
    im --> table["Results table"]
    table --> object_rows["Rows: Objects<br><br>Columns: Features<br>e.g., mean, sum, max"]

figure: /figures/measure_intensities.png
figure_legend: Object intensity measurements.

activity_preface: |
  - Open image [xy_float__h2b_bg_corr.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_float__h2b_bg_corr.tif)
  - Appreciate that the mean intensity in the background is zero.
  - Open label mask [xy_8bit_labels__h2b_bg_corr](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b_bg_corr.tif)
  - Measure the mean, max and sum intensities in both objects. For the sum measurements explain how to compute it and perform it in, e.g. excel or R.
  - Discuss the measurements' biophysical interpretation
    - The signal is H2B in a dividing and in an interphase cell.
    - Importantly, this was acquired with a widefield microscope!
      - The interpretation for a confocal microscope would be different!
  - Discuss that it is not really clear how large exactly the label regions have to be
  - Open label mask [xy_8bit_labels__larger_regions_h2b_bg_corr](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__larger_regions_h2b_bg_corr.tif)
  - Display the label mask on top of the raw image **[Image > Overlay > Add Image...]**
  - Measure the intensities again, one with the larger label mask
  - Discuss which values changed and by how much percent

activities:
  - ["ImageJ Macro & GUI", "measure_intensities/activities/measure_intensities_imagejmacro.ijm", "java"]

exercises: 
  - ["ImageJ Macro & GUI", "measure_intensities/exercises/measure_intensities_imagejguimacro.md"]

assessment: |

  ### Fill in the blanks (discuss with your neighbour)

    Fill in the blanks, using these words: number of pixels, integrated, mean, decrease, increase, increase, sum, decrease

    1. Average intensity is just another word for \_\_\_\_ intensity.
    1. Sum intensity is sometimes also called \_\_\_\_ intensity.
    1. The \_\_\_\_ intensity is equal to the mean intensity times the \_\_\_\_ in the measured region.
    1. In an unsigned integer image, increasing the size of the measurement region can only _____ the sum intensity.
    1. In an unsigned integer image, decreasing the size of the measurement region can \_\_\_\_ or \_\_\_\_ the mean intensity.
    1. In a floating point image, increasing the size of the measurement region could \_\_\_\_ the sum intensity.
    
     > ## Solution
     > 1. mean
     > 1. integrated
     > 1. sum, number of pixels
     > 1. increase
     > 1. decrease, increase
     > 1. decrease
     {: .solution}

learn_next:
  - "[Global background subtraction](../global_background_correction)"
  - "[Local background subtraction](../local_background_subtraction)"

external_links:


---
#### Background correction

In this module the images that we work are background corrected, meaning that the average intensity in regions without objects is zero. In general this is not the case and, in fact, proper background correction is a super important and very often also quite difficult task in bioimage analysis. There are thus several modules dedicated to background correction for intensity measurements. See below "Learn next" section.

#### Key points

- Intensity measurements are generally very tricky and most likely the source of many scientific mistakes. Please always consider consulting an bioimage analysis expert!
- Intensity measurements need a background correction. This can be achieved in several ways.
- At least, think carefully about whether the mean or sum intensity is the right readout for your biological question.
- If you publish or present something label your measurement properly, e.g. “Sum Intensity”. Just “Intensity” is not enough!
- Objects based intensity measurements require two input images: the (background corrected) intensity image and a label mask image.
