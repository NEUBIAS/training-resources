---
title: Spherical aberrations
layout: module
tags: ["microscopy", "image formation"]
prerequisites:
  - "[Digital image basics](./pixels)"
  - "[N-dimensional images](./multidimensional_image_basics)"
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
  - ["spherical_aberrations/act01.md", [["ImageJ GUI", "spherical_aberrations/act01_imagejgui.md"]]]


assessment: >
  ### Intensity and refractive index matching

  You compare two images of a sample deep within a tissue block. Image 1 (mounted in a high-RI clearing agent and using an oil objective) appears significantly brighter than Image 2 (mounted in PBS and using a water objectvive), despite using identical laser power and gain settings. Why does the RI-matched sample appear brighter?

  1. Clearing agents physically move the sample closer to the lens.

  2. PBS causes rapid fluorescence quenching.
  
  3. Better RI matching ensures light rays converge at a tighter focal point rather than smearing axially.
  
  4. The clearing agent increases the light-gathering capacity (NA) of the objective.
    
    > ## Solution
    > Correct Answer: 3., When spherical aberration is reduced, the Point Spread Function (PSF) is tighter, concentrating the same number of photons into a smaller volume, which increases the peak intensity.
    {: .solution}

  ### Apparent vs. Physical Depth

  When imaging through a medium with a lower refractive index than the objective's immersion medium (e.g., imaging into water with an oil objective), how does the apparent depth of a structure compare to its real physical depth?
    
    A. The structure appears at its exact physical depth
    
    B. The structure appears deeper than it actually is (Axial Scaling Error)
    
    C. The structure appears shallower than it actually is
    
    D. The structure appears wider in XY but its Z position remains accurate
    
    > ## Solution
    > Correct Answer: C, Refractive index mismatch causes light rays to bend, creating a "focal shift" that leads to axial scaling errors where structures appear at a different depth in the Z-stack than in physical reality.
    {: .solution}

learn_next:
  - ""

external_links:
  - "[SVI - Spherical aberrations](https://svi.nl/SphericalAberration)"
---

