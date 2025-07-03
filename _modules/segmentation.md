---
title: Segmentation overview
layout:  module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
objectives:
  - "Understand the difference between instance and semantic segmentation"
motivation: |
  Bioimage analysis very often is concerned with the measurement of features (intensity, shape, ...) of individual objects (cells, nuclei, ...) or regions (mesoderm, inter-cellular space, ...) in images. The process of partitioning an image into objects and regions is called "image segmentation" and due to its prevalence is of central importance to bioimage analysis.

concept_map: >
  graph TD
    I[Image] --> S(Semantic segmentation)
    I --> O(Instance segmentation)
    O --- IO(Individual objects)
    S --- R(Regions of same type)

figure: /figures/segmentation.png
figure_legend: Left - Semantic segmentation of nuclei, membranes and mitochondria; Right - Instance segmentation of cells. Data from Martinez, Pape et al., Whole body integration of gene expression and single-cell morphology, Cell 2021.


learn_next:
  - "[Image thresholding](../binarization)"

external_links:
  - "[Wikipedia: Segmentation](https://en.wikipedia.org/wiki/Image_segmentation#Groups_of_image_segmentation)"
---
