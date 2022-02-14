---
title:  Morpholigical filters on binary images
layout: module 
tags: ["draft","Rank filter series","Dilation","Erosion","Opening"]

prerequisites:
  - "[Segmentation](../segmentation)"
  - "[Connected component labeling](../connected_components)"
  - "[Neighbourhood image filters](../filter_neighbourhood)"
  
objectives: 
  - "Understand different rank/morpholigical filters."
  - "Asses how filters and filter sequences can be used to clean-up binary images."

motivation: >
 We use morphological filters to further process a binary image. They allow, for example, to correct the segmentation results by removing pixels that do not belong to foreground objects or to change the shape of the objects to better separate those in the  subsequent connected component analysis. Morphological filters make it also possible to find specific areas of an object, for example, its edge. 

concept_map: >
 graph TD
    subgraph opening
        erode("Erode (min)") --> dilate("Dilate (max)")
    end
    
    subgraph closing
            dilate2("Dilate (max)") --> erode2("Erode (min)")
    end
    subgraph rank operations
            any("...")
    end
    BI("Binary image") --> SE("structuring element")
    SE .-> erode 
    SE .-> dilate2 
    SE .-> any 
    dilate .-> BIM
    erode2 .-> BIM
    any .->  BIM("Modified binary image")
     
    
figure: /figures/filter_morphological.png
figure_legend: Scheme of how a rank filter acts on an image
activity_preface: |
  Open an image and investigate the action of a min filter and max filter. Use a binary as an example. 
  Perform an opening operation on the binary. Open an intensity image and perform an opening operation. 
  
activities: 

assessment: | 
 

exercises: 


learn_next:
   
---
images: [xy_8bit_binary__for_open_and_close.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__for_open_and_close.tif)

# Rank filter sequences

Often rank filters are applied in a sequence. We refer to an opening operation as a max-filter followed by a min-filter of the same size. 
A closing operation is the inverse, a min-filter followed by a max-filter. 



# Morphological filters

## Requirements

- Neighbourhood filters
- Rank filters

## Motivation

This module explains how filters can be used to change size and shape of objects in the image.

## Learning objectives
- Understand how to design morphological filters using rank filters
- Execute morpholofical filters on binary or grayscale images and explain the output

## Concept map


[*] Concept map above assumes bright objects on dark background. For dark objects on bright background effect of min and max filters inverses

### Activity: Explore erosion and dilation on binary images

- Open image: xy_8bit_binary__two_spots_different_size.tif
- Explore how structures grow and shrink, using erosion and dilation

### Activity: Explore opening and closing on binary images

- Open image: xy_8bit_binary__for_open_and_close.tif
- Explore effects of morphological closing and opening:
	- closing can fill holes
	- closing can connect gaps
	- opening can remove thin structures

### Formative assessment

Fill in the blanks, using those words: shrinks, increases, decreases, enlarges.

1. An erosion _____ objects in a binary image.
2. An erosion in a binary image _____ the number of foreground pixels.
3. A dilation in a grayscale image _____ the average intensity in the image.
4. A dilation _____ objects in a binary image.


True of false? Discuss with your neighbour!

1. Morphological openings on binary images can decrease the number of foreground pixels.
2. Morphological closings on binary images never decreases the number of foreground pixels.
3. Performing a morphological closing a twice in a row does not make sense, because the second closing does not further change the image.

## Learn more

- https://en.wikipedia.org/wiki/Morphological_gradient
- https://imagej.net/MorphoLibJ#Grayscale_morphological_filters



```mermaid
graph TD
    image --> max1[max]
    image --> min1[min]
    image --> max2[max]
    image --> min2[min]
    image --> d
subgraph rank filter sequence
    max2 --> min3[min]
    min2 --> max3[max]
    max1
    min1
    d[max - min]
    end
    max1 --> dilation
    min1 --> erosion
    max3 --> opening
    min3 --> closing
    d --> gradient
    subgraph morphological filter name
    dilation
    erosion
    opening
    closing
    gradient
    end
```
=======
