---
title: Working with strings
layout: module
tags: ["scripting"]
prerequisites: 
  - "[Variables](../variables)"

objectives:
  - "Construct complex strings, e.g. to produce log messages and create file paths"

motivation: |
  Combing several strings into a a larger string is a prevalent operation in scripting. This is useful, e.g., to create file paths and create log messages. Such concatenation of strings is surprisingly error prone and it is thus important to learn it properly and be aware of all the pitfalls.

concept_map: >

figure: /figures/string_concat.png
figure_legend: Examples of somewhat advanced string expressions (as it they may roughly look in some hypothetical scripting language).

activity_preface: |
  - Open a script editor.
  - Define three variables with values `"Analyzing image"`, `11` and `"..."`.
  - Concatenate the three variables to create the string: `"Analyzing image 11..."`.

activities:
  - ["ImageJ Macro", "string_concat/activities/string_concat.ijm", "java"]

exercises:
  - ["ImageJ Macro: Concatenate variables", "string_concat/exercises/string_concat_imagejmacro.md"]
  - ["ImageJ Macro: Create function arguments", "string_concat/exercises/string_concat_imagejmacro2.md"]
  - ["ImageJ Macro: Create paths", "string_concat/exercises/string_concat_imagejmacro3.md"]

assessment: >

  ### Fill in the blanks

    1. In MacOS and Linux sub-folders are separated by the `___` string, whereas on Windows they are separated by the `___` string.
    1. Concatenating `"Hello"` and `"world"` one obtains `___`.
    1. Concatenation the variables `folder = "/Users/Images"` and `file = "MyImage.tif"` one obtains `___`.

    > ## Solution
    >   1. MacOs `"/"`, Windows `"\"`
    >   1. One would get `"Helloworld"`; to fix this one needs to add a third `" "` string in the middle to get `"Hello world"`. 
    >   1. One would obetain `"/Users/ImagesMyImage.tif"`. There are several ways to fix this, depending on the scripting language. A good way is to use functions such as, e.g., `os.path.join( folder, file )` in python, because this will work for both cases: `folder = "/Users/Images"` and `folder = "/Users/Images/"`.
    {: .solution}
    

learn_next:

external_links:
  - "[Wikipedia: String concatenation operator in different languages](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(strings))"
  - "[File.separator in ImageJ](https://imagej.nih.gov/ij/developer/macro/functions.html#F)"
  
---
#### Strings

Strings are objects (variables) containing a sequence of characters such as "a" and "b".

#### String concatenation

String concatenation is the operation of joining multiple substrings together to make a bigger one. For example concatenating "Hello " and "world!" would result into "Hello world!". 

A frequent operation in bioimage analysis is to create paths to images by concatenating a folder and file name to a full path. Please note that when concatenating a folder and a file name you might need to add a "/" or "\" between the folder and the file name. Which of the two depends on the operating system and and thus all scripting languages offer special functions to help you write code that will run on all operating systems.
