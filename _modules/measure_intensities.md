---
title:  Object intensity measurements
layout: module
tags: ["Component"]

prerequisites:
  - "[Connected component analysis](../connected_components)"

objectives:
  - Understand the correct biophysical interpretation of the most common object intensity measurements
  - Perform object intensity measurements, including background subtraction

motivation: >
  The measurement of intensities in biological images is very common, e.g. to quantify expression levels of certain proteins by means of immuno-histochemistry. However, performing correct intensity measurements is very tricky and there are a lot of pitfalls. It is thus of utmost important to understand very well what one is doing. Without in-depth understanding the chance to publish wrong results based on intensity measurements is rather high.

concept_map: >
  graph LR
    li[Label image] --> im("Object intensity measurements")
    ii[Intensity image] --> im
    im --> table["Results table"]
    table --> object_rows["Rows: Objects<br><br>Columns: Mean, Sum, Max, ..., Background"]
    ii --> bgm("Background measurement")
    bgm --> table

figure: /figures/measure_intensities.png
figure_legend: H2b-mCherry widefield image of two cells. Common object intensity measurements, using a label mask and a manual background measurement.

activity_preface: |
  - Open image [xy_16bit__h2b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__h2b.tif)
  - Open label mask [xy_8bit_labels__h2b.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b.tif)
  - Using the label mask, measure the mean and max intensities as well as the objects' pixel area.
    - Exports the results as a table (and open in a spreadsheet software)
  - Manually measure the mean intensity in the background.
    - Add the background measurement as a new column to the table
  - Create new columns for background corrected mean, max, and sum intensity.
  - Discuss the measurements' biophysical interpretation
    - The signal is H2B in a dividing and in an interphase cell.
    - Importantly, this was acquired with a widefield microscope!
      - The interpretation for a confocal microscope would be different!
  - Repeat measurements with larger labels
    - Open label mask [xy_8bit_labels__h2b_dilate_labels.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b_dilate_labels.tif)
    - Appreciate that it is not always clear how large exactly the label regions have to be
    - Measure the intensities again, now with the larger label mask
    - Discuss which values changed and by how much percent

activities:
  - ["ImageJ GUI", "measure_intensities/activities/measure_intensities_imagejgui.md", "markdown"]

exercises:
  - ["ImageJ GUI", "measure_intensities/exercises/measure_intensities_imagejgui.md"]

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
     > 1. decrease, increase
     {: .solution}

learn_next:
  - "[Local background subtraction](../local_background_subtraction)"

external_links:


---
### Nomenclature

- median
- mean = average
- sum = total = integrated
- bg = background

### Formula

```
mean_corr = mean - bg
sum_corr = mean_corr * num_pixels = ( mean - bg ) * num_pixels = sum - ( bg * num_pixels )
```

### Biophysical interpretation

- `mean` often resembles the concentration of a protein
- `sum` often represents the total expression level of a protein
- For the correct biophysical interpretation you need to know the PSF of your microscope.
  - More specifically, you need to know how the 3D extend of the PSF relates to 3D extend of your biological structures of interest. Essentially, you need to exactly know __where__ your microscope system is measuring the intensities.
  - It is thus critical whether you used a confocal or a widefield microscope, because widefield microscope have an unbounded PSF along the z-axis.

### Key points

- Intensity measurements are generally very tricky and most likely the source of many scientific mistakes. 
  - Please consider consulting a bioimage analysis expert.
- Intensity measurements need a background correction. 
  - Finding the correct background value can be very difficult and sometimes even impossible and, maybe, the project just cannot be done like this!
- At least, think carefully about whether the mean or sum intensity is the right readout for your biological question.
- If you publish or present something, label your measurement properly, e.g. “Sum Intensity” (just “Intensity” is not enough)!
