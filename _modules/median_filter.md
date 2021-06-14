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
figure_legend: Median filter example. Left: Raw; Right: After a 5x5 median filter.

activity_preface: >
  Use example images that are relevant to your science and explore in detail what happens when applying a median filter.
  On purpose, increase the neighbourhood to an extend where your structures of interest become clearly compromised. Do some of all of these activities.
  
  - Open image [xy_8bit_binary__squares_different_size.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__squares_different_size.tif)
    discuss effect of median filter on removing small objects, preserving edge and changing edges for large radii. 
    
  - Open image [xy_8bit_binary__large_spot.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__large_spot.tif)
    discuss effect of median filter on edge changes. Use a ROI and apply filter only on the ROI. Compare also to mean filter. 
    
  - Open image [xy_8bit__two_noisy_squares_different_size.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_noisy_squares_different_size.tif)
  and discuss effect of median and mean filter of different size with respect to noise and preservation of structure. 
  
  - Open image [xy_8bit__PCNA.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif)  and discuss effect of filters with respect to preservation of structure. 
  
  
  - (Optional) Open image [xy_8bit_binary__test_structures.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__test_structures.tif) and discuss
  what happens to the structures. This is a more detail inspection of what does a median filter do.


activities:
    - ["ImageJ GUI & Macro median", "median_filter/activities/median_filter_imagejmacrogui.ijm", "java"]
    - ["ImageJ GUI & Macro mean", "median_filter/activities/mean_filter_imagejmacrogui.ijm", "java"]
        
exercises:
    - ["ImageJ GUI", "median_filter/exercises/median_filter_imagejgui.md"]
    
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
