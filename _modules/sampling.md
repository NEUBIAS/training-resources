---
title: Image sampling
layout: module
tags: ["draft", "microscopy", "image formation", "sampling"]
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[Point spread function](../psf)"
objectives:
  - Explain how spatial and axial sampling discretize a continuous optical image.
  - Identify under-sampling artifacts such as aliasing and loss of structural information.
  - Recognize over-sampling and its practical costs (data volume, phototoxicity, acquisition time).
  - Understand the optimal sampling depends on the biological question.
motivation: |
  In microscopy, image quality is not only limited by optics, but also by how finely the image is sampled.
  Even a perfect microscope can produce misleading data if the sampling is inappropriate.
  Under-sampling throws away biophysical information that can never be recovered, while over-sampling creates the illusion of higher resolution at the cost of time, light dose, and storage. Understanding image sampling means knowing how much information your experiment actually contains — and how much you really need to record.
concept_map: >
  graph TD
    A[Continuous Optical Image] -->|Sampling| B[Discrete Pixels & Voxels]
    B --> C{Sampling Regime}
    C -->|Under-sampling| D[Aliasing & Information Loss]
    C -->|Optimal sampling| E[Faithful Representation]
    C -->|Over-sampling| F[Redundant Data]
    F --> G[Longer Acquisition / Photobleaching]
    D --> H[Biased Measurements]
figure: /figures/sampling.png
figure_legend: "Fluorescent nuclei, acquired at different spatial sampling; scale bar 5 micrometer. Left: Intranuclear structures can be investigated; dividing cell can be clearly identified. Middle: Intracellular structures are not visible but the number of nuclei could still be measured. Right: Nuclei in the top left start to blur into one object, rendering cell counting challenging. **TODO: Replace this by a proper image**"
multiactivities:
  - ["sampling/downsampling.md", [["ImageJ Macro", "sampling/downsampling_imagejmacro.ijm"]]]

assessment: |

  ### Fill in the blanks

  1. If the pixel size is larger than half the width of the PSF, the image is \_\_\_\_\_-sampled and fine spatial detail is \_\_\_\_\_.
  1. Over-sampling does not improve true optical resolution, but it increases \_\_\_\_\_, \_\_\_\_\_, and \_\_\_\_\_.

  > ## Solution
  > 1. under; lost
  > 1. data volume; acquisition time; photobleaching
  {: .solution}
---