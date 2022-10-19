---
title: Deep learning instance segmentation
layout: module
tags: ["draft"]
prerequisites:
  - "[Image segmentation](../segmentation)"
  - "[Connected component labeling](../connected_components)"
objectives:
  - Run a deep learning model for instance segmentation
  - Visually assess the quality of the segmentation
  - Appreciate that, in order to work well, the model has to match the input data
  - Appreciate that even deep learning models may have parameters that need to be tuned

motivation: |
  Deep learning based nuclei and cell segmentation can be much faster and more accurate than conventional segmentation methods. In addition, there may be less parameter tuning required than for conventional methods. However, one can still make mistakes, such as applying the wrong deep learning model for the given input data. Both the usefulness and potential pitfalls make it very important to learn how to properly use and judge deep learning based image segmentation.

concept_map: >
  graph TD
    I("Intensity image") --> DL("Deep learning segementation tool")
    DL --> L("Label mask image")
    M("Trained model") --- DL
    P("Parameters") --- DL

figure: /figures/template.png
figure_legend: TODO

activity_preface: |
  - Use a deep learning tool to segment the cells in this image: [xyc_8bit__membranes_nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_8bit__membranes_nuclei.tif).
  - If the tool allows you to run different models, try them and compare the results
  - If the tool has parameters, exploer them and compare the results

activities:
- ["CellPose GUI", "deep_learning_run_segmentation/activities/cellpose_gui.md", "markdown"]

exercises:

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
---

