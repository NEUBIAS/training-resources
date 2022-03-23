---
title:     Output saving
layout:    module
tags: ["scripting"]
prerequisites:
  - "[Binarize an image](../binarization)"
  - "[Connected components labeling](../connected_components)"
  - "[Simple 2D object analysis](../workflow_segment_2d_nuclei_measure_shape)"
  - "Generating results tables"
  - "Defining regions of interest (ROIs)"

objectives:
  - "Save measurements as a table"
  - "Save ROIs"
  - "Save output label mask"

motivation: |
  There are multiple situations in which you need to save the different types of output you can generate with your image analysis pipelines. For example, you may want to save your results as measurement tables for further analysis in other software (e.g. RStudio, MS EXCEL, ..). It can also be important to save the regions of interest (ROIs) that were used for particular measurements, so that you can look back at them for reference, or to use them for visualization purposes. In addition to ROIs, images can be saved as label masks to store the information on different regions. Finally, you may also want to save your entire script containing particular settings or parameters that you used, so that you can re-run the analysis with the exact same settings or compare it with the results obtained using different settings.

concept_map: >
  graph TD
    II("Input image") --> IA("Image analysis process")
    IA --> RS("Measurements table")
    IA --> ROI("ROIs")
    IA --> PM("Label mask")

figure: /figures/output_saving.png
figure_legend: Image analysis processes can yield several outputs, such as a) label masks, b) measurement tables, or c) regions of interest (ROIs), which may include different types, such as polygon outlines, lines or points.

activity_preface: |
  - Use a template script and run it.
  - Understand what the commands do.
  - Record yourself saving the output.
  - Edit the script using the recorded commands.
  - Optional: define an output directory as a parameter and use string concatenation to specify where to save the file and with what name. An example output directory could be 'C:\\\Users\\\username\\\Desktop' on Windows (note double "\\" because a single "\\" is interpreted as an escape character) or '/Users/username/Desktop/' on MacOS.

activities:
  - ["ImageJ Macro", "output_saving/activities/output_saving_imagej-macro.md"]
  - ["ImageJ Jython", "output_saving/activities/output_saving_imagej-jython.md"]

exercises:
  - ["ImageJ Macro", "output_saving/exercises/output_saving_imagej-macro.md"]
  - ["ImageJ Jython", "output_saving/exercises/output_saving_imagej-jython.md"]

assessment: >

  ### Fill in the blanks

    - Three commonly saved data output types include  ___ .
    - In order to safely re-open your data or open it in different software, you need to save in an ____ file format.

    > ## Solution
    >   - Three commonly saved data output types include **results tables, ROI sets, and label masks**.
    >   - In order to safely re-open your data or open it in different software, you need to save in an **interoperable** file format.
    {: .solution}

  ### True or False
    - Label masks should be saved in JPEG format.
    - Tab-delimited text is a decent output format for results tables.

    > ## Solution
    >   - Label masks should be saved in JPEG format. **False** (JPEG compression results in loss of the unique label values in the image)
    >   - Tab-delimited text is a decent output format for results tables. **True** (this is generally more stable in other software than for example comma-delimited data)
    {: .solution}

learn_next:
[comment]: <> (Open a pre-saved data set, ROI set or label image and try to modify it)

external_links:


---
