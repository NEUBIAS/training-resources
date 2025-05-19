---
title: Multichannel images
layout: module
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[Data types](../datatypes)"
  - "[Lookup tables](../lut)"
objectives:
  - Understand/visualize different image channels.

motivation: |
  
  **Multichannel imaging** typically involves using a **fluorescence microscope** equipped with  multiple filter sets or detectors, each specific to a particular **fluorophore’s emission wavelength** (_Note_ that this differs from images acquired with color cameras e.g. histological stains)
  - The fluorescence signal of different dyes (at different wavelengths) can be **registered simultaneously** (or quasi) to one set of image spatial coordinates
  - Each signal then represents one **channel** 
  - Proper **inspection** and **rendering** of multichannel images is important to understand the spatial relationship between the different structures (e.g. colocalization)

concept_map: >
  graph TD
    F("Multichannel image")
    F --> C1("Channel 1")
    F --> C2("Channel 2")
    F --> CA(". . . .")
    F --> CN("Channel n")


figure: /figures/multichannel_images.png

figure_legend: Multichannel image. Left - Scheme of array organization for a multichannel image. Center - Example of three 2D (XY) images shown with grey look up table.  Right - All 3 channels overlaid to display a composite image using Cyan, Magenta, and Yellow look up tables, respectively. Note that the array shape of (X,Y,C) is just an example. The position of the channel dimension may differ depending on the data and the reader. 

multiactivities:
  - ["multichannel_images/multichannel_images_act1.md", [["ImageJ GUI", "multichannel_images/multichannel_images_act1_imagejgui.md"],["skimage napari", "multichannel_images/multichannel_images_act1_skimage_napari.py", "python"], ["Galaxy Napari", "multichannel_images/multichannel_images_act1_galaxy.md", "markdown"]]]
  - ["multichannel_images/multichannel_images_act2.md", [["ImageJ GUI", "multichannel_images/multichannel_images_act2_imagejgui.md"], ["ImageJ Macro", "multichannel_images/multichannel_images_act2_imagejmacro.ijm", "java"], 
  ["skimage napari", "multichannel_images/multichannel_images_act2_skimage_napari.py", "python"]]]


assessment: >

  ### True of false?

    1. In a multichannel image, each channel is an image that represents different data/stains
    1. There is no restriction in the choice of color for a merged image
    
    > ## Solution
    > 1. True
    > 1. False. Some color combinations may not be perceived as different colors by persons with color vision deficiency
    {: .solution}

  ###  Discuss with your neighbor

    1. How can multichannel images be used to improve machine learning models for image/object classification?
    1. Is RGB image always a 3-dimensional image?
    1. What is a potential challenge when analyzing multichannel images?

    > ## Solution
    > 1. By providing additional context and information that can be leveraged by the model
    > 1. Yes. In fact some software use 4 dimensions where the 4th dimension is transparency. If all channels are identical the image may render as a gray scale image.
    > 1. Crosstalk or bleed-through between channels. This typically should be corrected
    {: .solution}

learn_next:
 - "[N Dimensional Images](../multidimensional_image_basics)"

external_links:
 - "[forum.image.sc: Colourblind friendly combinations](https://forum.image.sc/t/colourblind-friendly-colour-combinations/92567)"
 - "[ASCB: How to make scientific figures accessible to readers with color blindness](https://www.ascb.org/diversity-equity-and-inclusion/how-to-make-scientific-figures-accessible-to-readers-with-color-blindness/)"
 - "[Fiji/Biop LUT for more than 3 colors](https://imagej.net/plugins/biop-lookup-tables)"
---
## Color combinations for multi channel images

### General recommendationas
The choice of lookup tables to display a merged multi-channel image should fulfill:
 * **Distinct color separation** so to maximize the visual separation between channels.
 * Avoidance of **problematic color combinations** that can't be distinguished with **color vision deficiency** (e.g. red/green)
 * If unsure test color combinations using a "color-blind mode". For example in ImageJ `Image > Color > Simulate Color Blindness`
 * If possible show the single channels next to the merged channel for better clarity

### Suggested color combinations
* **Two channels**:For example Green/Magenta, Blue/Yellow, Red/Cyan, Blue/Red 
* **Three channels**: For example Magenta/Green/Blue, Megenta/Yellow/Cyan, Red/Cyan/Yellow
* **More than three channels**: Displaying the merged image with enough contrast is challenging. It depends on the structures that have been stained and how much they overlap. Different color combinations should be tried out. One possibiility is Magenta/Green/Yellow/Cyan, or a grayscale LUT for one or more of the reference (less important) channels. 



 