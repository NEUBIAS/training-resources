Adapt the below code to change the following:
1. Specify an output directory
2. Save the results table as comma-separated data table instead of text-delimited data.
3. Save the output label image in a different image format (e.g. PNG, JPEG).
4. When running the code, try to specify different output directories.

> ## Solution
> ```
>// This macro opens and binarizes the Blobs image, and uses the particle analyzer to measure features of >blobs of certain sizes and circularities.
>// Different outputs are saved: ROIs, results table, and label mask.
>
>// specify an output directory
>outputDir = FIXME # (e.g. 'C:\\Users\\username\\Desktop' or 'C:/Users/username/Desktop' on Windows, or '/Users/username/Desktop/' on MacOS)
>
>// specify settings
>min_size = 100;
>max_size = 500;
>min_circ = 0.5;
>max_circ = 1;
>
>// close any pre-existing output you do not want in your saving results
>roiManager("reset"); // clear any pre-existing ROIs
>run("Clear Results"); // clear any pre-existing results
>run("Close All"); // close any open images
>
>// threshold blob image and run particle analyzer
>run("Set Measurements...", "area centroid center perimeter bounding redirect=None decimal=3") // set desired >measurements
>open("http://imagej.net/images/blobs.gif"); // open blobs
>run("Convert to Mask"); // convert to mask using default settings
>run("Analyze Particles...", "size=&min_size-&max_size circularity=&min_circ-&max_circ show=[Count Masks] >display add") // run the particle analyzer
>run("glasbey", "display=blob_labels_macro.tif view=net.imagej.display.DefaultDatasetView@541b120b")
>roiManager("Select All") // select all rois
>roiManager("Save", outputDir + "/blob_ROIset_macro.zip"); // save rois to output directory
>saveAs("Results", outputDir + "/blob_results_macro.csv"); // save results file to output directory
>saveAs("Png", outputDir + "/blob_labels_macro.png"); // save label mask to output directory
> ```
{: .solution}
