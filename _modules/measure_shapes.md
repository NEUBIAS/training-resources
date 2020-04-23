---
title:     Object shape measurements
layout:    module
---

## Shape measurements

<img src='https://g.gravizo.com/svg?
 digraph G {
        shift [fontcolor=white,color=white];
        "label image" -> shape_analysis -> table;
        table -> object_rows;
        table -> feature_columns;
        table -> visualisation;
}
'/>


### Activity: Measure object shape parameters

* Open image: xy_8bit_labels__four_objects.tif
* Perform shape measurements and discuss their meanings.
* Explore results visualisation
        * Color objects by their measurement values.
* Add a calibration to the image and check which shape measurements are affected.
* Draw a test image to understand the shape measurements even better.

### Activity: Explore sampling limits

* Draw a square (=circle) of 2x2 pixels (paper, whiteboard, ...)
        * Measure area, perimeter and circularity
        * Discuss the results
* Discuss the England's coastline paradox


### Formative assessment

True or false? Discuss with your neighbour!

* Circularity is independent of image calibration.
* Area is independent of image calibration.
* Perimeter can strongly depend on spatial sampling.
* Volume can strongly depend on spatial sampling.
* Drawing test images to check how certain shape parameters behave is a good idea.

### Learn more

* Especially surface and perimeter measurements are affected by sampling and resolution, see for example:
        * https://en.wikipedia.org/wiki/Coastline_paradox).
* Results visualisation:
        * https://imagej.net/MorphoLibJ#Grayscale_morphological_filters: **Label visualization in 3D viewer**

## Learn next

- object_shape_measurement_workflow.md
- intensity_measurements.md
