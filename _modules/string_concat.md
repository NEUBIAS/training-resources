---
title: String concatenation
layout: module
tags: ["scripting","draft"]
prerequisites: 
  - "[Variables](../variables)"

objectives:
  - "Concatenate strings"
  - "Convert numbers into strings"
motivation: |
  String is a type of variable that can cotain a combination of characters. 
  String concatenation is the operation of joining multiple substrings together to make a bigger one. 
  For example concatenating "Hello " and "world!" would result into "Hello world!". 
  You can also combine a string and a number. For example concatenating the string "Displaying image ", number 50 and " out of 100" would result into "Displaying image 50 out of 100". Furthermore, you may concatenate strings to create paths to the images by concatenating path to the folder and file names. 
  Please note that when concatenating file path and file name you might need to also concatenate a file separator such as / or \ between file path and dile name. Depending on the operating system and the programming language this file separator can be different. In the external links, you will find a generic way of adding a file separator in imageJ as an example.
  
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
  - ["ImageJ Macro: Concatenate variables", "string_concat/exercises/string_concat_imagejmacro.md"]
  - ["ImageJ Macro: Concatenate gaussian sigma values", "string_concat/exercises/string_concat_imagejmacro2.md"]
  - ["ImageJ Macro: Concatenate paths", "string_concat/exercises/string_concat_imagejmacro3.md"]

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
  - "[File.separator function in imageJ](https://imagej.nih.gov/ij/developer/macro/functions.html#F)"
  
---
#### String concatenation
You concatenate strings by using specific operators, depending on the programming platform. Fo example, the + operator. Let's look at a few examples:

`"Channel_"+1` -> `"Channel_1"`

`"image_"+"duplicate"` -> `"image_duplicate"`
 

