---
title: Volume rendering
layout: module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Look up tables](../lut)"

objectives:
  - "Visualize image data in 3D."
  - "Explore the data using different visualization settings."
  - "Creating animations."
motivation: |
  TODO

concept_map: >
  graph TD
    D("3-D image data") --> VR("Volume rendering")
    VR --> A("One 2-D image")
    VR -->|VR| AA("Two 2-D images (one pe eye)")
    A ---|has| P(Perspective and camera position)
    VR --- IS("Iso-surface")
    VR --- MP("Maximum projection")

figure: /figures/volume_viewer.png
figure_legend: Volume rendering.

activity_preface: |
  - Open a [calibrated 3-D MRI image](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__mri_full_head.tif)
  - Open a volume viewer.
  - Explore different rendering modes:
    - Maximum projection
    - Iso-surface rendering
      - Explore the surface threshold value.
  - Change transfer function and see explore effect on the displayed data.
  - Change camera position to explore different views.
  - Save a snapshot.
  - Create and save a custom animation, e.g. rotating the image.

acitivities:
  - ["ImageJ 3D Viewer", "volume_viewer/activities/3d_viewer.md", "markdown"]

exercises:
  - ["ImageJ Volume Viewer: 1", "volume_viewer/exercises/volume_viewer_exercise.md"]
  - ["ImageJ Volume Viewer: 2", "volume_viewer/exercises/volume_viewer_exercise2.md"]


assessment: >

  ### True or False
    - The actions performed in Volume Viewer GUI can be recorded.
    - Changing transfer functions will affect the data.

    > ## Solution
    >   - **False**
    >   - **False**
    {: .solution}

learn_next:
  -

external_links:
  - "[Wikipedia: Volume rendering](https://en.wikipedia.org/wiki/Volume_rendering)"
  - "[Fiji Volume Viewer plugin](https://imagej.nih.gov/ij/plugins/volume-viewer.html)"
-
---
