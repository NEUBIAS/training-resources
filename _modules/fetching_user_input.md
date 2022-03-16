---
title: Fetching user input (script parameters)
layout: module
tags: ["scripting"]
prerequisites:
  - "[Running a script](../script_run)"
  - "[Setting a scripting environment](../script_env)"
objectives:
  - "To create graphical user interface/ dialog box for fetching inputs through script"
  - "Understand how and which parameters can be fetched through graphical user interface"

motivation: |
  Sometimes when your script has lot of input parameters and you want to apply steps related to these input parameters with different values/settings, changing them within a script with each run makes your script more error-prone. Moreover, when steps to be performed on your data are not sequential, one can reduce the manual intervention steps by creating a custom GUI or dialog box with all the predefined parameters at the beginning of a script run. Script parameter notation is a very efficient way to declare all your input parameters through a dialog.

concept_map: >
  graph TD
    P("#@ parameter") -- declares user inputs --> S("Script")
    P("#@ parameter") -- has --> T("Type")
    T("Type") -- has --> PP("Properties")
    S --> G("Pop-up dialog (to fetch inputs interactively)")

figure: /figures/fetching_user_input.png
figure_legend: Fetching user parameters in a script using notation "#@ parameter". Running this script would produce a pop-up dialog shown in the figure. The variables for storing these inputs are defined at the end of each "#@ parameter" declaration. Pressing "OK" will store set values in variable which are used in the rest of the code.

activity_preface: |
  - Create series of macro steps using input parameters written in macro  
    - try try bitte

activities:
  - ["ImageJ GUI", "fetching_user_input/activities/createImage.ijm", "java"]

exercise_preface: |
  - Create input parameters from the steps written in macro
    - Open

exercises:
  - ["ImageJ GUI", "fetching_user_input/activities/createImage.ijm", "java"]

assessment: >

  ### True or False
    - `#@ Parameter` ensures that the correct value is entered in the dialog box
    - Default parameter values in the dialog box are never overwritten

    > ## Solution
    >   - **False** You can even enter characters for integer type but it will eventually throw an error
    >   - **False** Persisted value will overwrite default values
    {: .solution}

learn_next:

external_links:
- Read more about [script parameters](https://imagej.net/scripting/parameters)

---

### Syntax
- Template - `#@ Type (property1, property2,...) variableName`
- Example - `#@ Integer (label="Number", value=2) inputNumber`

### Parameter types/styles
- `Boolean, Byte, Short, Long, Integer, Float, Double, Character, String, File` etc.
- Checkbox, numeric field (slider, spinner, scroll bar), text field, file chooser (file, directory, open, save, extensions) etc.

### Parameter properties
- Widget label
  - Add label names to widgets
  - Usage - `label="Enter label name here"`
- Widget mouseover
  - Description of widgets when hovering over them
  - Usage - `description="This widget shows label name"`
- Default values
  - Usage - `value=15`
- Persistence
  - Decides if the values from previous run should appear
  - It will overwrite the default value
  - Usage - `persist=false`
- Visibility
  - Lets you decide if parameter should be:
    - Displayed
    - Editable and/or
    - Recordable
  - See [script parameters](https://imagej.net/scripting/parameters) for usage
- Multiple choices
  - Option selection using dropdown and radio buttons
  - Usage - `choices={"Option1", "Option2"}, style="listBox"`
  - Usage - `choices={"Option1", "Option2"}, style="radioButtonHorizontal"`
- Files and folders
  - Selects single/multiple files and folders
  - only file usage
    - Single - `#@ File (label="Select a file", style="file") myFile`
    - Multiple - `#@ File[] (label="Select some files", style="files") fileList`
  - Only directory usage
    - Single - `#@ File (label="Select a directory", style="directory") myDir`
    - Multiple - `#@ File[] (label="Select some directories", style="directories") dirList`
  - Both file and directory usage
    - `#@ File[] listOfPaths (label="select files or folders", style="both")`
