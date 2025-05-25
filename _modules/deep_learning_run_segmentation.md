---
title: Deep learning instance segmentation
layout: module
tags: ["draft"]
prerequisites:
  - "[Segmentation](../segmentation)"
  - "[Connected component labeling](../connected_components)"
objectives:
  - Run a deep learning model for instance segmentation
  - Visually assess the quality of the segmentation
  - Appreciate that, in order to work well, the model has to match the input data
  - Appreciate that even deep learning models may have parameters that need to be tuned
  - Appreciate that subtle differences in the image data may cause the model to fail

motivation: |
  Deep learning based nuclei and cell segmentation can be much faster and more accurate than conventional segmentation methods. In addition, there may be less parameter tuning required than for conventional methods. However, one can still make mistakes, such as applying the wrong deep learning model for the given input data. Both the usefulness and potential pitfalls make it very important to learn how to properly use and judge deep learning based image segmentation.

concept_map: >
    graph TD
      I("Intensity image") --> DL("Deep learning segmentation tool")
      DL --> L("Label mask image")
      M("Trained model") --- DL
      P("Parameters") --- DL

figure: /figures/deep_learning_run_segmentation.png
figure_legend: From left to right - _input intensity image_ (could be multichannel, multidimensional),  _UNET architecture_ that is mostly used a base for modern deep learning methods (such as cellpose/stardist/mesmer) for bioimage segmentation, _network output_ varies based on the model used i.e., xy-gradients/binary mask in case of cellpose and distances to object boundaries/object probabilities in case of stardist, _label mask_ generated using different methods depending upon preceding steps.

activity_preface: |
  - Use a deep learning tool to segment the cells in this image: [xyc_8bit__membranes_nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_8bit__membranes_nuclei.tif).
  - If the tool allows you to run different models, try them and compare the results
  - If the tool has parameters, explore them and compare the results

activities:
  - ["CellPose GUI", "deep_learning_run_segmentation/activities/deep_learning_cellpose_gui.md", "markdown"]

exercises:
- ["CellPose GUI", "deep_learning_run_segmentation/exercises/deep_learning_cellpose_gui.md", "markdown"]

assessment: >

  ### Fill in the blanks

    1. The typical output of a (deep learning based) instance segmentation is a ___ .
    1. If the segmentation is faulty you could consider to ___ or ___ .
    1. If you wonder which deep learning tool to use to segment your data you could ___ or ____.
    1. To run a deep learning model efficiently you should have a computer with ___ .

    > ## Solution
    >   1. label mask image
    >   1. use a different model or change the tool's parameters
    >   1. ask on [the forum](https://forum.image.sc/) or check the [BioImage Model Zoo](https://bioimage.io/#/)
    >   1. a GPU
    {: .solution}

learn_next:
  - Train a model (TODO)

external_links:
  - "[BioImage Model Zoo](https://bioimage.io/#/)"
  - "[ZeroCostDL4Mic](https://github.com/HenriquesLab/ZeroCostDL4Mic)"

---
