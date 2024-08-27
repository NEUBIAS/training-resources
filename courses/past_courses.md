# List of past courses performed using this material

Please note that some links may be outdated as they are from the date of the course. Each module/topic takes about 30-45 min to teach, it starts with an activity and finishes with hands-on by students.

# July 2023, ABiS-GBI 2023 course - Image data: image analysis, data management and reuse
In person course Okazaki and Kobe, Japan, 2023 July 3-7
See https://github.com/NEUBIAS/training-resources/blob/master/courses/2023_ABIS-GBI_image_data_and_analysis.md for further details.


# June 2023, Beginners course for python based image analysis using skimage and napari
Hybrid course with online sessions and in person hands-on. 
The hands-on were performed by faculty staff on different sites.

Course dates 2023 June 6, 7, 13. See https://github.com/NEUBIAS/training-resources/blob/master/courses/2023_skimage_napari_beginners.md for further details

# December 2022, Basics of Bioimage Analysis using the ImageJ GUI and scripting
Course dates 2022 December 7, 8, 9
In person course at the Max Planck Institute for Experimental Medicine, Heidelberg, 3 days.
Teacher Antonio Politi, MPI-NAT, Göttingen.

At the end of the course we worked on student projects using their image data. 

# March 2022, ImageJ macro scripting for bioimage analysis

A course with 2 afternoons a 4 hours each.  Each day had a 30 min break. 
**Teachers** 
 
 * Arif Kahn, EMBL, Heidelberg
 * Anniiek Stoekkermans, EMBL, Heidelberg
 * Christian Tischer, EMBL, Heidelberg
 * Antonio Politi, MPI-NAT, Göttingen
 
### Pre-requisites
Essential: Practical experience using the graphical user interface of Fiji.

Helpful: Knowledge of basic concepts of bioimage analysis. 

Topics covered in Basics of Image Analysis using the ImageJ GUI course, March 2022 (see below)

