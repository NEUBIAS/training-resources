---
title: Basic image analysis course overview
layout: module
tags: ["course"]
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[Data types](../datatypes)"
  - "[Display settings](../display_settings)"
  - "[Spatial calibration](../spatial_calibration)"
objectives:
  - Automatically extract biophysically meaningful numbers from microscopy images of biological samples.
motivation: |
  - Automated image analysis is more objective, reproducible and scalable than manual analysis.

concept_map: >
  graph TD
    T1("Images") --> T2("Analysis")
    T2 --> T3("Tables")

figure: /figures/basic_image_analysis_course.png
figure_legend: ""

multiactivities:

learn_next:
  - "[Segmentation overview](../segmentation)"

external_links:

---

The course will cover:

- Basic bioimage analysis steps
- Composing simple bioimage analysis workflows
- Batch processing
