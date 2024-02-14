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
  Typically, multichannel imaging involves using a fluorescence microscope equipped with multiple filter sets or detectors, each specific to a particular fluorophore's emission wavelength. In fluorescence microscopy, fluorescence signal of different dyes (at different wavelengths) can be registered simultaneously to one set of image spatial coordinates. Each signal the represents one channel and this information can be used to study/analyze various cellular and molecular processes e.g. colocalization.

concept_map: >
  graph TD
    L("Label mask") -->|"remove label(s)"| ML("Modified label mask")

figure: /figures/multichannel_2d_image.png
#figure_legend: Multichannel image. Example for three 2D (xy) channels.  Left - Each individual detector is one channel shown in blue, red and green lookup tables. Right- All channels overlaid to display a composite image. Note: array shape of (x,y,c) is just an example of channel order. The order may vary depending upon the data structure used to read image.

activity_preface: |
  - Open and inspect a sample multichannel image from ImageJ
  - Explore how different channels can be viewed and selected
  - Learn to adjust look up tables and brightness/contrast settings
  - Select two channels and save it as an RGB image

activities:
    - ["ImageJ GUI", "multichannel_images/activity1_imagejgui.md", "markdown"]
    - ["ImageJ GUI", "multichannel_images/activity2_imagejgui.md", "markdown"]

assessment: >

  ### True of false?

    1.
    1.
    1.

    > ## Solution
    >   1.
    >   1.
    >   1.
    {: .solution}

  ###  Discuss with your neighbor

    1.
    1.

    > ## Solution
    > 1.
    > 1.
    {: .solution}

learn_next:

external_links:

---
