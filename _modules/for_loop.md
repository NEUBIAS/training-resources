---
title:     For Loops
layout:    module
prerequisites: 
  - "ROIs"
[comment]: <> ( - NEEDS TO BE ADDED "[ROIs](../)")

objectives:
  - "Repeating operations multiple times"
  - "Running a script for multiple files"
motivation: |
  Often you need to repeat operations multiple times or run the script for multiple images. One example is when you want to repeat applying a similar filter on the same image, to find the best radius value of that filter. In such cases you can simplify the code by creating a loop instead of writing the same lines of code multiple times. Loops are also very useful for batch processing, which you will learn later.

  
concept_map: >
  graph TD
    A("Substring 1") --> X("Concatenated string")
    B("Substring 2") --> X
    C(Number 1) --> X
    D("...") --> X
    E("Substring n") --> X

figure: /figures/string_concat.png
figure_legend: String concatenation.

activity_preface: |
  - Open a script editor.
  - Define three variables with values "Hello ", "user number " and 50.
  - Concatenate the three variables.

activities:
  - ["ImageJ Macro", "string_concat/activities/string_concat.ijm", "java"]
  - ["ImageJ Jython", "string_concat/activities/string_concat.py", "python"]

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
[comment]: <> ( - NEEDS TO BE ADDED "[Batch processing](../)")

external_links:
  - "[ImageJ macro loops](https://imagej.nih.gov/ij/developer/macro/macros.html#loops)"
  - "[Image processing with python, search for loop keyword to see examples](https://datacarpentry.org/image-processing/aio/index.html)"
  
---
#### String concatenation
You concatenate strings by using specific operators, depending on the programming platform. Fo example, the + operator. Let's look at a few examples:

`"Channel_"+1` -> `"Channel_1"`

`"image_"+"duplicate"` -> `"image_duplicate"`
 

