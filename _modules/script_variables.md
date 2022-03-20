---
title:     Variables
layout:    module
tags: ["scripting", "draft"]
prerequisites:
 - "[Running a script](../script_run)"
objectives:
  - "Understand difference between variable name, value, type, and storage"
  - "How to use variables in functions"
motivation: |
  A variable is an essential concept in programming, it allows to structure and generalize a script/program.
  A variable stores in memory a value, e.g. a numeric or string value, that can be used and changed at several occasions in 
  a script. 
  
concept_map: >
  graph TD
    V("Variable") --> |has|Name("Symbolic name")
    V --> |has|Type("Type")
    
    V --> |has|Value("Value")
    V --> |is| Stored("Stored in memory")
    Value --> |can| Change
    Type --> |can| Change

figure: /figures/script_variables.png
figure_legend: Variables are containers specific for an information type. Variable names do not contain spaces, should explain their purpose, should be consistent throughout your code, and should adhere to a naming convention. 

activity_preface: |
  Use a script editor for all these activities.
  ### General usage of variables
  - Show how variables need to be assigned/declared before usage
  - Create two numeric variables and store results of addition in a new variable
  - Use a numeric variable in a simple function (e.g. print(variable)) and in an image processing function
  
  ### String variables
  - Show an example of a string variable and how to declare it
  
  ### Variable type
  - Discuss variable type and, for some languages, type declaration
  - Discuss possibility of type mismatch
  
activities:
  - ["ImageJ Macro, general usage", "script_variables/activities/script_variables_general_imagejmacro.ijm"]
  - ["ImageJ Macro, strings", "script_variables/activities/script_variables_strings_imagejmacro.ijm"]
  - ["ImageJ Macro, type", "script_variables/activities/script_variables_type_imagejmacro.ijm"]
  - ["ImageJ Groovy, type", "script_variables/activities/script_variables_type.groovy"]
    
    
exercise_preface: |
   ### Difference of Gaussians
   The code performs two gaussian blurs of an image with fixed sigma. The code then computes the difference of the two filtered images. 
   1. Modify the code and replace the hard-coded sigma value of the gaussian blur with 2 variables, 
   `sigma1` and `sigma2` respectively
   2. Make `sigma2` three times larger than `sigma1` and run again the code
   
   ### Fix it
   
   Try to run the code and fix the error(s). Modify the variable names to `camelCase` in a way that they their function is clear to the reader. 

exercises:
  - ["ImageJ Macro, difference of gaussians", "script_variables/exercises/script_variables_DoG_imagejmacro.md"]
  - ["ImageJ Macro, fix it", "script_variables/exercises/script_variables_fixit_imagejmacro.md"]


assessment: >
  
  ### True or False
    - A variable can only be a number
    - Variables have a symbolic name that can be referenced to
    - The value of a variable can't change
    - The name of the variable should indicate its function
    
    > ## Solution
    >   -  False
    >   -  True
    >   -  False
    >   -  True
    {: .solution}

learn_next:
    - "[Working with strings](../string_concat)"

external_links:

 
---
 
