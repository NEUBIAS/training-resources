---
title: Volume rendering
layout: module
prerequisites:
  - "[Projections](../projections)"
  - "[Volume slicing](../volume_slicing)"

objectives:
  - "Understand the concepts and some methods of 3-D rendering."
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
  - ["volume_viewer/volume_rendering.md", [["ImageJ 3D Viewer", "volume_viewer/volume_rendering_imagej_3dviewer.md"], ["skimage napari", "volume_viewer/volume_rendering_skimage_napari.py"], ["napari standalone app", "volume_viewer/volume_rendering_napari_gui.md"]]]



assessment: >

  ### True or False
    - Surface rendering and volume rendering are identical words for the same 3-D visualisation method.
    - Volume rendering is particularly useful for data containing very dense 3-D information such as very many cells or nuclei in an organ of a biological specimen.
    - Volume rendering is a simple algorithm that can easily be used without expert knowledge.
    - Volume rendering is very useful to get an impression of the morphology and spatial distribution of objects.

    > ## Solution
    >   - False. Although both methods are used for 3-D rendering they are different. In surface rendering one needs to define "the shell" of an object and only this will be visible. In volume rendering the intensity of all voxels can be represented such as in a maximum intensity projection based volume rendering.
    >   - False. If the data is very dense, there is a high probabilty that no matter from which angle you look there will be objects hidden behind other objects. Thus, sparse data can be more suited to 3-D rendering than very dense data.
    >   - False. In fact, volume rendering is very complex and there are many things to learn to master it (see for example [this website](https://developer.nvidia.com/gpugems/gpugems/part-vi-beyond-triangles/chapter-39-volume-rendering-techniques).
    >   - True. If the sample is not too dense, volume rendering allows one to get a quick overview of the whole 3-D specimen and its morphology.
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
