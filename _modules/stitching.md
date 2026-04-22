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
        Align(Step 1: Alignment and registration)
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
  - ["stitching/act02.md", [["ImageJ GUI", "stitching/act02_imagejgui.md"]]]
assessment: >


  ### Why is it standard practice to include an overlap (typically 10-20%) between adjacent tiles during acquisition?

    1. To increase the overall magnification of the final mosaic
    2. To provide redundant information used by registration algorithms to calculate the exact alignment
    3. To compensate for the low light sensitivity of the detector
    4. To ensure that the file size of each tile remains constant
    
    > ## Solution
    >   2 Registration algorithms (like phase correlation or feature matching) require a shared region to identify corresponding 
    {: .solution}

  ### Illumination Artifacts
  If individual tiles exhibit "vignetting" (darker edges) and are stitched together without prior correction, what is the most likely result in the final large image?
    1. The image will appear perfectly seamless.
    2. The resolution of the image will decrease by 50%.
    3. A visible "checkerboard" pattern or grid-like intensity variations will appear across the mosaic.
    4. The colors in the center of the image will shift toward the red spectrum.
    
    > ## Solution
    >   3  Uneven illumination causes "shading" at the tile borders. To avoid this, flat-field correction must be applied to each tile before the stitching process to ensure intensity homogeneity.
    {: .solution}
  


external_links:
  - "[BigStitcher: OpenSource to sticht very large data sets](https://imagej.net/plugins/bigstitcher/index)"
  - "[Imaris stitcher: commercial software](https://imaris.oxinst.com/learning/view/article/imaris-stitcher-technology)"
  - "[Image registration in general](https://imagej.net/imaging/registration)"
---

