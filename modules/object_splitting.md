---
title:     Object splitting
layout:    page
---

# Object splitting

## Requirements

- binarisation.md
- distance_transform.md

## "Intensity based" watershed

<img src='https://g.gravizo.com/svg?
 digraph G {
        shift [fontcolor=white,color=white];
        "intensity image" -> "watershed" -> "label image";
	"label image" -> "pond regions";
}
'/>

### Activity: Explore intensity based watershed 

- Open image: xy_8bit__touching_objects.tif
- Invert image for watershed 
- Apply watershed

### Activity: Use intensity based watershed for object segmentation

- Open intensity image: xy_8bit__touching_objects.tif
- Threshold intensity image => binary image (aka "mask")
- Invert intensity image for watershed 
- Apply watershed, using the mask

## "Shape based" watershed

<img src='https://g.gravizo.com/svg?
 digraph G {
        shift [fontcolor=white,color=white];
        "binary image" -> "distance map" -> "watershed" -> "label image";
	"label image" -> "thickness ponds";
}
'/>

### Activity: Explore shape based watershed

- Open image: xy_8bit__touching_objects_same_intensity.tif
- Threshold -> Binary image
	- Copy binary image (we'll need it as mask later...)
- Binary image -> Distance map
- Distance map -> Watershed 


### Learn more

TODO

### Formative Assessment

TODO

