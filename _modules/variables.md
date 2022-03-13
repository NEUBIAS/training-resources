---
title:     Variables
layout:    module
tags: ["scripting", "Draft"]
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

figure: /figures/variables.png
figure_legend: Variables are containers specific for an information type. The name of the variable should explain its purpose. Naming convention is camelCase (left side) or under_score (right side).

activity_preface: |
  - Open a script editor, create two numeric variables, store results of addition in a new variable.
  - Show how a variable can be used in a simple function (e.g. print(variable)) and in a image processing function.
  
activities:
  - ["ImageJ Macro", "variables/activities/variables_imagejmacro.ijm", "java"]

exercises:
  - ["ImageJ Macro", "variables/exercises/variables_imagejmacro.md"]

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
 
