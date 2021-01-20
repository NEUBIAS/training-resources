---
title:     Lookup table
layout:    module

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
  - Open the image "xy_8bit__nuclei_high_dynamic_range.tif"
  - Explore different single color LUTs and LUT settings
  - Appreciate that LUT settings do not change the pixel values
  - Appreciate that a single color LUT will not allow you to see all nuclei without clipping
  - Appreciate that certain colors like blue are not so good for seeing different intensities (grey values are probably the best).
  - Explore multi color LUTs for visualisation of such a "high dynamic range" (big difference of intensities) image.

activities:
  - ["ImageJ Macro", "lut/activities/explore_luts_imagejmacro.ijm", "java"]

exercises:
  - ["ImageJ Macro", "lut/exercises/configure_luts_imagejmacro.md"]

assessment: |

  ## Calculate the brightness:

  1. `value =  49, min = 10,  max = 50, brightness = ?`
  2. `value = 100, min =  0,  max = 65, brightness = ?`
  3. `value =  10, min = 20,  max = 65, brightness = ?`

  > ## Solution
  > 1. `0.975`
  > 2. `1.538 ( -> 1 )`
  > 3. `-0.15 ( -> 0 )`
  {: .solution}

  ### Fill in the blanks

  Fill in the blanks using those words: decrease, larger than, increase, smaller than
  1. Pixels with values _____ `max` will appear saturated.
  2. Decreasing `max` while keeping `min` constant will _____ the contrast.
  3. Decreasing both `max` and `min` will _____ the overall brightness.
  4. Pixels with values _____ the `min` will appear black (using a single color LUT).

  > ## Solution
  > 1. larger than
  > 2. increase
  > 3. decrease
  > 4. smaller than
  {: .solution}


learn_next:

external_links:

---
## Single color lookup tables

Single color lookup tables are typically configured by chosing one color such as, e.g., grey or green, and choosing a `min` and `max` value that determine the brightness of this color depending on the `value` of the respective pixel in the following way:

`brightness(value) = ( value - min ) / ( max - min )`

In this formula `1` is be the maximal brightness and `0` the minimal brightness (i.e. black) that, e.g., your computer monitor can produce.

It can be that the formula yields values that are less than `0` or larger than `1`. In that case the convention is to paint pixels black if the value is smaller than `0` and paint them with the maximal brightness if the value is larger than `1`. In such cases one speaks of "clipping", because one looses ("clips") information about the pixel value.

`1 / ( max - min)` is also sometimes called the "contrast" and `max + min` the "brightness" of the LUT.

### Example for clipping

`min = 20, max = 100, v1 = 100, v2 = 200`

`brightness( v1 ) = ( 100 - 20 ) / ( 100 - 20 ) = 1`

`brightness( v2 ) = ( 200 - 20 ) / ( 100 - 20 ) = 2.25`

Both pixel values will be painted with the same brightness as a brightness larger than `1` is not possible (see above).