---
title: Functions
layout: module
tags: ["scripting"]
prerequisites:
  - "[Variables](../script_variables)"
  - "[Loops](../script_for_loops)"
objectives:
  - "Wrap a piece of code into a function."
  - "Understand the skeleton of a function."
motivation: |
  When a series of steps (i.e. algorithm) that has to be performed on an image or a set of images should be executed more than once, or when the script gets too long and repetitive, it is more efficient to wrap such series of steps into a "function".
  This essentially means that you can reuse parts of code instead of rewriting it. A function is a block that has a specific name and can be called with inputs and can return values.

concept_map: >
  graph TD
    IV("Input values") --> F("Function")
    F -->|generates| OV("Output values")
    F -->|contains| RC("Reusable code")

figure: /figures/script_functions.png
figure_legend: Components and working of a function within a script.

multiactivities:
  - ["script_functions/add_two_numbers_activity1.md", [["skimage napari", "script_functions/add_two_numbers_activity1_skimage_napari.py"]]]
  - ["script_functions/open_inspect_image_activity2.md", [["skimage napari", "script_functions/open_inspect_image_activity2_skimage_napari.py"]]]

assessment: >

  ### True or False
    - The variables defined within the function can be used outside of the function.
    - Same function can be called multiple times within a script.

    > ## Solution
    >   -  **False**. It cannot be used unless the variable is returned by this function.
    >   -  **True**. In fact, calling the function multiple times is sort of the point of writing the function.
    {: .solution}

learn_next:
  - "[Batch processing](../batch_processing)"

external_links:
  - "[Wikipedia: Subroutine](https://en.wikipedia.org/wiki/Subroutine)"
---
