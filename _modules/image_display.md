---
title: Image display
layout: module

prerequisites:

objectives:
  - Visualise the pixel values of an image. 

motivation: >
  Images are a collection of a lot (millions) of values, which is information that is hard to process for our human brains. Thus, one typically assigns a color to each distinct value, by means of lookup tables (LUTs). 

concept_map: >
  graph TD
    V("Value") --> L("Lookup table (LUT)")
    L --> C("Color")
    L -->|often is| A("Adjustable")

figure: /figures/lut.png
figure_legend:
  Image displayed with a grey lookup table.

activity_preface: >
  Very often LUTs have a way to configure the brightness of the colors.
  
  `brightness = ( value - min ) / ( max - min )`
  
  `if ( brightness < 0 ) set to zero`
  
  `if ( brightness > 1 ) set to one`
  
  `0 <= brightness <= 1`
  
  `contrast = max - min`

activities:
  "ImageJ GUI": "lut/activities/lut_imagejgui.md"

exercises_preface: >
  Fill in the blanks, using those words: decrease, larger than, increase, smaller than
    1. Pixels with values _____ `max` will appear saturated.
    2. Decreasing `max` while keeping `min` constant will _____ the contrast.
    3. Decreasing both `max` and `min` will _____ the overall brightness.
    4. Pixels with values _____ the `min` will appear black, when using a grayscale LUT.

exercises:

learn_next:

external_links:

---
