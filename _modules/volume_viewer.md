---
title: Volume viewer
layout: module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"
  - "[Look up tables](../lut)"

objectives:
  - "Visualize data in 3D."
  - "Explore the data using different visualization settings."
  - "Creating animations."
motivation: |
  When the structures that one wants to in 3D image datasets are obscured in the 2D visualization, exploring and understanding the data in 3D can be much intuitive and easier. Occlusion cannot happen in 2D, therefore, one can visualize occluded objects in 3D by changing the transparency of objects occluding them. The "Volume Viewer" plugin in Fiji can be used for this purpose. It also allows to use intensity  and transparency settings to highlight regions of interest and save snapshots that can be used to create a custom animation.

concept_map: >
  graph TD
    Input 3D data("Already opened in Fiji") --> Volume Viewer("Plugins -> Volume Viewer")
    Volume Viewer --> Snapshots/Animations

figure: /figures/volume_viewer.png
figure_legend: Flowchart of volume viewer.


activity_preface: |
  - Open an 3D image stack (File -> Open Samples -> T1 Head(16-bits)) in Fiji.
  - Open Plugins -> Volume Viewer.
  - Rendering modes:
      - Slice
      - Slice and borders
      - Max projection
      - Projection
      - Volume
  - Play with LUT transfer function and see its effect on the displayed data.
  - Rotate to see the front pose of the face.
  - Make a snapshot.  
  - Create a custom animation making more snapshots and using Image -> Stacks -> Images to Stack.

exercises:
  - ["Exercise1 - ImageJ", "volume_viewer/exercises/volume_viewer_exercise.md"]
  - ["Exercise2 - ImageJ", "volume_viewer/exercises/volume_viewer_exercise2.md"]


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
  - "[Fiji Volume Viewer plugin](https://imagej.nih.gov/ij/plugins/volume-viewer.html)"

---
