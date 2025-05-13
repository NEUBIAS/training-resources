---
title: Statistical (rank) filters
layout: module
prerequisites:
  - "[Neighbourhood filters](../filter_neighbourhood)"
objectives:
  - Understand conceptually how local statistical (rank) filter work
  - Apply statistical filters to images
motivation: |
  - Almost every image analysis pipeline will contain a step that applies local statistical filters.
  - Local minimum and maximum filters are the basis of the very useful class of morpholoical filters.
  - The median filter is, due to its edge preserving properties, one of the most popular filters for reducing noise in microscopy images.
  - Variance filtering is very useful for detecting structures in label free microscopy such as transmission LM or EM. 
  
concept_map: >
  graph TD
    P("pixel") --> NS("neighbourhood statistics")
    NS -->  FP("filtered pixel value")

figure: /figures/filter_statistical.png
figure_legend: "Shows the effect of a radius 2 disk shaped kernel statistical filter on an image. Top left: Input; Top middle: Minimum; Top right: Maximum; Bottom left: Mean; Bottom middle: Median; Bottom right: Variance." 

multiactivities:
  - ["filter_statistical/median_filter.md", 
    [
    ["ImageJ Macro", "filter_statistical/median_filter_imagejmacro.ijm"], 
    ["skimage napari", "filter_statistical/median_filter_skimage_napari.py"],
    ["Galaxy", "filter_statistical/median_filter_galaxy.md"]
    ]
    ]
  - ["filter_statistical/statistical_filters.md", 
    [
    ["ImageJ Macro", "filter_statistical/statistical_filters_imagejmacro.ijm"], 
    ["skimage napari", "filter_statistical/statistical_filters_skimage_napari.py"]
    ]
    ]
  
assessment: >

  ### Answer the questions

    1. What is the primary purpose of applying a median filter to an image?
    1. How does a local maximum filter differ from a local minimum filter in terms of the output pixel values?
    1. Why might variance filtering be particularly useful in label-free microscopy?
    
    > ## Solution
    >   1. To reduce noise in an image while preserving edges.
    >   1. A local maximum filter replaces each pixel with the maximum value in its neighborhood, while a local minimum filter replaces it with the minimum value.
    >   1. Variance filtering highlights regions with high variability, which can help detect structures in label-free microscopy such as transmission light microscopy or electron microscopy.
    {: .solution}

learn_next:
  - "[Morphological filters](../filter_morphological)"

external_links:
---

