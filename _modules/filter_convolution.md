---
title:     Filter convolution (DRAFT)
layout:    module
---

## Convolution filters

<img src='https://g.gravizo.com/svg?
 digraph G {
    shift [fontcolor=white,color=white];
    "intensity image" -> "convolution" -> "filtered image";
    "small image" -> size;
    "small image" -> "pixel values";
    "kernel" -> "small image" [label="  is"];
    "kernel" -> "convolution";
}
'/>

### Activity: Explore convolution filters

* Open image: xy_8bit__nuclei_noisy_different_intensity.tif
* Try the result of different convolution filters, e.g.
        * https://en.wikipedia.org/wiki/Kernel_(image_processing)
        * Mean filter
        * Gaussian blur
        * Edge detection
* Appreciate that the results are (slightly) wrong within the 8-bit range of the input image.

### Activity: Use mean filter to facilitate image segmentation

* Open image: xy_8bit__nuclei_noisy_different_intensity.tif
* Appreciate that you cannot readily threshold the image
* Apply a mean filter
* Threshold the filtered image

### Formative assessment

* Draw the kernel of a 3x3 mean filter.
* Draw three different kernels that enhance edges.

### Learn more

* https://en.wikipedia.org/wiki/Kernel_(image_processing)
