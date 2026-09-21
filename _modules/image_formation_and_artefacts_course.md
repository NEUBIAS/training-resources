---
title: Image formation and imaging artefacts course overview
tags: ["course"]
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[Data types](../datatypes)"
  - "[Neighborhood filters](../filter_neighbourhood)"
  - "[Projections](../projections)"
objectives:
  - "Understand how an image is formed"
  - "Understand how artefacts affect the final image and the analysis"
  - "Understand how to mitigate imaging artefacts"
motivation: |
  To get reliable and quantifiable data, it is important to understand how an image is formed and what can be quantified depending on the image properties. The imaging process does not generate an exact representation of the "real" structure. For instance, small structures may not be distinguishable due to the instrinsic blur induced by a microscope (resolution limit), measured intensities may be affected by the position of an object in the field of view. 

concept_map: >
  graph LR
    %% 1. IMAGE FORMATION (Top Layer - LR)
    subgraph Formation [Image Formation]
        direction LR
        Light[Light Source] --> Sample[Sample]
        Sample --> Optics[Optics]
        Optics --> Detector[Detector]
        Detector --> Raw[Raw Image]
    end

    %% 2. ARTEFACTS (Bottom Layer - LR)
    subgraph Artefacts [Artefacts]
        direction LR
        SampleAb["Bleaching<br>Refractive index mismatch<br>Labelling<br>..."]
        OptAb["Blur<br>Shading<br>Spherical<br>Chromatic<br>Crosstalk..."]
        DetAb["Sampling / Aliasing<br>Noise<br>Saturation<br>..."]
        
        %% Force LR order in the bottom row
        SampleAb ~~~ OptAb ~~~ DetAb
    end

    %% 3. CORRECTIONS (Right Layer - TB)
    subgraph Correction [Corrections]
        direction TB
        Raw --> Proc{Processing}
        Proc --> BC[Bleach Correction]
        Proc --> FFC[Flat-field Correction]
        Proc --> Decon[Deconvolution]
        Proc --> Pdot[...]
        BC & FFC & Decon & Pdot --> Final[Final Image]
    end

    %% POSITIONING CONSTRAINTS
    %% ASSOCIATIONS (Vertical lines linking stage to artifact)
    Light --- OptAb
    Light --- SampleAb
    Sample --- SampleAb
    Optics --- OptAb
    Detector --- DetAb
    %% Force Artefacts subgraph to start below Formation subgraph
    Light ~~~ SampleAb
    Sample ~~~ SampleAb
    Optics ~~~ OptAb
    Detector ~~~ DetAb

 

    %% STYLING
    classDef art fill:#fff1f1,stroke:#d63031,stroke-width:1px,stroke-dasharray: 5 5;
    classDef form fill:#f1fff1,stroke:#27ae60,stroke-width:2px;
    classDef corr fill:#f1f1ff,stroke:#0984e3,stroke-width:2px;

    %% Fixed case-sensitivity for OptAb
    class SampleAb,OptAb,DetAb art;
    class Light,Sample,Optics,Detector,Raw form;
    class Proc,BC,FFC,Decon,Final corr;

figure: /figures/image_formation_and_artefacts_course.png
figure_legend: The quality of the results depends on sample preparation, mode of acquisition, and analysis pipeline. 

multiactivities:

learn_next:
  - 

external_links:
  - 
---

