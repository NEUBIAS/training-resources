---
title: Handling script parameters
layout: module
prerequisites:
  - "[Running a script](../script_run)"
  - "[Setting a scripting environment](../script_env)"
objectives:
  - "Organise script parameters in the code such that can be easliy adapted"
  - "Create dialog boxes for fetching scripting parameter"

motivation: |
  Scripts typically have parameters that one would like to change while leaving the core of the code untouched. Examples for such changable parameteres are the input image file and some image processing parameters such as filter sizes and thresholds. It is very important to learn how to "expose" such parameters in ways that do not require digging into and modifying the actual code too much.

concept_map: >
    graph TD
      S("Script") ---|has| P("Parameters")
      S ---|may have| CB
      S ---|may generate| UI
      CB("Special code block") --> P
      UI("UI elements") --> P
      CF("Config file") --> P
      A("Script arguments") --> P

figure: /figures/fetching_user_input.png
figure_legend: Schematic code examples for how parameters may be stored inside or passed from outside to a script.

activity_preface: |
  - Open a script and identify whether it contain parameters
  - Modify the script to implement different options for exposing these parameters (e.g., as show in above figure)

activities:
- ["ImageJ Macro", "fetching_user_input/activities/fetch_user_input_imagejmacro.md", "markdown"]

exercise_preface: |
  - Open a script and identify whether it contain parameters
  - Modify the script to implement different options for exposing these parameters (e.g., as show in above figure)

exercises:
- ["ImageJ Macro", "fetching_user_input/activities/createImage.ijm", "java"]

assessment: >

  ### Discussion
    1. Generally, what could be the pros and cons (considerations) of the different ways (see figure and concept map) in which scripting parameters can be handled?
    1. Specifically, what are the pros and cons of using UI elements for fetching parameters?
    
    > ## Solution
    >   1. This is a complex topic. Considerations could be: (i) How can I keep track which images were analyzed with which parameters? (ii) How can I ensure that users of my script use valid parameters? (iii) How experienced are the users of my script (e.g. would they be able to modify the script itself)? (iv) If the script itself is modified when changing a parameter, how do I keep track of the different "versions" of the script? 
    >   1. Pro: UI elements typically allow you to restrict the input values to a valid range and it makes your script easy to use for people without programming experience. Con: Every time you want to run the script you have to interact with the UI and, unless you implement something special, you don't keep track which parameters were used to run the script.
   {: .solution}

learn_next:

external_links:
  - "[Scijava script parameters](https://imagej.net/scripting/parameters)"
  - "[Napari magic GUI](https://napari.org/magicgui/)"
---
