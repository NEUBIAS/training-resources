---
title:     Pixels 
layout:    page
---

# Pixels

## Concept map

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    image -> pixel [label="  has many"];
    pixel -> value;
    pixel -> indices;
    pixel -> voxel [label="  3D"];
  }
'/>

## Activity: Explore pixel values and indices

* Open image: xy_8bit__nuclei_noisy_different_intensity.tif
* Explore different ways to inspect pixel values and indices
* Check where the lowest pixel indices are in the displayed image:
        * Most commonly: Upper left corner, which is different to conventional coordinate systems.

## Formative assessment

True or false?

* The lowest pixel index of a 2D image always is `[1,1]`.
* When looking at a 2D image, the lowest pixel indices are always in the lower left corner.

## Learn next

- display.md
