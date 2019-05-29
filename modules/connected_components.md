---
title:     Connected components 
layout:    page
---

## Connected components analysis

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "intensity image" -> "connected component analysis" -> "label image";
    connectivity -> "connected component analysis";
  }
'/>


### Activity: 2D connected components analysis

* Open image: xy_8bit_binary__nuclei.tif
* Perform connected components analysis
* Explore multi-color LUTs for object labelling
* Explore removing and joining labels


### Activity: 3D connected components analysis

Repeat above activity but use a 3D image:

* Open image: xyz_8bit_binary__spots.tif

### Formative assessment

Fill in the blanks, using these words: less, more, 8, 255, 4, more.

1. In 3D, pixels have _____ neighbors than in 2D.
2. 8-connected connectivity results in _____ objects than 4-connected connectivity.
3. In 3D, pixels have ____ non-diagonal neighbors.
4. In 2D, pixels have ____ non-diagonal neighbors.
5. A 8-bit label image can maximally have _____ objects.
6. The maximum value in a label image is equal to or _____ than the number of objects.

## Learn next

- shape_measurements.md
