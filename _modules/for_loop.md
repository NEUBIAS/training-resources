---
title:     For Loops
layout:    module
prerequisites: 
  - "ROIs"
  - "Input and output files"
[comment]: <> ( - NEEDS TO BE ADDED "[ROIs](../)")

objectives:
  - "Repeating operations multiple times"
  - "Running a script for multiple files"
motivation: |
  Often you need to repeat operations multiple times or run the script for multiple images. One example is when you want to repeat applying a similar filter on the same image, to find the best radius value of that filter. In such cases you can simplify the code by creating a loop instead of writing the same lines of code multiple times. Loops are also very useful for batch processing, which you will learn later.

  
concept_map: >
  graph TD
    A("Previous code") --> B("For loop with a counter and a maximum")
    B --> C("Statements to be repeated")
    C --> D("Counter = Counter+1")
    D --> E("Counter < maximum")
    E --> B
    D --> F("Counter >= maximum")
    F --> G("Next code to run")


figure: /figures/for_loop.png
figure_legend: For loop.

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
#### For loop
Loops are used for repeating a set of operations multiple times, for example on multiple images, multiple channels or multiple timepoints or Z-slices. 


