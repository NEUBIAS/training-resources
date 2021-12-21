---
title:     Script functions
layout:    module
prerequisites:
  - "[Basic properties of images and pixels](../pixels)"

objectives:
  - "Describe the purpose of a function in a script."
  - "Demonstrate the usage and flow of a function."
  - "Make the script more efficient."
motivation: |
  When a series of steps(i.e. algorithm) that has to be performed on an image or a set of images should be executed more than once, or when the script gets too long and repetitive, it is more efficient to write this series as modules called "functions".
  This essentially means that you can reuse parts of code instead of rewriting it. A function is a block that can be called with inputs and can return values.

concept_map: >
  graph TD
    IV("Input values-None") --> F(Function (Set of operations))
    F --> OV("Output values-None")

figure: /figures/Function_demonstration.png
figure_legend: Components and working of a function within a script.

activity_preface: |
  - Run the script and try to calculate mean intensity of 2 different slices.

activities:
  - ["ImageJ Macro", "script_functions/activities/Function_display_slice.ijm", "java"]

exercises:
  - ["ImageJ Macro", "script_functions/exercises/functions_imagejmacro.md"]

assessment: >

  ### True or False
    - The values returned by function cannot be used outside of the function.
    - Function can be called multiple times within a script.

    > ## Solution
    >   - It can be used unless the variable returned is not overwritten. **False**
    >   -  **True**
    {: .solution}

learn_next:
  -

external_links:
  - "[Wikipedia: Subroutine](https://en.wikipedia.org/wiki/Subroutine)"

---
