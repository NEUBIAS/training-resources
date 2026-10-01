---
title: Smart microscopy - adjustment of the acquisition parameters 
layout: module
tags: []
prerequisites:
  - Tool for designing Smart Microscopy workflows with the possibility for automated adjustment of light intensity, exposure time or other parameters influencing the average photon counts for the emitted light.
  - (Advanced/optional) automated control of objective correction collar or other parameters controlling image sharpness.
  - Image histogram
  - Signal-to-Noise ratio (SNR)
  - "[Intensity measurements](../measure_intensities)" 
objectives:
  - "Learn how automated adjustment of imaging settings can improve image quality"
  - "Test workflows for automated improvement of SNR and image sharpness"
  
motivation: |
  This module explains the workflow for automatically improving image quality using feedback microscopy.
  
  Insufficient image quality often caused by sub-optimal image analysis settings. In case of multiposition imaging of heterogeneous samples, it is hardly possible to set up optimal imaging parameters for each field of view. In case of cyclic or time-lapse imaging, optimal imaging settings might change over time due to the changes in the imaged samples.

  Smart microscopy can make use of automated image analysis for scoring image quality (e.g. brightness, SNR, sharpness) and improving this score via adaptive control of critical image analysis parameters.


concept_map: >
  graph TD
    D("[M]: Acquire image with default settings") --> A("[A]: Calculate image quality score")
    A --> N("[M]: Acquire image with the improved settings")
    N --> M("Move to new position")
    M --> I("[M]: Acquire other images with the improved settings")
    I --> N

figure: /figures/smart_microscopy_acquisition_parameters.png
figure_legend: Figure 1. Hela Kyoto cells stained with anti-tubulin-FITC primary labelled antibody. Images are acquired on Zeiss LSM900 confocal microscope. Left image - default laser power. Right image - automatically adjusted laser power

multiactivities:
  - ["smart_microscopy_acquisition_parameters/act01.md", [["Zeiss ZEN Experiment Feedback", "smart_microscopy_acquisition_parameters/act01_zen_experiment_feedback.md"]]]

assessment: >

  ### Questions 

    1. Which parameters need to be automatically controlled for improving image SNR?
    1. Why optimal imaging settings can change for cyclic staining and time-lapse experiments?
    
    > ## Answers
    >   1. Laser power, exposure time, scanning speed, averaging, objective correction collar
    >   1. In cyclic staining-restaining experiments labelling efficiency might differ significantly between cycles due to differences in the labelling efficiency or biological reasons. In time-lapse experiments, morphology and signal strengh in the live specimen often change over time due to change of the sample itself or fluorescence bleaching.
    {: .solution}

learn_next:
  - "[Targeted imaging](../to_add)"

external_links:
  - "[To add](https://to_add)"
---

