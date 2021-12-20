---
title:     Running a script (Draft)
layout:    module
prerequisites:
  - "[TODO: Setting up a scripting environment](../pixels)"
objectives:
  - "Understand that a script is a single text file that is written in a specific scripting language"
  - "Understand the basic building blocks of a script, i.e. what happens in each line"
  - "Run a bioimage analysis script"
  - "Modify a bioimage analysis script"

motivation: |
  Scripts are a very good and common way of sharing and publishing bioimage analysis workflows.
  It is thus very important to know how to run such scripts, e.g. when you find one in a publication or 
  when someone in your bioimage analysis support develops such a script for you.
  
concept_map: >
  graph TD
    S("Script") --> R("Run")
    S --> X("Share, Publish, Reproduce")
    R --> Y("With user interaction")
    R --> Z("Batch")
    S --> T("Text")
    T --> P("Programming language")
    P --> OFP("Objects, functions, parameters, comments, ...")

figure: /figures/script_run.png
figure_legend: Running a python script in the napari script editor plugin.

activity_preface: |
  - Download a bioimage analysis script
  - Open the script
  - Run the script
  - Discuss the typical content of a bioimage analysis script, such as:
    - Programming language
    - Includes
    - Comments
    - Functions
    - Parameters
    - Objects/Variables
  - Discuss particularities for your platform

activities:
  - ["ImageJ macro in Fiji script editor", "script_run/activities/script_run_fiji_imagej_macro.md", "markdown"]
  - ["Python script in napari console", "script_run/activities/script_run_napari_terminal.md", "markdown"]
  - ["Python script in napari script editor plugin", "script_run/activities/script_run_napari_script_editor.md", "markdown"]

exercises:

assessment: >

  ### True or False
    - Python is a scripting language. 
    - A comment is a line of code that will be executed.
    - You can run scripts in Excel and Word.
    - You can run scripts in Fiji.
    
    > ## Solution
    >   - **True**
    >   - **False** Comments are just for humans to read.
    >   - **True** Excel and Word in fact do have their own [scripting capabilities}(https://support.microsoft.com/en-us/office/introduction-to-office-scripts-in-excel-9fbe283d-adb8-4f13-a75b-a81c6baf163a)
    >   - **True**
    {: .solution}

learn_next:

external_links:
  - "[Scripting Fiji](https://imagej.net/scripting/)"
  - "[Scripting QuPath](https://qupath.readthedocs.io/en/stable/docs/scripting/overview.html)"
---

#### Image analysis platforms with scripting capabilities

- Fiji
- QuPath
- Napari

#### Script content

A script is a text file where each line is code that can be executed by the platform in which you are running the script. There are different types of content that a line can represent. Sometimes one line can even contain multiple of such contents.

##### Comments

It is good practice to add some human readable comments to explain what the code is doing.
This is achieved by starting the line with a special symbol, such as `#` or `//` or `/*`.
Note that a comment can be either a whole line in the script or also added behind an actual coding statement.

Examples:
- IJ-Macro: ...
- IJ-Groovy: ...
- Python: `# binarise the image`
- Python: `binary_image = image > 49 # binarise the image`


##### Import statements

In some cases one needs to tell the executing environment which libraries are needed to run the code. This is done via so-called import statements.

Examples:
- IJ-Macro: You don't need import statemts as everything is available by default.
- IJ-Groovy: ...
- Python: `import imageio`


##### Functions and parameter

Examples:
- IJ-Macro: `IJ.run(...)`
- Python: `viewer.add_image(image)`


##### Objects

Very often you want to store the results of some computation in an object. In most languages this is achieved by the `=` sign operator, where you assign the output of the computation on the right of the `=` sign to the object on the left.

Examples:
- IJ-Macro: ???
- Python: `binary_image = threshold(image, 10)`
