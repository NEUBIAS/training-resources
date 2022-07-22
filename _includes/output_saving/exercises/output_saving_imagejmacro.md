Adapt the code from the activity such that you:
1. Specify an output directory in the beginning
2. Save the results table as comma-separated data table instead of text-delimited data.
3. Save the output label image in a different image format (e.g. PNG, JPEG). Is this a good format for label images?

> ## Solution
> ```java
>// This macro uses the particle analyzer to measure features of shapes.
>// Different outputs are saved: ROIs, results table, and label mask.
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
>roiManager("Save", outputDir + "/shapes_ROIset_macro.zip"); // save rois to output directory
>saveAs("Results", outputDir + "/shapes_results_macro.csv"); // save results file to output directory
>saveAs("Png", outputDir + "/shapes_labels_macro.png"); // save label mask to output directory
> ```
{: .solution}
