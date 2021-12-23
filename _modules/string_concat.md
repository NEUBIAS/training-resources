---
title:     String concatenation
layout:    module
prerequisites: 
  - "[Variables](../variables)"
[comment]: <> (  - NEEDS TO BE ADDED "[Variables](../)")

objectives:
  - "Concatenate strings"
  - "Convert numbers into strings"
motivation: |
  String is a type of variable that can cotain a combination of characters. 
  String concatenation is the operation of joining multiple substrings together to make a bigger one. 
  For example concatenating "Hello " and "world!" would result into "Hello world!". 
  You can also combine a string and a number. For example concatenating the string "Displaying image ", number 50 and " out of 100" would result into "Displaying image 50 out of 100". Furthermore, you may concatenate strings to create paths to the images by concatenating path to the folder and file names.
  
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
[comment]: <> ( - NEEDS TO BE ADDED "[Saving tables, images, ROIs](../)")

external_links:
  - "[Wikipedia: String concatenation operator in different languages](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(strings))"
  
---
#### String concatenation
You concatenate strings by using specific operators, depending on the programming platform. Fo example, the + operator. Let's look at a few examples:

`"Channel_"+1` -> `"Channel_1"`

`"image_"+"duplicate"` -> `"image_duplicate"`
 

