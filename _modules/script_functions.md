---
title: Functions
layout: module
tags: ["draft","scripting"]
prerequisites:
  - "[Variables](../script_variables)"

objectives:
  - "Avoid code duplication using functions."
  - "Understand the skeleton of a function."
  - "Make the script more efficient."
motivation: |
  When a series of steps(i.e. algorithm) that has to be performed on an image or a set of images should be executed more than once, or when the script gets too long and repetitive, it is more efficient to write this series as modules called "functions".
  This essentially means that you can reuse parts of code instead of rewriting it. A function is a block that has a specific name and can be called with inputs and can return values.

concept_map: >
  graph TD
    IV("Input values") --> F("Function")
    F -->|generates| OV("Output values")
    F -->|contains| RC("Reusable code")

figure: /figures/script_functions.png
figure_legend: Components and working of a function within a script.

activity_preface: |
  - Open an image stack
  - Enter the slice numbers for which you want to calculate mean intensity.
  - Run a function to extract the specified slices, display them and calculate their mean intensity.
  - Display the mean intensity value for each specified slice.

activities:
  - ["ImageJ Macro", "script_functions/activities/function_display_slice_imagejmacro.ijm", "java"]

exercises:
  - ["Exercise1 - ImageJ Macro", "script_functions/exercises/functions_imagejmacro.md"]
  - ["Exercise2 - ImageJ Macro", "script_functions/exercises/functions_imagejmacro2.md"]

assessment: >

  ### True or False
    - The variables defined within the function can be used outside of the function.
    - Same function can be called multiple times within a script.

    > ## Solution
    >   - It cannot be used unless the variable is returned by this function. **False**
    >   -  **True**
    {: .solution}

learn_next:
  -

external_links:
  - "[Wikipedia: Subroutine](https://en.wikipedia.org/wiki/Subroutine)"

---
