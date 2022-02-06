---
title: Segmentation
layout:  module
tags: ["draft"]
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
objectives:
motivation: |
concept_map: >
  graph LR
    I[Image] --> O(Instance/Object segmentation)
    I --> S(Semantic/Region segmentation)
    O -- often stored as--- L(Label mask image)
    S -- often stored as--- L

figure: /figures/segmentation.png
figure_legend: Left - Semantic segmentation of nuclei, membranes and mitochondria; Right - Instance segmentation of cells (Data from Martinez, Pape et al., Whole body integration of gene expression and single-cell morphology, Cell 2021).

activity_preface: |

activities:

exercises:

assessment: >

learn_next:

external_links:
  - "[Wikipedia: Segmentation](https://en.wikipedia.org/wiki/Image_segmentation#Groups_of_image_segmentation)"
---
