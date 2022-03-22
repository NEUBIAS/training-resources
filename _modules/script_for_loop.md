---
title:     Loops
layout:    module
tags: ["scripting", "draft"]
objectives:
  - "Use for loops to repeat operations multiple times"
  - "Running a script for multiple files"
  
motivation: |
  In an imaging processing workflow you often apply the same operation to several images, several labels, etc. In order to avoid repeating the same code many times we can use control flow statements such as a `for` loop. Loops together with `if` clauses represent extremely useful tools when programming. 

  
concept_map: >
  graph TD
    A["Previous code"] --> Loop{"Check condition"}
    Loop --> |Condition is valid| RepeatChunk("Code chunk to be repeated")
    RepeatChunk --> Loop
    Loop --> |Condition is not valid| NextChunk("Next code to run")


figure: /figures/for_loop.png
figure_legend: In a control flow statement a piece of code is repeated (loop) as long as a specific condition is valid. 


activity_preface: |
  ### For loop basics
  - Open a script editor.
  - Open and run a script that contains several repeated operations and explain that you would like to write this part of code in a more simple way. 
  - Explain the different elements of a numeric `for` loop:
    - The loop header, the loop counter/variable, and body
    - The initial and end condition
    - How the counter is iterated (e.g. `i++`).
  - Using a print command show how the iterator changes
  - Take the starting script and modify it using a `for` loop

activities:
- ["ImageJ Macro, loop structure", "script_for_loop/activities/script_for_loop_loopstructure.ijm"]
- ["ImageJ Macro, example no loop", "script_for_loop/activities/script_for_loop_measure_distances_noloop.ijm"]
- ["ImageJ Macro, example with loop", "script_for_loop/activities/script_for_loop_measure_distances_withloop.ijm"]
    
exercise_preface: |
 ### Multiple erosion
  * Open the binary image [xy_8bit_binary__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__nup_nuclei/xy_8bit_binary__nuclei.tif")
  * Create a macro (or use a pre-defined one)  to erode and find boundary of the binary object
  * Modify the macro so that you can perform an arbitrary number of erosions and find their boundary
exercises:
- ["ImageJ Macro, Multiple erosion", "script_for_loop/exercises/script_for_loop_erodeband.md"]

assessment: >


    

learn_next:

external_links:
  - "[ImageJ macro loops](https://imagej.nih.gov/ij/developer/macro/macros.html#loops)"
  - "[Image processing with python, search for loop keyword to see examples](https://datacarpentry.org/image-processing/aio/index.html)"
  
---
#### For loop
A `for` loop occurs by iterating over a loop variable defined in a loop header. You use `for` loops when you know the number of iterations to execute.


#### While loop
As a `for` loop a `while` loop repeats 

