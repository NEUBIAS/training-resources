---
title:     GUI recording
layout:    module
prerequisites:
  - "[Filter convolution](../filter_convolution)"
objectives:
  - "Record an image analysis action in a graphical user interface such that it becomes a script."
motivation: |
  Typically in a GUI, but not reproducible....blbalbaba
  
concept_map: >
  graph TD
    GUI --> S("Script")
    S --> reproducible
    S --> shareable
    S --> batchable

figure: /figures/scripting_gui_recording.png
figure_legend: GUI recording in ImageJ.

activity_preface: |
  - blabla

activities:
  - ["ImageJ Macro", "scripting_gui_recording/activities/scripting_gui_recording_activity_1.md", "markdown"]


exercises:
  - ["ImageJ GUI", "binarization/exercises/binarization_imagejgui.md"]
  - ["ImageJ Macro", "binarization/exercises/binarization_imagejmacro.md"]
  - ["ImageJ Jython", "binarization/exercises/binarization_jython.md"]

assessment: >

  ### Fill in the blanks

    - Pixels in a binary image can have maximally ___ different values.
    - If the threshold is larger than the maximal pixel value in the intensity image, all pixels in the binary image have a value of ___.
    
    > ## Solution
    >   - Pixels in a binary image can have maximally **2** different values.
    >   - If the threshold is larger than the maximal pixel value in the intensity image, 
    > all pixels in the binary image have a value of **0**.
    {: .solution}
    
  ### True or False
    - There is only one correct threshold value in order to convert an intensity image into a binary image. 
    - Binary images are always unsigned 8-bit where the foreground is 255.
    
    > ## Solution
    >   - There is only one correct threshold value in order to convert an intensity image into a binary image. **False**
    >   -  Binary images are always unsigned 8-bit where the foreground is 255. **False**
    {: .solution}

learn_next:
  - "[Automatic threshold for binarization](../auto_threshold)"
  - "[Finding objects in a binary image](../connected_components)"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"
  
---
#### Image thresholding
A common algorithm for binarization is thresholding. A threshold value `t` is chosen, either manually or automatically, 
and all pixels with intensities below `t` are set to 0, whereas pixels with intensities `>= t` are set to the value for the foreground. 
Depending on the software the foreground value can be different (e.g. 1 in MATLAB or 255 in ImageJ). At any pixel (x,y):

`p_im(x,y) < t` -> `p_bin(x,y) = 0`

`p_im(x,y) >= t` -> `p_bin(x,y) = 1`

where, p_im and p_bin are the intensity and binary images respectively.

It is also possible to define an interval of threshold values, i.e. a lower and upper threshold value. Pixels with intensity values 
within this interval belong to the foreground and vice versa. 
 

