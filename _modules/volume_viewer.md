---
title: Volume rendering
layout: module
prerequisites:
  - "[Volume projections](../projections)"
  - "[Volume slicing](../volume_slicing)"

objectives:
  - "Understand the concepts and some methodes of 3-D rendering."
  - "Appreciate that 3-D rendering can be challenging for some data."
  - "Perform basic volume rendering using a software tool."

motivation: |
  Intuitively grasping 3-D shapes requires visualisation of the whole object.
  This is not possible when just looking at one or several slices of a 3-D data set.
  Thus is it important about different volume rendering techniques that can create a 3-D appearance of the whole image.
  This is especially useful for sparse data, where individual 2-D slices only contain a small subset of the relevant information.

concept_map: >
  graph TD
    D("3-D image data") --> R("Volume rendering")
    R --> A("2-D image with 3-D appearance")
    R -->|VR| AA("Two 2-D images (one per eye)")
    R ---|has| M("Many methods and settings...")

figure: /figures/volume_viewer.png
figure_legend: Volume rendering examples.

activity_preface: |
  - Example data:
    - [3-D+t Chromosome congression](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzt_8bit__starfish_chromosomes.tif)
      - Useful to see in 3-D rendering (as it is very hard to see what is going on in 2-D slices)
    - [3-D EM and segmentation](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit__em_synapses_and_labels.tif)
      - EM data is difficult to render in 3-D but for the segmentation channel it is very useful
    - [3-D MRI head](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__mri_full_head.tif)
      - Good to compare various rendering modes
    - [3-D Organoid nuclei](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__organoid_nuclei.tif)
      - Challenge: Outer nuclei occulde inner nuclei
    - [3-D FIB-SEM](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__fib_sem_crop.tif)
      - Challenge: Dense signal, background is bright
    - [3-D Tissue segmentation label mask](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated_labels__platy_tissues.tif)
      - Challenge: Epithelial tissue occludes inside
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


assessment: >

  ### True or False
    - TODO.

    > ## Solution
    >   - **TODO**
    {: .solution}

learn_next:

external_links:
  - "[Blender documentation](https://docs.blender.org/manual/en/2.79/render/blender_render/materials/special_effects/volume.html)"
  - "[Wikipedia: Volume rendering](https://en.wikipedia.org/wiki/Volume_rendering)"
  
---

## Volume rendering software

| Software  | Multi-Channel | Time-lapse |  Max-Projection  | Volume | Iso-Surface  | ...  | ...  | ...  | ...  |
|---|---|---|---|---|---|---|---|
| [Blender](https://docs.blender.org)  | | |   |   |   |   |   |   |   |
| [Drishti](https://github.com/nci/drishti) | | |   |   |   |   |   |   |   |
| [ImageJ 3D viewer](https://imagej.net/plugins/3d-viewer/) | N | N | N  | Y  | Y |   |   |   |   |
| [Napari](https://napari.org/)    |  |   |   |   |  |  |  |   |   |
| [ImageJ Volume Viewer](https://imagej.nih.gov/ij/plugins/volume-viewer.html) | N | N  | Y | Y  | N  |   |   |   |   |
| [ImageJ ClearVolume (Upate Site)](https://imagej.net/plugins/clearvolume)  | Y  | Y | Y  | N  | N  |   |   |   |   |
