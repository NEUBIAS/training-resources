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
    V("Image pixel value") --> L("Lookup table (LUT)")
    L --> |does not change|V
    L --> |changes|C("Displayed pixel color & brightness")

figure: /figures/lut.png
figure_legend:
  "Left: Image displayed with a grey LUT and the color mapping as an inset. Right: Image shown with several different LUTs."

multiactivities:
  - ["lut/lut_act1.md", [["ImageJ GUI", "lut/lut_act1_imagejgui.md", "markdown"], 
	["ImageJ Macro", "lut/lut_act1_imagejmacro.ijm", "java"], 
	["skimage napari", "lut/lut_act1_skimage_napari.py", "python"],["Galaxy Napari","lut/lut_act1_galaxy.md"]]]
  - ["lut/lut_act2.md", [["ImageJ GUI", "lut/lut_act2_imagejgui.md"], 
  ["ImageJ Macro", "lut/lut_act2_imagejmacro.ijm", "java"], 
	["skimage napari", "lut/lut_act2_skimage_napari.py", "python"],["Galaxy Napari","lut/lut_act2_galaxy.md"]]]

keypoints:
  - LUT stands for "look-up table"; it defines how numeric pixel values are mapped to colors for display.
  - A LUT has configurable contrast limits that determine the pixel value range that is rendered linearly.
  - LUT settings must be responsibly chosen to convey the intended scientific message and not to hide relevant information.
  - A gray scale LUT is usually preferable over a colour LUT, especially blue and red are not well visible for many people. 
  - For high dynamic range images multi-color LUTs may be useful to visualise a wider range of pixel values.
assessment: |

  ### Compute how the contrast limits affect the rendered pixel brightness

  Read the below section "Explanations: Single color lookup tables" and use the formula that is given there to compute the rendered pixel brightness for the following scenarios:

  1. `value =  49, min = 10,  max = 50, brightness = ?`
  2. `value = 100, min =  0,  max = 65, brightness = ?`
  3. `value =  10, min = 20,  max = 65, brightness = ?`

  > ## Solution
  > 1. `0.975`
  > 2. `1.538 -> 1.0`
  > 3. `-0.22  -> 0.0`  
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

Lookup tables do the mapping from a numeric pixel value to a color. This is the main mechanism how we visualise microscopy image data. In case of doubt, it is always a good idea to show the mapping as an inset in the image (or next to the image).

#### Single color lookup tables

Single color lookup tables are typically configured by chosing one color such as, e.g., grey or green, and choosing a `min` and `max` value that determine the brightness of this color depending on the `value` of the respective pixel in the following way:

`brightness( value ) = ( value - min ) / ( max - min )`

In this formula, 1 corresponds to the maximal brightness and 0 corresponds to the minimal brightness that, e.g., your computer monitor can produce.

Depending on the values of `value`, `min` and `max` it can be that the formula yields values that are less than 0 or larger than 1. 
This is handled by assinging a brightness of 0 even if the formula yields values < 0 and assigning a brightness of 1 even if the formula yields values 
larger than `1`. In such cases one speaks of "clipping", because one looses ("clips") information about the pixel value (see below for an example).

##### Clipping example

`min = 20, max = 100, v1 = 100, v2 = 200`

`brightness( v1 ) = ( 100 - 20 ) / ( 100 - 20 ) = 1`

`brightness( v2 ) = ( 200 - 20 ) / ( 100 - 20 ) = 2.25`

Both pixel values will be painted with the same brightness as a brightness larger than `1` is not possible (see above).

#### Multi color lookup tables

As the name suggestes multi color lookup tables map pixel gray values to different colors.

For example:

`0 -> black`

`1 -> green`

`2 -> blue`

`3 -> ...`

Typical use cases for multi color LUTs are images of a high dynamic range (large differences in gray values) and label mask images (where the pixel values encode object IDs).

Sometimes, also multi color LUTs can be configured in terms of a `min` and `max` value. The reason is that multi colors LUTs only have a limited amount of colors, e.g. 256 different colors. For instance, if you have an image that contains a pixel with a value of 300 it is not immediately obvious which color it should get; the `min` and `max` settings allow you to configure how to map your larger value range into a limited amount of colors.
