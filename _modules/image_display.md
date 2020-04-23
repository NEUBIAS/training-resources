---
title:     Image display
layout:    module
---

# Prerequisites

- image_pixel_content

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

if ( brightness < 0 ) set to zero
if ( brightness > 1 ) set to one

0 <= brightness <= 1

contrast = max - min
```

## Activity

* Open image: xy_16bit__nuclei_high_dynamic_range.tif
* Explore different single color LUTs and LUT settings
* Appreciate that LUT settings do not change the pixel values
* Explore multi-color LUT for visualisation of high dynamic range images
	* Add a LUT calibration bar to the image


## Formative Assessment

### Fill in the blanks

Fill in the blanks, using those words: decrease, larger than, increase, smaller than

1. Pixels with values _____ `max` will appear saturated.
2. Decreasing `max` while keeping `min` constant will _____ the contrast.
3. Decreasing both `max` and `min` will _____ the overall brightness.
4. Pixels with values _____ the `min` will appear black, when using a grayscale LUT.

### TODO: Comparative image display

Open two images and display with the same LUT settings.
