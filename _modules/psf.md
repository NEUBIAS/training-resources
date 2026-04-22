---
title: Point spread function 
layout: module
tags: ["draft", "microscopy", "image formation", "psf"]
prerequisites:
  - "[Digital image basics](../pixels)"
objectives:
  - Identify PSF-induced artifacts in microscopy images, specifically axial elongation (Z-distortion) and lateral blurring.
  - Predict the impact of the PSF on quantitative measurements, including how it inflates object size and dilutes signal intensity.
  - Understand how microscope hardware configurations change the PSF.
motivation: |
  In microscopy, what you see is never exactly what is actually there. The Point Spread Function (PSF) is the fundamental reason for this discrepancy. Think of the PSF as the "signature" of your microscop — it describes how the system takes a single, infinitesimal point of light and smears it into a 3D diffraction pattern. If you are doing quantitative microscopy (measuring intensity, size, or distance), ignoring the PSF is like trying to do carpentry with a ruler that changes length depending on where you stand.

concept_map: >
  graph TD
    A[Physical Object] -->|Convolution by PSF| B(Blurred Optical Image)
    B -->|Quantification Process| D{Measurement Type}
    
    D -->|Morphology| E[Size/Shape Distortion]
    D -->|Intensity| F[Signal Dilution/Crosstalk]
    D -->|Localization| G[Precision Limits]


figure: /figures/psf.png
figure_legend: "Image formation in a confocal microscope: central longitudinal (XZ) slice. The 3D acquired distribution arises from the convolution of the real light sources with the PSF."

multiactivities:
  - ["psf/fluorescent_beads.md", [["ImageJ GUI", "psf/fluorescent_beads_imagejgui.md"]]]
  - ["psf/image_formation_wf_vs_confocal.md", [["ImageJ GUI", "psf/image_formation_wf_vs_confocal_imagej_gui.md"]]]
  

assessment: >

  ### Fill in the blanks

    1. In fluorescence microscopy, the PSF causes an apparent increase in object \_\_\_\_\_ and a decrease in peak \_\_\_\_\_. This is most pronounced for structures with a physical size below \_\_\_\_\_ .
    1. The PSF is typically elongated along the \_\_\_\_\_ axis, which explains why structures often appear stretched in that direction in 3D microscopy images.
    
    > ## Solution
    >   1. In fluorescence microscopy, the PSF causes an apparent increase in object **size** and a decrease in peak **intensity**. This is most pronounced for structures with a physical size below **one micrometer**.
    >   1. The PSF is typically elongated along the **z** axis, which explains why structures often appear stretched in that direction in 3D microscopy images.
    {: .solution}

learn_next:
  - "[TODO](../auto_threshold)"

external_links:
  - "[Wikipedia: Point spread function](https://en.wikipedia.org/wiki/Point_spread_function)"
---

