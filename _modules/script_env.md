<<<<<<< Local Changes
---
title:     Setting up a scripting environment
layout:    module
prerequisites:

objectives:
  - "Set up a scripting environment for your platform"
motivation: |
  In order to run image analysis scripts you need a platform where you can actually excute those scripts. 
  In this module there is a collection of installation instructions for some common platforms.
  
concept_map: >
  graph TD
    S("Script") -->|contains| C("Code")
    E("Environment") -->|executes| C
    S("Script editor") -->|modifies| C
    S("Script editor") -->|may have| A("Auto-completion")
    S("Script editor") -->|may have| B("Break-points")

figure: 

activity_preface: |
  - Install a scripting environment for your platform of choice.

activities:
  - ["Napari python script editor plugin", "script_env/activities/binarization_imagejgui.md", "markdown"]
  - ["Fiji script editor (IJ Macro, Groovy, Jython, ...)", "script_env/activities/binarization_imagejmacro.ijm", "java"]
  - ["IntelliJ for Groovy", "script_env/activities/binarization_jython.py", "python"]
  - ["Eclipse for Jython", "script_env/activities/binarization_matlab.m", "matlab"]

exercises:

assessment: >


learn_next:
  - "[Running an image analysis script](../script_run)"

external_links:
  - "[Using the Fiji script editor](https://imagej.net/scripting/script-editor)"
  - "[What is an IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)"
---

#### IDE

If you are writing a lot of code you should consider upgrading your current scripting environment to a full-fledged integrated development environment ([IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)).

=======
>>>>>>> External Changes
