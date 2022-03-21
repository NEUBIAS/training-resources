---
title: Running a script
layout: module
tags: ["scripting"]
prerequisites:
objectives:
  - "Understand that a script is a single text file that is written in a specific scripting language"
  - "Understand the basic building blocks of a script, i.e. what happens in each line"
  - "Run a bioimage analysis script"
  - "Modify a bioimage analysis script"

motivation: |
  Scripts are a very good and common way of sharing and publishing bioimage analysis workflows. It is thus very important to know how to run such scripts, e.g. when you find one in a publication or when someone in your bioimage analysis support develops such a script for you. Many of the common bioimage analysis platforms support scripting, e.g. Fiji, QuPath, napari.
  
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
  - Do some slight modification, e.g. changing some processing parameter, and run the script again

activities:
  - ["ImageJ Macro in Fiji", "script_run/activities/script_run_fiji_imagej_macro.md", "markdown"]
  - ["(Draft) Python script in napari console", "script_run/activities/script_run_napari_terminal.md", "markdown"]
  - ["(Draft) Python script in napari script editor plugin", "script_run/activities/script_run_napari_script_editor.md", "markdown"]
exercises:
  - ["ImageJ Macro in Fiji", "script_run/exercises/script_run_fiji_imagej_macro.md"]

assessment: >

  ### True or False
    1. Python is a scripting language.
    1. Anaconda is a scripting language.
    1. A comment is a line of code that will be executed.
    1. You can run scripts in Excel and Word.
    1. You can run Python scripts in Fiji.
    
    > ## Solution
    >   1. **True.** In fact, python has very powerful image analysis capabilities.
    >   1. **False.** Anaconda is something that will help you with dependency management (e.g., of the things you need to run a script).
    >   1. **False.** Comments are just for humans to read.
    >   1. **True.** Excel and Word in fact do have their own [scripting capabilities](https://support.microsoft.com/en-us/office/introduction-to-office-scripts-in-excel-9fbe283d-adb8-4f13-a75b-a81c6baf163a)
    >   1. **True** and also **False.** In fact, you can run Jython scripts in Fiji. Jython is a scripting language that looks like python but it actually runs Java code.
    {: .solution}

learn_next:
  - "[Script recording](../script_record)"
  - "[Using variables](../script_variables)"

external_links:
  - "[ImageJ Macro Functions](https://imagej.nih.gov/ij/developer/macro/functions.html)"
  - "[Scripting Fiji](https://imagej.net/scripting/)"
  - "[Scripting QuPath](https://qupath.readthedocs.io/en/stable/docs/scripting/overview.html)"
---

#### Programming script content

A programming script is a text file where each line is code that can be executed by the platform (the compiler) in which you are running the script. There are different types of content that a line can represent. Sometimes one line can even contain multiple of such contents. In the following sections some of the very common types of content are very briefly discussed (check out the follow-up modules for much more details).

##### Comments

It is good practice to add some human readable comments to explain what the code is doing. To tell the compiler that a part of a script is a comment, one prepends the comment section special symbol, such as `//` or `#`.

Examples:
- ImageJ-Macro, Java, Groovy: `// binarise image`
- Python: `# binarise image`
- Python: `binary_image = image > 49 # binarise image`
  - In this example the comment is on the same line as the actual code

##### Import statements

In some cases one needs to tell the executing environment which libraries are needed to run the code. This is done via so-called import statements.

Examples:
- Groovy: `import ij.plugin.Scaler`
- Python: `from os import open`

##### Functions and parameter

Functions are the heart of a program, they do stuff, depending on the paramteres that you give.

Examples:
- IJ-Macro: `run("Duplicate...", "title=duplicateImage");`
- Python: `viewer.add_image(image)`

##### Variables

Very often you want to store the results of some computation. In most languages this is achieved by the `=` sign operator, where you assign the right of the `=` sign to the varaible on the left.

Examples:
- IJ-Macro: `lengthOfString = getStringWidth("hello world");`
- Python: `binary_image = threshold(image, 10)`
