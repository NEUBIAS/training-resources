---
title:     Variables
layout:    module
prerequisites:
 - [TODO add links]
objectives:
  - "Explain concept of variable"
  - "Run minimal example of computation using a variable"
motivation: |
  A variable is an essential concept in programming, it allows to structure and generalize a script/program.
  A variable stores a value, e.g. a numeric value, that can be used and changed at several occasions in 
  a script.
  
  
concept_map: >
  graph TD
    V("Variable") --> |has|Name("Symbolic Name")
    V --> |has|Type("Type")
    V --> |has|Value("Value")
    V --> |is| Stored("Stored in memory")
    Value --> |can| Change

figure: /figures/variables.png
figure_legend: 
   Variables are containers specific for an information type. The name of the variable should explain 
   its purpose. Naming convention is CamelCase (left side) or under_score (right side).

activity_preface: |
  - Open the binary image [xy_8bit_binary__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei.tif).
  - Discuss the image data type and the pixel values.
  - Open the image [xy_8bit__two_cells.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif) and binarize it by applying a manually defined threshold.

activities:
  - ["ImageJ GUI", "binarization/activities/binarization_imagejgui.md", "markdown"]
  - ["ImageJ Macro", "binarization/activities/binarization_imagejmacro.ijm", "java"]
  - ["ImageJ Jython", "binarization/activities/binarization_jython.py", "python"]
  - ["MATLAB", "binarization/activities/binarization_matlab.m", "matlab"]
  - ["KNIME", "binarization/activities/binarization_knime.md", "markdown"]
  - ["Python", "binarization/activities/binarization.py", "python"]

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
 
 
 