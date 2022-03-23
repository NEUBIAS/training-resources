1. Download the template script: [output_saving_imagej-macro_template.ijm](https://github.com/NEUBIAS/training-resources/tree/master/_includes/output_saving/activities/output_saving_imagej-macro_template.ijm). The aim of the script is to generate different kinds of output (labels, results, ROIs) from this image: [xy_8bit_binary_randomshapes.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary_randomshapes.tif).
2. Run and understand the script.
2. Add commands that save the different output: label image, results table, ROIs.

> ## Solution
> ```java
>// This macro uses the particle analyzer to measure features of shapes.
>// Different outputs are saved: ROIs, results table, and label mask.
>
>// make sure the background is set to black in Process>Binary>Options
>run("Options...", "iterations=1 count=1 black do=Nothing");
>
>// specify an output directory
>outputDir = FIXME // (e.g. 'C:\\Users\\username\\Desktop' or 'C:/Users/username/Desktop' on Windows, or '/Users/username/Desktop/' on MacOS)
>
>// specify size parameters for object selection
>minSize = 0
>maxSize = 1000
>
>// close any pre-existing output you do not want in your saving results
>roiManager("reset"); // clear any pre-existing ROIs
>run("Clear Results"); // clear any pre-existing results
>run("Close All"); // close any open images
>
>// Set measurements and run particle analyzer on binary shapes image
>run("Set Measurements...", "area centroid center perimeter bounding redirect=None decimal=3") // set desired measurements
>open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary_randomshapes.tif"); // open binary image with random shapes
>run("Analyze Particles...", "size=&minSize-&maxSize show=[Count Masks] display add") // run the particle analyzer>run("glasbey")
>
>// Save the results
>saveAs("tiff", outputDir + File.separator + "shapes_labels_macro.tiff"); // save label mask to output directory
>saveAs("results", outputDir + File.separator + "shapes_results_macro.txt"); // save results file to output directory
>roiManager("Save", outputDir + File.separator + "shapes_ROIset_macro.zip"); // save rois to output directory
> ```
{: .solution}
