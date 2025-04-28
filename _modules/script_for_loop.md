---
title:     Loops
layout:    module
tags: ["scripting"]
prerequisites:
  - "[Variables](../script_variables)"
objectives:
  - "Use for loops to repeat operations multiple times"
  - "Running a script for multiple files"
  
motivation: |
  In an imaging processing workflow you often apply the same operation to several images, several labels, etc. In order to avoid repeating the same code many times we can use control flow statements such as a `for` loop. Loops together with `if` clauses represent extremely useful tools when programming. 

  
concept_map: >
  graph TD
    A["Previous code"] --> Loop{"Check condition"}
    Loop --> |Condition is valid| RepeatChunk("Code chunk to be repeated")
    RepeatChunk --> Loop
    Loop --> |Condition is not valid| NextChunk("Next code to run")


figure: /figures/for_loop.png
figure_legend: In a control flow statement a piece of code is repeated (loop) as long as a specific condition is valid. 



multiactivities: 
 - ["script_for_loop/script_for_loop_act1.md", [["ImageJ Macro, loop structure", "script_for_loop/activities/script_for_loop_loopstructure.ijm"], ["ImageJ Macro, example no loop",  "script_for_loop/activities/script_for_loop_measure_distances_noloop.ijm"], ["ImageJ Macro, example with loop", "script_for_loop/activities/script_for_loop_measure_distances_withloop.ijm"], ["Python, for loop",  "script_for_loop/script_for_loop_python.py"], 
 ["Python, advanced for loop",   "script_for_loop/script_advanced_for_loop.py"]]]
 - ["script_for_loop/script_for_loop_act2.md",[["ImageJ Macro, Multiple erosion", "script_for_loop/exercises/script_for_loop_erodeband.md"]]]
    

assessment: |
    ### Tracking changes in a Loop
    You have the following Python code snippet
      ```python
      numbers = [10, 5, 20, 15]
      total = 0
      for num in numbers:
          if num > 10:
              total = total + num
      print(total)
      ```
      What is the final value of the variable total after this code is executed? 
      a) 0, b) 15, c) 35, d) 50
      > ## Solution
      > The correct answer is c) 35
      {: .solution}

    ### Conditional Logic in a Loop

    Examine the following ImageJ macro snippet:

      ```
      threshold = 100;
      pixelValue = 120;

      if (pixelValue > threshold) {
        print("Pixel is above threshold");
      } else {
        print("Pixel is at or below threshold");
      }
      ```
      What will be printed to the ImageJ Log window when this code is executed?
      a) Pixel is above threshold, b) Pixel is at or below threshold, c) Nothing will be printed, d) An error will occur
      
      > ## Solution
      > The correct answer is a)
      {: .solution}
learn_next:
  - "[String and paths](../string_concat)"
  - "[Functions](../script_functions)"
  - "[Batch processing](../batch_processing)"


external_links:
  - "[ImageJ macro loops](https://imagej.nih.gov/ij/developer/macro/macros.html#loops)"
  - "[Image processing with python, search for loop keyword to see examples](https://datacarpentry.org/image-processing/aio/index.html)"
  
---
#### For loop
A `for` loop occurs by iterating over a loop variable defined in a loop header. You use `for` loops when you know the number of iterations to execute.

Example `for` loop in ImageJ-macro language:
```java
// i is the variable over which it is itarated, i++ is a short cut for i = i + 1
for (i = 0; i <10; i++) { // loop header
  print(i)
  //Eventually more code
}
```

Example `for` loop in python, note that you can iterate over any type of list:
```python
my_fruits = ["apple", "banana", "cherry"]
for fruit in my_fruits:
  print(fruit)
  # more code
```


#### While loop
While loop does not have a fixed number of iterations. Typically the header contains a condition, the loop continues as long as the condition is true.  In the body of the loop something is computed that may change the condition. 

Example `while` loop in ImageJ-macro:

```java
counter = 0;
nax_count = 5;
while (counter < max_count) {
  print(counter)
  counter = counter + 1
}
```

Example `while` loop in python:

```python 
counter = 5
while counter > 0:
  print(counter)
  counter = counter - 1 
  # More code
print("End of while loop")
```

#### If/Else conditional expressions
This is not a loop, but a condition for which some code is executed. `if` a condition is true, then do this, `else` (i.e. condition is not true) then do that.

Example `if/else` in python:
```python
condition = True

if condition:
    result = 10
    print("condition is True")
else:
    result  = 20
    print("condition is False")

print(result)
```