### Monday, 21. March 2022, 13:00 – 17:00 CET
 * [Running, understanding and modifying an ImageJ macro](https://neubias.github.io/training-resources/script_run/index.html)
 * [Recording a script](https://neubias.github.io/training-resources/script_record/index.html)
 * [Variables](https://neubias.github.io/training-resources/script_variables/index.html)
 * [String concatenation](https://neubias.github.io/training-resources/string_concat/index.html)

### Monday, 22. March 2022, 13:00 – 17:00 CET
 * [Automated output saving (label mask images, ROIs, and tables)](https://neubias.github.io/training-resources/output_saving/index.html)
 * [Handling script parameters](https://neubias.github.io/training-resources/fetching_user_input/index.html)
 * [Loops](https://neubias.github.io/training-resources/script_for_loop/index.html)
 * [Batch processing](https://neubias.github.io/training-resources/batch_processing/index.html)

Some commands manipulating strings in IJMacro
```
imageDir = File.getDirectory(inputImageFile);
print(imageDir);
print(File.getParent(imageDir));
indexOf(imageDir, File.separator);
split(imageDir, File.separator); // gets you an array
```
Also see https://imagej.net/scripting/parameters


# March 2022, Basics of Image Analysis using the ImageJ GUI


A course with 4 afternoons a 4 hours each.  Each day had a 2x30 min break. 
**Teachers** 
 * Arif Kahn, EMBL, Heidelberg
 * Anniiek Stoekkermans, EMBL, Heidelberg
 * Christian Tischer, EMBL, Heidelberg
 * Antonio Politi, MPI-NAT, Göttingen

### Pre-requisites
Additional modules that are needed for the course, but are not covered in the course: 
 * [Digital image Basics](https://neubias.github.io/training-resources/pixels/index.html) 
 * [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)
 * [Spatial calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html)
 * [Data types](https://neubias.github.io/training-resources/datatypes/index.html) and 
 * [Image file formats](https://neubias.github.io/training-resources/image_file_formats/index.html) 

### Monday, 7. March 2022, 13:00 – 17:00 CET
 * [Segmentation](https://neubias.github.io/training-resources/segmentation/index.html)
 * [Thresholding (Foreground background segmentation)](https://neubias.github.io/training-resources/binarization/index.html)
 * [Connected component labeling](https://neubias.github.io/training-resources/connected_components/index.html)
 * [Object shape measurements](https://neubias.github.io/training-resources/measure_shapes/index.html)
 * [Basic 2D object analysis](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
 
How to add numbers on label image https://forum.image.sc/t/overlay-numbers-on-image/35604/2
Also look at  https://github.com/BIOP/ijp-LaRoMe

Spotfinder for FISH-data using Radial Symmetry - https://www.researchsquare.com/article/rs-992563/v1 https://github.com/PreibischLab/RS-FISH

### Tuesday, 08. March 2022, 13:00 – 17:00 CET
 * [Object filtering](https://neubias.github.io/training-resources/filter_objects/index.html)
* [Object intensity measurements](https://neubias.github.io/training-resources/measure_intensities/index.html) see also [Global background correction](https://neubias.github.io/training-resources/global_background_correction/index.html)
* [Image neighborhood filtering ](https://neubias.github.io/training-resources/filter_neighbourhood/index.html)
 * [Median filter](https://neubias.github.io/training-resources/median_filter/index.html) 
 * Workflow: [2D noisy object segmentation and filtering](https://neubias.github.io/training-resources/workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/index.html)

### Monday, 14. March 2022, 13:30 – 17:00 CET
 * [Local background subtraction](https://neubias.github.io/training-resources/local_background_correction/index.html) 
 * [Morphological filters](https://neubias.github.io/training-resources/filter_morphological/index.html)
 * [Skeletonization] [https://neubias.github.io/training-resources/skeletonization/index.html]

### Tuesday, 15. March 2022, 13:30 – 17:00 CET
 * [Automatic threshold using the histogram](https://neubias.github.io/training-resources/auto_threshold/index.html)
 * [Distance transform](https://neubias.github.io/training-resources/distance_transform/index.html)
 * [Watershed](https://neubias.github.io/training-resources/watershed/index.html)
 * Workflow: [Nuclei and cells segmentation](https://neubias.github.io/training-resources/workflow_nuclei_and_cells_segmentation/index.html)

### Follow up discussions:
**Watershed integrated workflows in ImageJ**

For shape based watershed (input is binary), integrated workflows with distance transform + watershed are for example:  [Process >  Binary > Watershed] this is only 2D or [MorpholibJ > Binary > Distance Transform Watershed] and [MorpholibJ > Binary > Distance Transform Watershed 3D]

Discussion on different features of distance transform https://github.com/NEUBIAS/training-resources/issues/327

**Machine learning with pre-defined features**
In these tools you draw on the image some areas that belong, e.g. to foreground or background. The algorithm computes rules to classify all the pixels of the image. Works really well most of the time. 
https://www.ilastik.org/download.html
Within ImageJ you can try Weka trainable segmentation. https://imagej.net/plugins/tws/

**Deep learning based segmentation (some examples)**
Can achieve superior results for complex problems. Using pre-trained models is typically quite easy. The tools we indicate have pre-trained models. 
https://imagej.net/plugins/stardist https://github.com/stardist/stardist
https://github.com/MouseLand/cellpose https://www.cellpose.org/
If you need to train models this requires a more involved software installation on specific hardware (GPU with CUDA enabled) and some knowledge in python. There are effort to make this process “easier” https://github.com/HenriquesLab/ZeroCostDL4Mic




# June 2021, Basics of Bioimage Analysis
A course with 4 afternoons a 3 hours each.  Each day had a 30 min break. 
**Teachers** 
 * Antonio Politi, MPI-NAT Göttingen
 * Christian Tischer, EMBL, Heidelberg

### Monday, 07. June 2021, 14:00 – 17:00 CET
 * Self introductions
 * [Digital image Basics](https://neubias.github.io/training-resources/pixels/index.html) 
 * [Spatial calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html)
 * [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)

### Tuesday, 08. June 2021, 14:00 – 17:00 CET
 * Self introductions
 * [Thresholding](https://neubias.github.io/training-resources/binarization/index.html)
 * [Connected component labeling](https://neubias.github.io/training-resources/connected_components/index.html)
 * [Data types](https://neubias.github.io/training-resources/datatypes/index.html)
 * [Object shape measurements](https://neubias.github.io/training-resources/measure_shapes/index.html)
 * Optional homework Workflow - [Nuclei segmentation and shape measurements](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
 
### Monday, 14. June 2021, 14:00 – 17:00 CET
 * [Nuclei segmentation and shape measurements](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html) Discuss if there has been problems 
 * [Object intensity measurements](https://neubias.github.io/training-resources/measure_intensities/index.html)
 * [Global background correction](https://neubias.github.io/training-resources/global_background_correction/index.html)
 * [Neighbourhood filters (introduction)](https://neubias.github.io/training-resources/filter_neighbourhood/index.html)

### Tuesday, 15. June 2021, 14:00 – 17:00 CET
Self introduction 
 * Self study recommendations (see follow up material for self study)
 * [Median filter](https://neubias.github.io/training-resources/median_filter/index.html)
 * [Local background subtraction](https://neubias.github.io/training-resources/local_background_correction/index.html)
 * [Object filtering](https://neubias.github.io/training-resources/filter_objects/index.html)
 * [Workflow - 2D segmentation of noisy images with object filtering](https://neubias.github.io/training-resources/workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/index.html)

### Follow up material
* https://github.com/tischi/segmentation-annotator A plugin to navigate labels and image
* https://forum.image.sc/ Very useful to post questions and browse through. 
* https://imagej.net/ The main site for imageJ

# January-February 2021,  Basics of Bioimage Analysis

**Title: Basics of Bioimage Analysis**

A course with 4 afternoons a 3 hours each.  Each day had a 30 min break. 

**Teachers** 
 * Antonio Politi, MPI-NAT Göttingen
 * Christian Tischer, EMBL, Heidelberg

### Monday, 25. January 2021, 14:00 – 17:00 CET
 * [Digital image Basics](https://neubias.github.io/training-resources/pixels/index.html) 
 * [Spatial calibration](https://neubias.github.io/training-resources/spatial_calibration/index.html)
 * [Lookup tables](https://neubias.github.io/training-resources/lut/index.html)
	
### Tuesday, 26. January 2021, 14:00 – 17:00 CET
 * [Thresholding](https://neubias.github.io/training-resources/binarization/index.html)
 * [Connected component labeling](https://neubias.github.io/training-resources/connected_components/index.html)
 * [Data types](https://neubias.github.io/training-resources/datatypes/index.html)
 * [Object shape measurements](https://neubias.github.io/training-resources/measure_shapes/index.html)
 * Optional homework Workflow - [Nuclei segmentation and shape measurements](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html)
The workflow summarizes what we have learned during the first 2 days.
We can discuss it on Monday


### Monday, 1. February 2021, 14:00 – 17:00 CET
 * [Nuclei segmentation and shape measurements](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html) Discuss if there has been problems 
 * [Object intensity measurements](https://neubias.github.io/training-resources/measure_intensities/index.html)
 * [Global background correction](https://neubias.github.io/training-resources/global_background_correction/index.html)
 * [Neighbourhood filters (introduction)](https://neubias.github.io/training-resources/filter_neighbourhood/index.html)

### Tuesday, 2. February 2021, 14:00 – 17:00 CET
 * Self introduction 
 * Self study recommendations (see follow up material for self study)
 * [Median filter](https://neubias.github.io/training-resources/median_filter/index.html)
 * [Local background subtraction](https://neubias.github.io/training-resources/local_background_correction/index.html)
 * [Filter objects](https://neubias.github.io/training-resources/filter_objects/index.html)
 * [Workflow - 2D segmentation of noisy images with object filtering](https://neubias.github.io/training-resources/workflow_segment_2d_noisy_nuclei_filter_objects_measure_shape/index.html)
 
 
 ### Follow-up material
* Analysis of fluorescence data in ImageJ:  https://petebankhead.gitbooks.io/imagej-intro/content/
* ImageJ Macro: https://www.youtube.com/watch?v=o8tfkdcd3DA
* Colocalisation: https://www.youtube.com/watch?v=P2JvFe0hB_M
* Advanced MorpholibJ: https://www.youtube.com/watch?v=_SiM33C3KcE
* NEUBIAS youtube channel (more specialized topics): https://www.youtube.com/channel/UC-oy7UpEhRfHQ-5ePCviKFg
* How to ask for help (active and responsive): https://forum.image.sc/
**Python:**
* https://www.youtube.com/watch?v=2KF8vBrp3Zw
* https://scikit-image.org/docs/dev/api/skimage.html
**R**
* https://www.bioconductor.org/packages/release/bioc/html/EBImage.html


