---
title:     Median filter
layout:    module
prerequisites:
    - "[Pixels](../pixels)"
    - "[Neighbourhood image filters](../filter_neighbourhood)"

objectives:
  - "Understand in detail what happens when applying a median filter to an image"
  
motivation: |
  The median filter is a rank filter and is one of the most popular filters for reducing noise in microscopy images.
  While the median filter has indeed many good properties, it should be - like any other filter - used with care and a good understanding of its properties.
  
concept_map: >
  graph TD
    pixel --> NE("neighbourhood pixel values")
    NE -->  median
    median --> MF("median filtered pixel value")

figure: /figures/median_filter_grayscale.png
figure_legend: Median filter example. Left - Raw; Right - After a 5x5 median filter.

multiactivities:
  - ["median_filter/median_filter.md", [["ImageJ Macro", "median_filter/median_filter_imagejmacro.ijm", "java"], ["skimage napari", "median_filter/median_filter_skimage_napari.py", "python"],["Galaxy", "median_filter/median_filter_galaxy.md"]]]

assessment: |

    ### True or false? 
      1. Median filter is just another name for mean filter.
      2. Small structures can completely disappear from an image when applying a median filter. 
    
    > ## Solution
    >   1. Median filter is just another name for mean filter. **FALSE** 
    >   2. Small structures can completely disappear from an image when applying a median filter. **TRUE**
    {: .solution}
    
    
learn_next:
    "[Rank filters and rank filter sequences](../filter_rank)"

external_links:

---

## Properties of median filter

The median filter is based on ranking the pixels in the neighbourhood

<img src="../figures/median_filter_and_ranking.png"  align ="center" width="50%" >


In general, for any neighbourhood filter, if the spatial extend of the neighbourhood is significantly 
(maybe three-fold) smaller than the smallest spatial length scale that you care about, you are on the safe side.

However, in biology, microscopy images are often containing relevant information down to the level of a single pixel. Thus, you typically have to deal with the fact that filtering may alter your image in a significant way. To judge whether this may affect your scientific conclusions you therefore should study the effect of filters in some detail.

Although a median filter typically is applied to a noisy gray-scale image, understanding its properties is easier when looking at a binary image.

From inspecting the effect of the median filter on above test image, one could say that a median filter
- is edge preserving
- cuts off at convex regions
- fills in at concave regions
- completely removes structures whose shortest axis is smaller than the filter width
