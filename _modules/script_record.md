---
title: Recording a script
layout: module
tags: ["scripting"]

prerequisites:
  - "[Running a script](../script_run)"

objectives:
  - "Record graphical user interface (GUI) actions into a script"

motivation: |
  Writing an image analysis script from scratch is difficult because you need to remember all the commands needed to execute all the required actions. However, luckily some software packages have an option to record what you do in the graphical user interface into a script. This is very powerful and good to know!   

concept_map: >
  graph TD
    G("Graphical user interface") --> A("Image analysis action")
    G -->|generates| E("Executable code (text)")
    E -->|executes| A  

figure: /figures/script_record.png
figure_legend: Concept of script recording.

activity_preface: |
  - In FIJI, enable the script recorder.
  - Open the image [xy_8bit__small_noisy_nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__small_noisy_nuclei.tif).
  - Duplicate the image
  - Perform a gaussian blur operation on the duplicated image
  - Inspect (and clean up) the recorded script
  - Run the script

activities:
  - ["ImageJ", "script_record/activities/script_record_imagejgui.md", "markdown"]

exercises:
  - ["ImageJ", "script_record/exercises/script_record_imagejgui.md"]

assessment: >
  ### Q&A

    - How could one publish an image analysis workflow that you did in a software that only has a graphical user interface?
    - How could one share an image analysis script with a colleague?

    > ## Solution
    >   - One could record a screencast.
    >   - One could send the script by e-mail.
    {: .solution}

learn_next:
  - "[Using variables](../variables)"

external_links:
  - "[ImageJ macro recorder](https://imagej.net/scripting/macro#the-recorder)"
---
