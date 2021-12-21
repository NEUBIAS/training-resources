---
title:     Variables
layout:    module
prerequisites:
 - [TODO add links]
objectives:
  - "Explain concept of variable"
  - "Run minimal example of computation using a variable"
motivation: |
  A variable is an essential concept in programming, it allows to structure and generalize a script/program.
  A variable stores a value, e.g. a numeric or string value, that can be used and changed at several occasions in 
  a script. 
  
  
concept_map: >
  graph TD
    V("Variable") --> |has|Name("Symbolic Name")
    V --> |has|Type("Type")
    V --> |has|Value("Value")
    V --> |is| Stored("Stored in memory")
    Value --> |can| Change

figure: /figures/variables.png
figure_legend: Variables are containers specific for an information type. The name of the variable should explain its purpose. Naming convention is CamelCase (left side) or underscore (right side).

activity_preface: |
  - Open a script editor, create variables, add those,
  - Show how a variable can be used in a simple function (e.g. print(variable)) and in a image processing function.
  
activities:
  - ["ImageJ Macro", "variables/activities/variables_imagejmacro.ijm", "java"]

exercises:
  - ["ImageJ Macro", "variables/exercises/variables_imagejmacro.md"]

assessment: >
  
  ### True or False
    - A variable can only be a number
    - Variables have a symbolic name that can be referenced to
    - The value of a variable can not change
    - The name of the variable should indicate its function
    
    > ## Solution
    >   -  False
    >   -  True
    >   -  False
    >   -  True
    {: .solution}

learn_next:
  - ""

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Variable_(computer_science)"
 
---
 