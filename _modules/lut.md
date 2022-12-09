---
title: Lookup tables
layout: module

prerequisites:
  - "[Basic properties of images and pixels](../pixels)"

objectives:
  - "Understand how the numerical values in an image are transformed into colourful images."
  - "Understand what a lookup table (LUT) is and how to adjust it."
  - "Appreciate that choosing the correct LUT is a very serious responsibility when preparing images for a talk or publication."

motivation: |
  Images are a collection of a lot (millions) of values, which is information that is hard to process for our human brains. Thus, one typically assigns a color to each distinct value, by means of a lookup table (LUT). There is no fix recipe for how to adjust this mapping from numbers to colors. It is easy to chose a mapping that hides certain information in an image, while emphasising other information. Thus, configuring this mapping properly is a great responsibility that scientists have to take on when presenting their image data. 

concept_map: >
  graph TD
    V("Pixel value") --> L("Lookup table (LUT)")
    L --> |does not change|V
    L --> C("Color & Brightness")
    L -->|often is| A("Adjustable")

figure: /figures/lut.png
figure_legend:
  Image displayed with a grey LUT and the color mapping as an inset. In addition, another image shown with several different LUTs and settings.

activity_preface: |
  - Open the image [xy_8bit__nuclei_high_dynamic_range.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif)
  - Explore different single color LUTs and LUT settings
  - Visualise the LUT, e.g. as an inset in the image as in above figure.
  - Appreciate that LUT settings do not change the pixel values
  - Appreciate that a single color LUT will not allow you to see all nuclei without clipping
  - Appreciate that certain colors like blue are not so good for seeing different intensities (grey values are probably the best).
  - Explore multi color LUTs for visualisation of such a "high dynamic range" (big difference of intensities) image.

activities:
  - ["ImageJ Macro & GUI", "lut/activities/explore_luts_imagejmacro.ijm", "java"]
  - ["skimage napari", "lut/activities/explore_luts_skimage_napari.py", "python"]

exercise_preface: |
  - Open the image [xy_calibrated_16bit__nuclear_protein_control.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_calibrated_16bit__nuclear_protein_control.tif)
  - Open the image [xy_calibrated_16bit__nuclear_protein_treated.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_calibrated_16bit__nuclear_protein_treated.tif)
  - Display both images next to each other with the same LUT settings (this is what one typically should do for a presentation or publication).

exercise_preface: |
  - Open the image [xy_calibrated_16bit__nuclear_protein_control.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_calibrated_16bit__nuclear_protein_control.tif)
  - Open the image [xy_calibrated_16bit__nuclear_protein_treated.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_calibrated_16bit__nuclear_protein_treated.tif)
  - Display both images next to each other with the same LUT settings (this is what one typically should do for a presentation or publication).

exercises:
  - ["ImageJ Macro & GUI", "lut/exercises/configure_luts_imagejmacro.md"]

assessment: |

  ## Calculate the brightness:

  Use the formula and explanations given in above section on "single color lookup tables".

  1. `value =  49, min = 10,  max = 50, brightness = ?`
  2. `value = 100, min =  0,  max = 65, brightness = ?`
  3. `value =  10, min = 20,  max = 65, brightness = ?`

  > ## Solution
  > 1. `0.975`
  > 2. `1.538 ( -> 1 )`
  > 3. `-0.15 ( -> 0 )`
  {: .solution}

  ### Fill in the blanks

  Fill in the blanks using those words: larger than, smaller than
  1. Pixels with values _____ `max` will appear saturated.
  2. Pixels with values _____ the `min` will appear black (using a single color LUT).

  > ## Solution
  > 1. larger than
  > 2. smaller than
  {: .solution}

learn_next:

external_links:

---
### Lookup tables

Lookup tables do the mapping from a numeric pixel value to a color. This is the main mechanism how we visualise microscopy image data. In case of doubt, it is always a good idea to show the mapping as an inset in the image (or next to the image).

### Single color lookup tables

Single color lookup tables are typically configured by chosing one color such as, e.g., grey or green, and choosing a `min` and `max` value that determine the brightness of this color depending on the `value` of the respective pixel in the following way:

`brightness( value ) = ( value - min ) / ( max - min )`

In this formula, 1 corresponds to the maximal brightness and 0 corresponds to the minimal brightness that, e.g., your computer monitor can produce.

Depending on the values of `value`, `min` and `max` it can be that the formula yields values that are less than 0 or larger than 1. This is handled by assinging a brightness of 0 even if the formula yields values < 0 and assigning a brightness of 1 even if the forumla yield values larger than `1`. In such cases one speaks of "clipping", because one looses ("clips") information about the pixel value (see below for an example).

#### Clipping example

`min = 20, max = 100, v1 = 100, v2 = 200`

`brightness( v1 ) = ( 100 - 20 ) / ( 100 - 20 ) = 1`

`brightness( v2 ) = ( 200 - 20 ) / ( 100 - 20 ) = 2.25`

Both pixel values will be painted with the same brightness as a brightness larger than `1` is not possible (see above).

### Multi color lookup tables

As the name suggestes multi color lookup tables map pixel gray values to different colors.

For example:

`0 -> black`
`1 -> green`
`2 -> blue`
`3 -> ...`

Typical use cases for multi color LUTs are images of a high dynamic range (large differences in gray values) and label mask images (where the pixel values encode object IDs).

Sometimes, also multi color LUTs can be configured in terms of a `min` and `max` value. The reason is that multi colors LUTs only have a limited amount of colors, e.g. 256 different colors. For instance, if you have an image that contains a pixel with a value of 300 it is not immediately obvious which color it should get; the `min` and `max` settings allow you to configure how to map your larger value range into a limited amount of colors. 

