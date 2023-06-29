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
    R -->|"Virtual Reality"| AA("Two 2-D images (one per eye)")
    R ---|has| M("Many methods and settings...")

figure: /figures/volume_viewer.png
figure_legend: Volume rendering examples.

multiactivities:
  - ["volume_viewer/volume_rendering.md", [["ImageJ 3D Viewer", "volume_viewer/volume_rendering_imagej_3dviewer.md"], ["skimage napari", "volume_viewer/volume_rendering_skimage_napari.py"]]]


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

| Software | Multi-Channel | Time-lapse |  Max-Projection  | Volume | Iso-Surface  | ...  | ...  | ...  | ...  |
|---|---|---|---|---|---|---|---|
| [Blender](https://docs.blender.org)  | | |   |   |   |   |   |   |   |
| [Drishti](https://github.com/nci/drishti) | | |   |   |   |   |   |   |   |
| [ImageJ 3Dscript](https://imagej.net/plugins/3dscript) |  |  |   |   |  |   |   |   |   |
| [ImageJ 3D viewer](https://imagej.net/plugins/3d-viewer/) | N | N | N  | Y  | Y |   |   |   |   |
| [ImageJ ClearVolume (Upate Site)](https://imagej.net/plugins/clearvolume)  | Y  | Y | Y  | N  | N  |   |   |   | 
| [ImageJ Volume Viewer](https://imagej.nih.gov/ij/plugins/volume-viewer.html) | N | N  | Y | Y  | N  |   |   |   |   |
| [Napari](https://napari.org/)    |  |   |   |   |  |  |  |   |   |
