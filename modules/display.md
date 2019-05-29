---
title:     Image display
layout:    page
---

# Image display

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    LUT -> color;
    LUT -> brightness;
    min -> LUT;
    max -> LUT;
    value -> LUT;
  }
'/>

```
brightness = ( value - min ) / ( max - min )

0 <= brightness <= 1

contrast = max - min
```

## Activity

* Open image: xy_8bit__nuclei_noisy_different_intensity.tif
* Explore different LUTs and LUT settings
        * Appreciate that LUT settings do not affect image content.


## Formative Assessment

Fill in the blanks, using those words: decrease, larger than, increase, smaller than

1. Pixels with values _____ `max` will appear saturated.
2. Decreasing `max` while keeping `min` constant will _____ the contrast.
3. Decreasing both `max` and `min` will _____ the overall brightness.
4. Pixels with values _____ the `min` will appear black, when using a grayscale LUT.
