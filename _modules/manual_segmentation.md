---
title: Manual segmentation
layout: module
tags: ["draft"]
prerequisites:
  - "[Label mask images](../connected_components)"
  - "[Segmenation](../segmentation)"
objectives:
  - "Manually segment parts of a 2-D (3-D) image."
motivation: |
  Manual segmentation is useful in many ways. If the dataset of interest is small, manual segmentation may be faster than designing an automated segmentation workflow, or automated segmentation may be very difficult. In addition, manual segmentation can serve as training and validation data for (deep-learning based) automated segmentation algorithms.

concept_map: >
  graph TD
    I("Image") --> MS("Manual segmentation")
    MS --> LM("Label mask image")

figure: /figures/manual_segmentation.png
figure_legend: Manual segmentation in ITK-SNAP and corresponding label mask image.

activity_preface: |
  - Open the FIXME
  - Perform a manual instance segmentation of FIXME

activities:
  - ["ITK-SNAP", "manual_segmentation/activities/itk_snap.md", "markdown"]

exercises:

assessment: >

  ### Fill in the blanks

    1. Manual segmentations are often stored as ___.

    > ## Solution
    >   1. label mask images
    {: .solution}
    

learn_next:

external_links:
---

## Manual segmentation considerations

### How to deal with objects that are not fully in the image?

### Should objects be separated by background pixels?



