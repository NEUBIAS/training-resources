---
title:  Morphological filters
layout: module
tags: ["Rank filters","Dilation","Erosion","Opening", "Granulometry"]

prerequisites:
  - "[Segmentation overview](../segmentation)"
  - "[Thresholding](../binarization)"
  - "[Connected component labeling](../connected_components)"
  - "[Neighborhood filters](../filter_neighbourhood)"

objectives:
  - "Understand how to design morphological filters using rank filters"
  - "Execute morphological filters on binary or label images and understand the output"

motivation: >
 Morphological filters (MFs) are used to clean up segmentation masks and achieve a change in morphology and/or size of the objects. For example, MFs are used to remove wrongly assigned foreground pixels, separate touching objects, or identify objects boundaries.

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
    BI("Binary/label image") --> SE("structuring element")
    SE .-> erode
    SE .-> dilate2
    SE .-> any
    dilate .-> BIM
    erode2 .-> BIM
    any .->  BIM("Modified binary/label image")


figure: figures/filter_morphological.png
figure_legend: "Upper row - Example of a workflow using morphological filters to improve the segmentation and compute the edge of the nuclei for further intensity measurements if necessary measurements have to be made on the periphery. Image on top left is a 2 channel intensity image (where channel 1 shows nuclear membrane and channel 2 shows dna staining). Lower row - Image level description of dilation and erosion operation using a 3x3 structuring element (left side). Morphological filters applied in series, e.g. opening (i.e. erosion followed by dilation) and closing (i.e. dilation followed by erosion), can achieve very useful results (right side). Red and green arrows show erosion and dilation respectively"

multiactivities:
  - ["filter_morphological/filter_morphological_act1.md", [["ImageJ Macro", "filter_morphological/filter_morphological_act1_imagejmacro.ijm"], ["skimage napari", "filter_morphological/filter_morphological_act1_skimage_napari.py"]]]
  - ["filter_morphological/filter_morphological_act2.md", [["ImageJ Macro", "filter_morphological/filter_morphological_act2_imagejmacro.ijm"], ["skimage napari", "filter_morphological/filter_morphological_act2_skimage_napari.py"]]]
  - ["filter_morphological/filter_morphological_act3.md", [["ImageJ Macro", "filter_morphological/filter_morphological_act3_imagejmacro.ijm"], ["skimage napari", "filter_morphological/filter_morphological_act3_skimage_napari.py"]]]
  - ["filter_morphological/filter_morphological_act4.md", [["ImageJ GUI", "filter_morphological/filter_morphological_act4_imagejgui.md"], ["ImageJ Macro", "filter_morphological/filter_morphological_act4_imagejmacro.ijm"]]]
  - ["filter_morphological/cytoplasmic_ring.md", [["skimage napari", "filter_morphological/cytoplasmic_ring_skimage_napari.py"]]] 
  - ["filter_morphological/granulometry_2d.md", [["ImageJ Macro", "filter_morphological/granulometry_2d_imagejmacro.ijm"]]] 

assessment: |

    ### Fill in the blanks
    Using those words fill in the blanks: closing, opening,  min, shrinks, decreases, enlarges, max.

      1. An erosion _____ objects in a binary image.
      2. An erosion in a binary image _____ the number of foreground pixels.
      3. A dilation _____ objects in a binary image.
      4. An erosion of a binary image corresponds to a ___ rank operation.
      5. An dilation of a binary image corresponds to a ___ rank operation.
      6. A dilation followed by an erosion is called ___.
      7. An erosion followed by a dilation is called ___ .

      > ## Solution
      > 1. shrinks
      > 2. decreases
      > 3. enlarges
      > 4. min
      > 5. max
      > 6. closing
      > 7. opening
      {: .solution}

    ### True of false?
    Discuss with your neighbour!

      1. Morphological openings on binary images never decrease the number of foreground pixels.
      2. Morphological closings on binary images never decreases the number of foreground pixels.
      3. Performing a morphological closing twice in a row does not make sense, because the second closing does not further change the image.
      4. Performing a morphological closing with radius 2 element is equivalent to two subsequent closing operation with radius 1.

      > ## Solution
      > 1. False
      > 2. True
      > 3. True
      > 4. False
      {: .solution}



learn_next:

external_links:
    - "[Morphological gradient (Wikimedia)](https://en.wikipedia.org/wiki/Morphological_gradient)"
    - "[Lecture on filters and segmentation - Refining masks (R. Haase)](https://www.youtube.com/watch?v=LT8L3vSLQ2Q&t=1871s)"
    - "[Morphological filters on grayscale images (MorphoLibJ)](https://imagej.net/plugins/morpholibj#grayscale-morphological-filters)"

---

## Rank filters
In the region defined by the structuring element, pixel elements are ranked/sorted according to their values. The pixel in the filtered image is replaced with the corresponding sorted pixel (smallest = min, greatest = max, median ). See also [Median filter](../median_filter). Morphological filters corresponds to one or several rank filters applied to an image.

## Morphological filters on binary images
A typical application of these filters is to refine segmentation results. A max-filter is called **dilation** whereas a min-filter is called **erosion**. Often rank filters are applied in a sequence. We refer to a **closing** operation as a max-filter followed by a min-filter of the same size. An **opening** operation is the inverse, a min-filter followed by a max-filter.

Opening operations will:
 * Remove small/thin objects which extent is below the size of the structuring element
 * Smooth border of an object

Closing operations:
 * Fill small holes below the size of the structuring element
 * Can connect gaps

Image subtraction using eroded/dilated images allows to identify the boundary of objects and is referred to **morphological gradients**:
 * Internal gradient: original - eroded
 * External gradient: dilated - original
 * (Symmetric) gradient: dilated - eroded

**Fill holes** operation is a slightly more complex morphological operation. It is used to identify background pixels surrounded by foreground pixels and change their value to foreground. Algorithmically there are several ways to achieve this.


## Morphological filters on label images
Morphological filters work also on label images. If the objects are not touching this will achieve the expected result for each label. However, when objects touch each other, operations such as dilations can lead to unwanted results.


## Morphological filters on grey level images
Min and max operations can be applied to grey level images. Applications are for example contrast enhancement, edge detection, feature description, or pre-processing for segmentation.
