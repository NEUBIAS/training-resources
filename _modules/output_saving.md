---
title:     Output saving

layout:    module

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
  There are multiple situations in which you need to save the different types of output you can generate with FIJI. For example, you may want to save your results tables for further analysis in other software (e.g. RStudio, MS EXCEL, ..). It can also be important to save the ROIs that were used for particular measurements, so that you can look back at them for reference, or to use them for visualization purposes. In addition to ROIs, images can be saved as label masks to store the information about different regions. Finally, you may also want to save your entire script containing particular settings or parameters that you used, so that you have re-run the analysis with the exact same settings or compare it with the results obtained using different settings. When you save your output, try to think about the 'interoperability' of the file format: does it allow you to safely re-open the data afterwards or in different software?

concept_map: >
  graph TD
    II("Input image") --> IA("Image analysis process")
    IA("Image analysis process") --> RS("Results table")
    IA("Image analysis process") --> ROI("ROIs")
    IA("Image analysis process") --> PM("Label mask")

figure: /figures/output_saving.png
figure_legend: Image analysis processes can yield several outputs, such as results tables, ROI sets and label masks.

activity_preface: |
  - Open the blobs image (File > Open Samples > Blobs).
  - Binarize it and run the 'analyze particles' command to generate different kinds of output.
  - Save the different output types.

activities:
  - ["ImageJ GUI/Macro", "output_saving/activities/output_saving_macro.ijm", "java"]
  - ["ImageJ Jython", "output_saving/activities/output_saving_jython.py", "python"]

exercises:
  - ["ImageJ Macro", "output_saving/exercises/output_saving_imagejmacro.md"]
  - ["ImageJ Jython", "output_saving/exercises/output_saving_jython.md"]

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
    - The best default output format for results tables is tab-delimited text.

    > ## Solution
    >   - Label masks should be saved in JPEG format. **False** (JPEG compression results in loss of the unique label values in the image)
    >   - The best default output format for results tables is tab-delimited text. **True** (this is generally more stable in other software than for example comma-delimited data)
    {: .solution}

learn_next:
  - "[Opening pre-saved ROIs/Images/datasets and modify them (?)]"

external_links:
  - "[MorpholibJ](https://imagej.net/plugins/morpholibj)"

---
#### Image thresholding
A common algorithm for binarization is thresholding. A threshold value `t` is chosen, either manually or automatically,
and all pixels with intensities below `t` are set to 0, whereas pixels with intensities `>= t` are set to the value for the foreground.
Depending on the software the foreground value can be different (e.g. 1 in MATLAB or 255 in ImageJ). At any pixel (x,y):

`p_im(x,y) < t` -> `p_bin(x,y) = 0`

`p_im(x,y) >= t` -> `p_bin(x,y) = 1`

where, p_im and p_bin are the intensity and binary images respectively.

It is also possible to define an interval of threshold values, i.e. a lower and upper threshold value. Pixels with intensity values
within this interval belong to the foreground and vice versa.
