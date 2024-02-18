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

activity_preface: |
  - Open a [sample multichannel image](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__hela-cells.tif)
    - This is a 16-bits/channel composite color image of HeLa cells with red lysosomes, green mitochondria and blue nucleus. Image courtesy of Tony Collins, creator of the ImageJ for Microscopy collection of plugins at <http://www.macbiophotonics.ca/imagej/>
  - Explore how different channels can be viewed and selected
  - Learn to adjust look up tables and brightness/contrast settings
  - Learn to select channels and make an RGB image

activities:
    - ["ImageJ GUI - Inspect/view channels", "multichannel_images/activity1_imagejgui.md", "markdown"]
    #- ["binarization/binarization_act1.md", [["ImageJ GUI", "binarization/binarization_act1_imagejgui.md"], ["ImageJ Macro", "binarization/binarization_act1_imagejmacro.ijm"], ["ImageJ Jython", "binarization/binarization_act1_jython.py"], ["skimage napari", "binarization/binarization_act1_skimage_napari.py", "python"]]]
    - ["ImageJ GUI - Save channels as Tiff/RGB image", "multichannel_images/activity2_imagejgui.md", "markdown"]

assessment: >

  ### True of false?

    1. An RGB image is a 3-dimensional image
    1. In a multichannel image, each channel is a grayscale image that represents different data


    > ## Solution
    >   1. False; RGB is a datatype and has nothing to do with the image dimensionality
    >   1. True
    {: .solution}

  ###  Discuss with your neighbor

    1. How can multichannel images be used to improve machine learning models for image/object classification?
    1. What is a potential challenge when analyzing multichannel images?

    > ## Solution
    > 1. By providing additional context and information that can be leveraged by the model
    > 1. Correcting for crosstalk or bleed-through between channels
    {: .solution}

learn_next:

external_links:

---
