---
title: Running a script
layout: module
tags: ["scripting","draft"]
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
  Many of the common bioimage analysis platforms support scripting, e.g. Fiji, QuPath, napari.
  
concept_map: >
  graph TD
    S("Script") --> R("Run")
    S --> X("Share, Publish, Reproduce")
    R --> Z("Batch")
    S --> T("Text")
    T --> P("Programming language")
    P --> OFP("Variables, functions, parameters, comments, ...")

figure: /figures/script_run.png
figure_legend: Running a python script in the napari script editor plugin.

activity_preface: |
  - Open a bioimage analysis script
  - Run the script
  - Briefly discuss the typical building blocks of programming script, such as:
    - Include statements
    - Comments
    - Functions
    - Parameters
    - Objects/Variables
  - You may discuss particularities for your platform

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

#### Programming ccript content

A programming script is a text file where each line is code that can be executed by the platform (the compiler) in which you are running the script. There are different types of content that a line can represent. Sometimes one line can even contain multiple of such contents. In the following sections some of the very common types of content are briefly discussed.

##### Comments

It is good practice to add some human readable comments to explain what the code is doing. To tell the compiler that a part of a script is a comment, one prepends the comment section special symbol, such as `//` or `#`.

Examples:
- IJ-Macro: `// binarise image`
- IJ-Groovy: `// binarise image`
- Python: `# binarise image`
- Python: `binary_image = image > 49 # binarise image`
  - In this example the comment is on the same line as the actual code

Learn more in module TODO.

##### Import statements

In some cases one needs to tell the executing environment which libraries are needed to run the code. This is done via so-called import statements.

Examples:
- IJ-Macro: N/A
- IJ-Groovy: `import ij.plugin.Scaler`
- Python: `from os import open`

Learn more in module TODO.

##### Functions and parameter

Examples:
- IJ-Macro: `IJ.run(...)`
- Python: `viewer.add_image(image)`

Learn more in module TODO.

##### Variables

Very often you want to store the results of some computation. In most languages this is achieved by the `=` sign operator, where you assign the right of the `=` sign to the varaible on the left.

Examples:
- IJ-Macro: `lengthOfString = getStringWidth("hello world");`
- Python: `binary_image = threshold(image, 10)`

Learn more in module TODO.