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
    D("3-D image data") --> R("Volume rendering")
    R --> A("2-D image with 3-D appearance")
    R -->|VR| AA("Two 2-D image (one per eye)")
    R ---|has| M("Many methods and settings...")

figure: /figures/volume_viewer.png
figure_legend: Volume rendering examples.

activity_preface: |
  - Example data:
    - [3-D MRI head](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__mri_full_head.tif)
    - [3-D Organoid nuclei](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__organoid_nuclei.tif)
    - [3-D FIB-SEM](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__fib_sem_crop.tif)
  - Open a volume viewer.
  - Explore different volume rendering modes (as available in your softwares):
    - Maximum projection
      - Explore different camera positions
    - Volume rendering
      - Explore various transparency (alpha) mappings.
        - Interesting for [3-D FIB-SEM](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__fib_sem_crop.tif)
    - Iso-surface rendering
      - Explore various surface thresholds
      - Explore changing the light position
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

external_links:
  - "[Blender documentation](https://docs.blender.org/manual/en/2.79/render/blender_render/materials/special_effects/volume.html)"
  - "[Wikipedia: Volume rendering](https://en.wikipedia.org/wiki/Volume_rendering)"
  - "[Fiji Volume Viewer plugin](https://imagej.nih.gov/ij/plugins/volume-viewer.html)"
  - "[Drishti](https://en.wikipedia.org/wiki/Drishti_(client))"
  
---

## Volume rendering software

|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| [Napari](https://napari.org/)    |   |   |   |   |   |   |   |
| [Blender](https://docs.blender.org)   |   |   |   |   |   |   |   |
| [Drishti](https://github.com/nci/drishti)  |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
