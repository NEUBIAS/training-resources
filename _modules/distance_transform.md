---
title:  Distance transform
layout: module
---

<img src='https://g.gravizo.com/svg?
 digraph G {
        shift [fontcolor=white,color=white];
        "binary image" -> "distance transform" -> "distance map";
	"distance map" -> "values are distances";
}
'/>

## Activity: Explore distance transform

- Open image: xy_8bit_binary__two_objects.tif
- Learn:
	- It matters what is foreground and what is background.
	- The image data type limits the possible distance values.
	- There is a difference between calibrated vs. pixel-based distance transforms.


## Actvity: Use distance map for automated distance measurements

- Open reference object image: xy_8bit_binary__single_object.tif
- Compute distance map
- Open label image: xy_8bit_labels__two_spots.tif
- Measure "intensity" of label image objects in distance map
	- intensity is distance

## Activity: Use distance map for automated region selection

- Open reference object image: xy_8bit_binary__single_object.tif
- Compute distance map
- Threshold distance map to select regions

### Formative Assessment

TODO

### Learn more

TODO
