---
title: String concatenation
layout: module
tags: ["scripting"]
prerequisites: 
  - "[Variables](../variables)"

objectives:
  - "Combine (concatenate) strings, paths and numbers into a bigger string"
motivation: |
  Combining several strings into a larger string is a prevalent operation in scripting. This is useful, e.g., to create file paths and create log messages. Such concatenation of strings is surprisingly error prone and it is thus important to learn it properly and be aware of all the pitfalls.

concept_map: >
  graph TD
    A("String 1") --> X("Concatenated string")
    B("String 2") --> X
    C("...") --> X
    D("String N") --> X

figure: /figures/string_concat.png
figure_legend: String concatenation.

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

#### String concatenation

String concatenation is the operation of joining multiple substrings together to make a bigger one. For example concatenating "Hello " and "world!" would result into "Hello world!". 

#### Creating paths

A frequent operation in bioimage analysis is to create paths to images by concatenating a folder and file name to a full path. Please note that when concatenating a folder and a file name into a full path, you might need to add a so-called file separator between the folder and the file name. This is a character that separates directory names within a path to a particular location on your computer. Different operating systems use different file separators: on Linux and MacOS, this is `/`, while Windows uses `\`. To make it worse, when you store a directory you are typically never sure whether the contained string ends on `/` or `\` or does not have the separator in the end, e.g. `C:\Users\Data`, in which case you have to add it when concatenating a file name). To make it even worse, in some programming langauges the `\` character have a special meaning within strings and is thus not simply interpreted as a character and to actually get a backslash you may have to write `\\`.

If you want to have some "fun" you can read those discussions:
- [forward slash in java](https://stackoverflow.com/questions/9575116/forward-slash-in-java-regex)
- [string replace a backslash in java](https://stackoverflow.com/questions/5596458/string-replace-a-backslash)

As all of this can quickly become a huge mess, fortunately, scripting languages typically offer special functions to help you write code to create file paths that will run on all operating systems. 
