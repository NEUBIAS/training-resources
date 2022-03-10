---
title: Commenting
layout: module
tags: ["scripting","draft"]
prerequisites:
  - "[Binarization](../binarization)"
  - "[Connected component labeling](../connected_components)"
objectives:
  - "Understand the concept and purpose of commenting."
  - "Comment properly what certain section of code."
motivation: |
  When you read your code again in six months from now, you want to understand what your code does, and why. Also if you would pass your code to another person, for them to use, modify, and/or extend it. For this, you can add **comments** to your code, i.e. text which can be read by human, and is ignored by computer when it executes your code.
  In addition, you can use comment to skip certain part of the code. For example, when you wrote testing code and later no longer need those.
  
concept_map: >
  graph TD
    ST("script text") --> CD("code")
    ST("script text") --> CM("comment")
    CD -->|read by| RC("computer")
    CM -->|read by| RH("human")
    CM -->|ignored by| RC("computer")

figure: /figures/code_comment.png
figure_legend: Single line comment, and multiple line (block) comment.

activity_preface: |
  - Expand the activity for different platforms.
  - Identify comment part or where it's missing, and use that to understand the code.
  - Try to run the codes and see if it does what you expected. If necessary, add proper comment to further explain what certain part of code does.

activities:
  - ["MATLAB", "commenting/activities/binarization_matlab.m", "matlab"]
  - ["Python", "commenting/activities/binarization.py", "python"]

exercises:

assessment:

learn_next:

external_links:

---
