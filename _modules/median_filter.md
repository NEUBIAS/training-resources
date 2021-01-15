---
title:     Median filter properties
layout:    module
prerequisites:
  - "[Rank filters](../filter_rank)"
objectives:
  - "Understand in detail what happens when applying a median filter to an image"
motivation: |
  The median filter is one of the most popular filters for reducing noise in microscopy images. While the median filter has indeed many good properties, it should be - like any other filter -  used with care and a good understanding of its properties.
  
concept_map: >
  graph TD
    pixel --> NE("neighbourhood pixel values")
    NE -->  median
    median --> MF("median filtered pixel value")

figure: /figures/median_filter_binary.png
figure_legend: Left: Binary input image; Middle: After a 5x5 median filter; Right: Difference image

activity_preface: >
  Use example images that are relevant to your science and explore in detail what happens when applying a median filter.
  On purpose, increase the neighbourhood to an extend where your structures of interest become clearly compromised. 

activities:

exercises:


assessment: >

  ### True or False
    - There is only one correct threshold value in order to convert an intensity image into a binary image. 
    - Binary images are always unsigned 8-bit where the foreground is 255.
    
    > ## Solution
    >   - There is only one correct threshold value in order to convert an intensity image into a binary image. **False**
    >   -  Binary images are always unsigned 8-bit where the foreground is 255. **False**
    {: .solution}

learn_next:

external_links:

---

## Median filter

In general, for any neighbourhood filter, if the spatial extend of the neighbourhood is significantly (maybe three-fold) smaller than the smallest spatial length scale that you care about, you are on the safe side.

However, in biology, microscopy images are often containing relevant information down to the level of a single pixel. Thus, you typically have to deal with the fact that filtering may alter your image in a significant way. To judge whether this may affect your scientific conclusions you therefore should study the effect of filters in some detail.

Although a median filter typically is applied to a noisy gray-scale image, understanding its properties is easier when looking at a binary image.

From inspecting the effect of the median filter on above test image, one could say that a median filter
- is edge preserving
- cuts off at convex regions
- fills in at concave regions
- completely removes structures whose shortest axis is smaller than the filter width
