---
title:     Rank filters and rank filter sequences (DRAFT)
layout:    module 
prerequisites:
  - "[Pixels](../pixels)"
  - "[Median filters](../median_filter)"
  - "[Neighbourhood image filters](../filter_neighbourhood)"
objectives: 
  - "Understand how rank filters function."
  - "Execute and compare several rank filters."
  - "Understand rank filter sequences on intensity and binary images"

motivation: >
  Typical rank filters are median, min and max filters. 
  When applied to binary images one typically refer to binary operations, such as erosion (min-filter) or dilation (max-filter). 
  For binary images rank filters help to clean up the image before the connected component analysis
  (remove small objects, separate objects, close holes). For intensity images rank filters can be used to compute a 
  local-background. 
  
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
  Open an image and investigate the action of a min filter and max filter. Use a binary as an example. 
  Perform an opening operation on the binary. Open an intensity image and perform an opening operation. 
  
activities: 

assessment: | 
 

exercises: 


learn_next:
   
---
# Rank filter sequences

Often rank filters are applied in a sequence. We refer to an opening operation as a max-filter followed by a min-filter of the same size. 
A closing operation is the inverse, a min-filter followed by a max-filter. 

