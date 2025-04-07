---
title: Basic batch analysis course overview
layout: module

prerequisites:

objectives:
  - "Create a script for automated batch analysis of many images"

motivation: |
  In order to make statistically significant conclusions one must analyse several images of several samples. To do so, being able to devise an automated batch analysis is very useful.

concept_map: >
  graph TD
    I("Images") --> B("Automated analysis")
    O("Measurements")

figure: /figures/batch_processing.png
figure_legend: "Batch processing of several images, yielding as many segmentations and object measurement tables."

learn_next:

external_links:

---

### General comments

Batch analysis of images can be done in various ways. Some image analysis software packages offer in-built funtionality to perfom automated batch analysis. In addition, there are dedicated **workflow management systems** that can be employed to deploy workflows on high-performance compute infrastructure.

Under the hood, we would argue that all these solutions contain the folloing components:

- Functionality to execute the same analysis for many input images. 
- Functionality to create output data based on the input data, often with file names that are derived from the input data, e.g. if the input is "image001.tif" the output could be "image001_segmented.tif"
- Analysis "functions", i.e., analysis "modules" that are applied to the input

In this course we will learn how to perform such basic batch analysis, using **scripting**.