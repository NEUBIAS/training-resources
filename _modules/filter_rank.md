---
title:     Rank filters
layout:    module
prerequisites:
  - "[Pixels](../pixels)"
  - "[Neighbourhood image filters](../filter_neighbourhood)"
objectives: 
  - "Understand how rank filters function."
  - "Execute and compare several rank filters."
  - "Compare image smoothing using rank (e.g. median) vs. another filter type (e.g. mean)."

motivation: >
  Rank filters such as median-filters can be used to denoise images by preserving the boundary. 
  When applied to binary images one typically refer to binary operations 
  such as erosion (min-filter) or dilation (max-filter).

concept_map: >
  graph TD
    pixel --> NE("neighbourhood pixel values")
    NE --> sorted("sorted pixel values")
    sorted --> min
    sorted --> max
    sorted --> median
    sorted --> ...
    subgraph rank value
    min
    max
    median
    ...
    end
    subgraph replace pixel value
    fpixel1
    end
    median --> fpixel1[rank filtered pixel]
    min -.-> fpixel1
    max -.-> fpixel1
    ... -.-> fpixel1

figure: /figures/rank_filter.png
figure_legend: Scheme of how a rank filter acts on an image
activity_preface: |
  Open an image and investigate the action of a median filter with respect to:
    - removing the noise
    - remove small structures
    - preserves edges
    
  Compare the median filter with respect to a mean filter.
  
activities:
    - ["ImageJ GUI", "filter_rank/activities/filter_rank_imagejgui.md", "markdown"]

assessment: | 
    ### True or false? 
      1. Median filter is just another name for mean filter.
      2. Small structures can completely disappear from an image when applying a median filter. 
    
    > ## Solution
    >   1. Median filter is just another name for mean filter. **FALSE** 
    >   2. Small structures can completely disappear from an image when applying a median filter. **TRUE**
    {: .solution}

exercises: 
  - ["ImageJ GUI", "filter_rank/exercises/filter_rank_imagejgui.md"]      


learn_next:
    "[Median filter properties](../median_filter)"
---

