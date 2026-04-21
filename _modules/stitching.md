---
title: Stitching of tiled images
layout: module
tags: ["draft"]
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[Projections](../projections)"
objectives:
  - Learn how to stitch tiled images into a single large image
  - Learn which parameters affect the quality of the results
motivation: |
  The Field of View (FOV) of a digital microscope is determined by the objective magnification, the intermediate magnification (e.g., camera adapter), and the physical dimensions of the detector sensor. 
  
  In cases where the structure of interest exceeds the FOV, we use tiled acquisition. This involves recording a grid of neighboring images—called tiles—with a specific percentage of overlap. In post-processing, these tiles are aligned and merged using stitching algorithms to reconstruct a single large-scale image.

concept_map: >
  graph LR
    %% Define Inputs
    subgraph Input_Data [Input Data]
      direction TB
        RawImages(Image Tiles)
        StageCoords(Grid Positions)
        Overlap(Overlap)
    end

    %% Define the Core Process
    subgraph Stitching_Core [Stitching Algorithm]
        direction TB
        Align(Step 1: Alignment)
        Blend(Step 2: Blending/Merging)
    end

    %% Define the Final Output
    LargeImage(Final Large Stitched Image)

    %% Define Connections/Flow
    RawImages --> Align
    StageCoords --> Align
    Overlap --> Align

    Align --> Blend
    Blend --> LargeImage

    %% Styling for clarity (Optional but helpful)
    classDef process fill:#f9f,stroke:#333,stroke-width:2px;
    classDef input fill:#ccf,stroke:#333,stroke-width:1px;
    classDef output fill:#cfc,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5;

    class Align,Blend process;
    class RawImages,StageCoords,Overlap input;
    class LargeImage output;

figure: /figures/stitching.png
figure_legend: TODO

multiactivities:
  - ["stitching/act01.md", [["ImageJ GUI", "stitching/act01_imagejgui.md"], ["ImageJ Macro", "stitching/act01_imagejmacro.ijm"]]]

assessment: >

  ### Fill in the blanks

    1. TODO ___ .
    1. TODO ___ .
    
    > ## Solution
    >   1. TODO
    >   1. TODO
    {: .solution}

learn_next:
  - "[TODO](../auto_threshold)"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"
---

