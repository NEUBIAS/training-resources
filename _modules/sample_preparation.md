---
title: Sample preparation artefacts
layout: module
tags: ["image formation"]
prerequisites:
  - "[Digital image basics](../pixels)"
objectives:
  - "Understand that sample preparation will affect the final imaging result"
  - "Understand which type of artefacts can come from sample preparation"
motivation: |
  When preparing samples for imaging, a series of steps to preserve and label the structure of interest are applied. These protocols are rarely perfect and depending on the type of fixation and labelling one obtain variable results. For example, certain structure may change their appearance, the biological sample may shrink, or some of the labels may not penetrate the sample. It is important to be aware how the sample preparation can affect the final imaging result. 

concept_map: >
  graph TD
    T1("Biological sample") --> T2("Sample preparation protocol")
    T2 --> T3("Labelled sample") --> T4("Imaging")

figure: /figures/sample_preparation.png
figure_legend: Schematic rendering of the sample preparation steps for chemical fixation and labelling. The labelled sample can then be imaged. Depending on the protocol and timings sample preparation artefacts may occur (lower row)

multiactivities:
  - ["sample_preparation/act01.md", [["ImageJ Macro", "sample_preparation/act01_imagejmacro.ijm"]]]

assessment: >

  ### True or False

    1. Sample preparation has no effect on the imaging result.
    1. The optical resolution depends on the sample preparation.
    1. The signal to background depends on the sample preparation.
    
    > ## Solution
    >   1. False
    >   1. False
    >   1. True
    {: .solution}

learn_next:
  - 

external_links:
  - 
---

