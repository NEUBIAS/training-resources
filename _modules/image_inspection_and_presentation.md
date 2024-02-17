---
title: Quantitative image inspection and presentation
layout: module
tags: ["workflow"]
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[Lookup tables](../lut)"
objectives:
  - "Quantitatively inspect and present fluorescent microscopy images."
motivation: |
  For scientific discovery using microscopy it is critical to be able quantitatively inspect and present bioimaging data. This is important at many stages, ranging from looking at the data yourself, presenting the data to lab members and finally creating a figure for a publication.  

concept_map: >
  graph TD
    ID("Image data") --> IS("Inspection")
    IS --> P("Presentation")

figure: /figures/image_inspection_and_presentation.png
figure_legend: "Fluorescence microscopy data showing collagen secretion of tissue culture cells. Left: 0 hours secretion of collagen; right: 96 hours secretion of collagen."

multiactivities:
  - ["image_inspection_and_presentation/inspect_collagen_data.md", [["ImageJ Macro", "image_inspection_and_presentation/inspect_collagen_data.ijm"], ["ImageJ GUI", "image_inspection_and_presentation/inspect_collagen_datagui.md"]]]
  - ["image_inspection_and_presentation/create_collagen_figure.md", [["Powerpoint", "image_inspection_and_presentation/create_collagen_figure_powerpoint.md"]]]

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .

    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:

external_links:
  - "[Forum discussion on collagen figure creation](https://forum.image.sc/t/image-data-figure-creation-best-practices-example-for-collagen-secretion/84584)"
---
