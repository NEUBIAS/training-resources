---
title:     Intensity measurements 
layout:    page
---

## Intensity measurements

### Activity: Measure intensities in image regions

* Open image: xy_float__h2b_bg_corr.tif
* Measure for both nuclei:
        * Maximum intensity
        * Average intensity
        * Median intensity
        * Sum intensity
* Discuss the interpretation!
* Discuss where to measure!


### Activity: Intensity measurements without pixel based background correction

#### Motivation

There are several good reasons not to subtract the background from each pixel in an image:

* It is a bit tricky to do it right, because one has to convert to float to accomodate floting point and negative values.
* If one has really big image data (TB) one would need (at least) another TB storage for the background corrected version of the image.

#### Workflow

* Open image: xy_calibrated_8bit__two_nuclei_high_background.tif
* Measure for both nuclei and a background region:
        * Maximum intensity
        * Average intensity
        * Median intensity
        * Sum intensity
* Discuss how to correct the intensities for the background
        * Appreciate that you also need the region areas for this task
        * Measure the region areas
                * Watch out: the image is calibrated!
                * Use the area for the correction.

### Formative assessment: Intensity measurements

Fill in the blanks, using these words: integrated, mean, number_of_pixels, decrease, increase, sum

1. Average intensity is just another word for _____ intensity.
2. The _____ intensity is equal to the mean intensity times the _____ in the measured region.
3. In an 8-bit image, increasing the size of the measurement region can only _____ the sum intensity.
4. In a float image, increasing the size of the measurement region can _____ the sum intensity.

