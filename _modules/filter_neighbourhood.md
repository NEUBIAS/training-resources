---
title:     Neighbourhood image filters
layout:    module
prerequisites:
  - "[Image pixels](image_pixels)"
objectives:
  - Understand the basic principle of a neighbourhood filter
motivation: >
  This module explains how image features (objects) can be enhanced using filters

#|   |   |   |   |   |   |   |   |
#|---|---|---|---|---|---|---|---|
#| NC  | NC  | NC  |   |   |   |   |   |
#| NC  | C, NC  | NC  |   |   |   |   |   |
#| NC  | NC  | NC  |   |   |   |   |   |
#|   |   |   |   | NB  | NB  | NB  |   |
#|   |   |   |   |  NB | B, NB| NB  |   |
#|   |   |   |   |  NB |  NB |  NB |   |
#|   |   |   |   |   |   |   |   |

concept_map: >
  graph TB
    P(pixel) --> |has| NBH(neighbourhood pixels) 
    NBH --> |are used in| A(mathematical formula)
    A --> |compute new| NP(pixel value) 

# figure: /figures/binarization.png
# figure_legend: Image before and after binarization by applying a threshold.

activity_preface: >
  Use mean filter to facilitate image binarization

activities:

  "ImageJ GUI": "filter_neighbourhood/activities/mean_filter_imagejgui.md"
  "KNIME": "filter_neighbourhood/activities/mean_filter_knime.md"
#  "ImageJ Macro":
#  "Jython":
#  "MATLAB":

exercises_preface: >


exercises:
#  "ImageJ GUI": 
#  "ImageJ Macro":
#  "Jython":
#  "MATLAB":

learn_next:
- "[Convolution filters](filter_convolution)"
- "[Rank filters](filter_rank)"

external_links:

---
