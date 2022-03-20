---
title:     Variables
layout:    module
tags: ["scripting", "draft"]
prerequisites:
 - "[Running a script](../script_run)"
objectives:
  - "Variables name, value, type, and storage"
  - "How to use variables in functions"
motivation: |
  A variable is an essential concept in programming, it allows to structure and generalize a script/program.
  A variable stores a value, e.g. a numeric or string value, that can be used and changed at several occasions in 
  a script. 
  
concept_map: >
  graph TD
    V("Variable") --> |has|Name("Symbolic name")
    V --> |has|Type("Type")
    V --> |has|Value("Value")
    V --> |is| Stored("Stored in memory")
    Value --> |can| Change

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
  - ["ImageJ Macro", "script_variables/activities/script_variables_imagejmacro.ijm", "java"]

exercises_preface: 
exercises:
  - ["ImageJ Macro", "script_variables/exercises/script_variables_imagejmacro.md"]

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

external_links:

 
---
 
