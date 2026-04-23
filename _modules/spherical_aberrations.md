---
title: Spherical aberrations (DRAFT)
layout: module
tags: ["microscopy", "image formation", "DRAFT"]
prerequisites:
  - ""
objectives:
  - "Intensity Loss (Dimming): Understand why light fails to converge at a single focal point, leading to a  dimmer and less contrasty signal"
  - "Learn how the difference between your immersion oil and your sample environment triggers these aberrations."
  - "Z-Shift and Scaling: Identify why objects appear at the wrong depth or seem elongated/shortened in 3D space."

motivation: |
  Spherical aberrations create blurry and low contrast images. The aberrations are dynamic and are often introduced by the sample itself (cover glass thicknes, refractive index mismatch in immersion/mounting/sample media, depth of the sample ...). 
  
  It is important to understand the effect of spherical aberrations to:
  - correctly interpret the imaging results, 
  - adapt the experimental protocol

concept_map: >
 graph TD
    %% 1. Root Causes
    subgraph Causes [Root Causes]
        RI["Refractive Index (RI)<br>Mismatch"]
        CG["Wrong Coverglass<br>Thickness"]
        SD["Imaging Deep<br>into Tissue"]
    end

    %% 2. The Physical Mechanism
    Phys["Non-coincident focal points:<br>Marginal rays vs. Central rays"]

    %% 3. Image Artifacts
    subgraph Artefacts [Image Artefacts]
        Asym["Asymmetric PSF<br>(Z-Smearing)"]
        Loss["Intensity Drop<br>(Dimmer Signal)"]
        ZErr["Axial Scaling Error<br>(Depth Distortion)"]
    end

    %% 4. Solutions
    subgraph Solutions [How to Fix]
        Coll["Correction Collar<br>Adjustment"]
        Mount["RI Matching<br>(Mounting Media)"]
        Water["Matching Immersion<br>Objectives"]
    end

    %% Logical Flow
    Causes --> Phys
    Phys --> Artefacts
    Artefacts -.-> Solutions

    %% Styling for 10.7.0
    classDef cause fill:#f1f1ff,stroke:#0984e3,stroke-width:2px;
    classDef phys fill:#fff7e6,stroke:#ffa502,stroke-width:2px;
    classDef art fill:#fff1f1,stroke:#d63031,stroke-width:1px,stroke-dasharray: 5 5;
    classDef sol fill:#f1fff1,stroke:#27ae60,stroke-width:2px;

    class RI,CG,SD cause;
    class Phys phys;
    class Asym,Loss,ZErr art;
    class Coll,Mount,Water sol;

figure: /figures/spherical_aberrations.png
figure_legend: Spherical aberrations occurr when oblique light rays entering a lens are focused in a different plane than the central rays. The result is that ray of light coming from the same source are out of focus relative to each other. This causes change in dimension of the object, blur, and loss in intensity. The effect is particularly visible deeper in a sample.

multiactivities:
  - ["spherical_aberrations/act01.md", [["ImageJ GUI", "spherical_aberrations/act01_imagejgui.md"], ["skimage napari", "spherical_aberrations/act01_skimage_napari.py"]]]


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
  - "[SVI - Spherical aberrations](https://svi.nl/SphericalAberration)"
---

