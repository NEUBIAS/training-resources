---
title: Multichannel images
layout: module
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[Data types](../datatypes)"
  - "[Lookup tables](../lut)"
objectives:
  - Understand/visualize different image channels.
motivation: >
  Typically, multichannel imaging involves using a fluorescence microscope equipped with multiple filter sets or detectors, each specific to a particular fluorophore's emission wavelength. In fluorescence microscopy, fluorescence signal of different dyes (at different wavelengths) can be registered simultaneously to one set of image spatial coordinates. Each signal then represents one channel and this information can be used to study/analyze various cellular and molecular processes e.g. colocalization.

concept_map: >
  graph TD
    F("Multichannel image")
    F --> C1("Channel 1")
    F --> C2("Channel 2")
    F --> CA(". . . .")
    F --> CN("Channel n")


figure: /figures/multichannel_2d_image.png

figure_legend: Multichannel image. Example for three 2D (xy) channels. Left - Each individual image is a channel shown in blue, red and green lookup tables.
  Right - All channels overlaid to display a composite image.
  Note that the array shape of (x,y,c) is just an example of channel order. The order may vary depending upon the data structure used to read image

multiactivities:
  - ["multichannel_images/activity1_multichannel_images.md", [["ImageJ GUI", "multichannel_images/activity1_imagejgui.md"],["skimage napari", "multichannel_images/activity1_skimage_napari.py", "python"], ["Galaxy Napari", "multichannel_images/activity1_galaxy.md", "markdown"]]]
  - ["multichannel_images/activity2_save_multichannel_images.md", [["ImageJ GUI", "multichannel_images/activity2_imagejgui.md"], ["ImageJ Macro", "multichannel_images/activity2_imagejmacro.ijm", "java"], 
  ["skimage napari", "multichannel_images/activity2_skimage_napari.py", "py"]]]


assessment: >

  ### True of false?

    1. In a multichannel image, each channel is a grayscale image that represents different data

    > ## Solution
    >   1. True
    {: .solution}

  ###  Discuss with your neighbor

    1. How can multichannel images be used to improve machine learning models for image/object classification?
    1. Is RGB image always a 3-dimensional image?
    1. What is a potential challenge when analyzing multichannel images?

    > ## Solution
    > 1. By providing additional context and information that can be leveraged by the model
    > 1. Not necessarily. In Fiji, one can have an RGB data type without alteration of the image array dimensions (still 2D for xy-images). However, in MALTAB and Python, for an RGB, an image array must be at least 3-dimensional
    > 1. Correcting for crosstalk or bleed-through between channels
    {: .solution}

learn_next:

external_links:
 - "[forum.image.sc: Colourblind friendly combinations](https://forum.image.sc/t/colourblind-friendly-colour-combinations/92567)"
---
## Color combinations for multi channel images
The choice of look-up tables to display a multi-channel image should fulfill following points:
 * Distinct color separation so to maximize the visual separation between channels.
 * Color blindness
 * ...