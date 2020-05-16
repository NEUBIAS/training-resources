---
title:     Filter object properties by neighbor properties
layout:    module
---

# Neighbors of neighbors

## Requirements

- Neighbourhood filters
- Rank filters

## Motivation

This module shows how to apply a filter to values of a graph, considering neighbors of neighbors.

## Learning objectives
- Understand how to construct a graph from a label image
- Understand neighbor-hood relation ships

### Activity: Initialize GPU
activities:
  "CLIJ2 Macro": "filter_neighbor_objects/init_gpu.md"

### The dataset
We start with a list of random point coordinates, draw a spots image
and partition the image space between these points.

### Activity: Make a random labelmap
activities:
  "CLIJ2 Macro": "filter_neighbor_objects/random_labelmap.md"

# figure: /figures/filter_neighbor_objects/image_1588707389177.png
# figure_legend: Random labels

Before running operations on neighbors, we need to determine which labels of the
label map are neighbors. Furthermore, we can draw the neighborhood relationships as a graph/mesh.

### Activity: Make a random labelmap
activities:
  "CLIJ2 Macro": "filter_neighbor_objects/generate_touch_matrix.md"

# figure: /figures/filter_neighbor_objects/image_1588707389261.png
# figure_legend: A graph derived from the labelmap

## Distribute values in space
We get the center of mass of all objects in our label map and generate vector
measurement values which are a bit random, but also differ on the left and
right side of the image.

### Activity: Make a random labelmap
activities:
  "CLIJ2 Macro": "filter_neighbor_objects/distribute_values.md"

## Create a parametric image showing measurements in 2D space

## Activity: Draw parametric image
activities:
  "CLIJ2 Macro": "filter_neighbor_objects/draw_parametric_image.md"

# figure: /figures/filter_neighbor_objects/image_1588707389508.png
# figure_legend: Mean intensity of neighbors

## Smoothing between neighbors
We can apply smoothing operations, e.g. the mean filter:

## Activity: Mean of neighbors
activities:
  "CLIJ2 Macro": "filter_neighbor_objects/mean_of_neighbors.md"

# figure: /figures/filter_neighbor_objects/image_1588707389595.png
# figure_legend: Mean intensity of neighbors

To prevent the orange stripe in the center, we use the median filter:

## Activity: Median of neighbors
activities:
  "CLIJ2 Macro": "filter_neighbor_objects/median_of_neighbors.md"

# figure: /figures/filter_neighbor_objects/image_1588707389685.png
# figure_legend: Median intensity among neighbors

Based on that image, we can visualize the border:

## Activity: Standard deviation of neighbors
activities:
  "CLIJ2 Macro": "filter_neighbor_objects/stddev_of_neighbors.md"

# figure: /figures/filter_neighbor_objects/image_1588707389789.png
# figure_legend: Standard deviation of mean intensities between neighbors

## Increasing the radius of operation
Furthermore, we can increase the radius of operation by using `neighborsOfNeighbors();`.
When applying the mean filter, one can see a wider orange stripe in the middle of the image.

## Activity: Mean of neighbors of neighbors
activities:
  "CLIJ2 Macro": "filter_neighbor_objects/mean_of_neighbors_of_neighbors.md"

# figure: /figures/filter_neighbor_objects/image_1588707389916.png
# figure_legend: Mean intensity of neighbors of neighbors

At the end of the macro, clean up:

## Activity: Clean up
activities:
  "CLIJ2 Macro": "filter_neighbor_objects/cleanup.md"


