---
title: Smart microscopy targeted imaging 
layout: module
tags: 
prerequisites:
  - No programming or engineering knowledge is required 
  - Know how to operate a microscope
  - "[Segmentation](../segmentation)" 
  - "[Thresholding](../binarization)" 
  - "[Connected component labelling](../connected_components)" 
objectives:
  - Understand basic feedback microscopy workflow for automatically finding target objects and re-imaging them at high resolution
  - Understand essential steps in constructing and testing such a workflow
  - Learn which use cases would be appropriate for such workflow and possible limitation
motivation: |
  High-resolution imaging of large samples is a very time-consuming process. In many biological studies high-resolution microscopy data are not required for the entire sample, but only for specific areas. For example, often only sub-population of cells showing particular phenotype need to be imaged at high resolution. Manual selection of target areas is a laborious process and requires constant involvement of experimenters.
  Automating such experiments with smart (adaptive feedback) microscopy enables running such experiments in high-throughput manner without any user supervision. Image processing is done via pre-defined image analysis routine, which ensures unbiased and reproducible selection of imaged objects.

concept_map: >
  graph TD
    L("Low resolution image") --> I("Find objects")
    I --> H("Image objects at high resolution")
    H --> M("Move to new position")
    M --> L

figure: /figures/smart_microscopy_low_zoom_high_zoom.png
figure_legend: TODO

multiactivities:
  - ["smart_microscopy_low_zoom_high_zoom/act01.md", [["Automic Tools with Zen Blue", "smart_microscopy_low_zoom_high_zoom/act01_automictools.md"], ["Zen Blue Guided Acquisition", "smart_microscopy_low_zoom_high_zoom/act01_zen_blue_guided.md"]]]

assessment: >

  ### Questions 

    1. TODO?
    1. TODO?
    
    > ## Answers
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:
  - "[Automatic threshold for binarization](../auto_threshold)"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"
---

