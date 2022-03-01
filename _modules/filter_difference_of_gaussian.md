---
title:     Difference of Gaussian (DRAFT)
layout:    module
---

## Difference of Gaussian (DoG)

<img src='https://g.gravizo.com/svg?
 digraph G {
        shift [fontcolor=white,color=white];
        image -> "small blur";
        image -> "large blur";
        "small blur" -> "noise filtered";
        "large blur" -> "local background";
        "small blur" -> "small blur - large blur" -> "DoG";
        "large blur" -> "small blur - large blur" -> "DoG";
        "DoG" -> "Laplacian of Gaussian (LoG)" [label="  is related"];
}
'/>

### Activity: Enhance spots in noisy image with uneven background

- Open image: xy_8bit__two_spots_noisy_uneven_background.tif
- Appreciate that you cannot readily threshold the spots
- Compute DoG:
        - Copy image and blur with a Gaussian of small sigma -> Gs
        - Copy image and blur with a Gaussian of bigger sigma -> Gb
                - For the official DoG: `rb = sqrt(2) * rs`
        - Create `DoG = Gs - Gb`
- Appreciate that now it is possible to threshold the spots in the DoG image

### Learn more

- https://imagescience.org/meijering/software/featurej/
- https://en.wikipedia.org/wiki/Difference_of_Gaussians
- https://github.com/CellProfiler/CellProfiler/blob/master/cellprofiler/modules/enhanceorsuppressfeatures.py#L4
