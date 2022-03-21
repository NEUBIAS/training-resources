---
title:     Loops
layout:    module
tags: ["scripting", "draft"]
objectives:
  - "Use for loops to repeat operations multiple times"
  - "Running a script for multiple files"
  
motivation: |
  In imaging processing workflow you often apply the same operation to several images, several labels, etc. In order to avoid repeating the same code several times we can use control flow statements such as a `for` loop. The `for` loop together with `if` clauses represent extremely useful tools when  programming. 

  
concept_map: >
  graph TD
    A["Previous code"] --> Loop{"Check condition"}
    Loop --> |Condition is valid| RepeatChunk("Code chunk to be repeated")
    RepeatChunk --> Loop
    Loop --> |Condition is not valid| NextChunk("Next code to run")


figure: /figures/for_loop.png
figure_legend: In a control flow statement a piece of code is repeated (loop) as long as a specific condition is valid. 


activity_preface: |
  - Open a script editor.
  - Print "Starting the process"
  - For images 1 to 10 print: "processing image number:" and the image number.
  - Print "Process completed"

activities:
  - ["ImageJ Macro", "script_for_loop/activities/script_for_loop.ijm"]

exercises:

  - ["ImageJ Macro", "string_concat/exercises/string_concat_imagejmacro.md"]

assessment: >

  ### Fill in the blanks

    - "Nuclei"+1+2 concatenation results in ___ string.
    - "Nuclei"+"1"+2 concatenation results in ___ string.
    
    > ## Solution
    >   - "Nuclei"+1+2 concatenation results in **"Nuclei3"** string.
    >   - "Nuclei"+"1"+2 concatenation results in **"Nuclei12"** string.
    {: .solution}
    

learn_next:

external_links:
  - "[ImageJ macro loops](https://imagej.nih.gov/ij/developer/macro/macros.html#loops)"
  - "[Image processing with python, search for loop keyword to see examples](https://datacarpentry.org/image-processing/aio/index.html)"
  
---
#### For loop
A `for` loop occurs by iterating over a loop variable defined in a loop header. You use `for` loops when you know the number of iterations to execute.


#### While loop
As a `for` loop a `while` loop repeats 

