---
title:     Setting up a scripting environment
layout:    module
tags: ["draft","scripting"]
prerequisites:

objectives:
  - "Set up a scripting environment for your platform"
motivation: |
  In order to run bioimage analysis scripts you need a platform where you can both run and develop those scripts. There is a range of solutions where especially the development of script ranges from a simple text editor to a full integrated development environment ([IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)).
  
concept_map: >
  graph TD
    S("Script") -->|contains| C("Code")
    E("Environment") -->|executes| C
    S("Script editor") -->|modifies| C
    S("Script editor") -->|may have| A("Auto-completion")
    S("Script editor") -->|may have| B("Break-points")

figure: /figures/script_env.png
figure_legend: Fiji script editor with auto-completion and <kbd>Run</kbd> button

activity_preface: |
  Install a scripting environment for your bioimage analysis platform.

activities:
  - ["Fiji script editor (IJ Macro, Groovy, Jython, ...)", "script_env/activities/script_editor_imagej.md", "markdown"]
  - ["Napari python script editor plugin", "script_env/activities/script_editor_plugin_napari.md", "markdown"]

exercises:

assessment: >

learn_next:
  - "[Running an image analysis script](../script_run)"

external_links:
  - "[Using the Fiji script editor](https://imagej.net/scripting/script-editor)"
  - "[What is an IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)"
---

