Open the multidimensional image [xyz_16bit_t1-head.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_t1-head.tif).
- Reslice the image from different directions, such that you can view the image stack from the side, from the top, and from the front.

> ## Solution
> ```
>// This macro opens and binarizes the Blobs image, and uses the particle analyzer to measure features of >blobs of certain sizes and circularities.
>// Different outputs are saved: ROIs, results table, and label mask.
>
>// specify an output directory
>outputDir = FIXME # (e.g. r'C:\Users\UserName\Desktop' on Windows or '/Users/UserName/Desktop/' on MacOS)
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

> ## Solution
> ```
>""" Open the head image stack and reslice it to view it from different angles (side, top, and front) """
>
>// Close other open images
>run("Close All");
>
>// open head image stack
>open("http://imagej.net/images/t1-head.zip");
>rename("Head viewed from the side");
>
>// Reslice the head image stack to view the head from the top and from the side
>run("Reslice [/]...", "output=1.500 start=Top"); // view head from the top
>rename("Head viewed from the top");
>run("Reslice [/]...", "output=1.500 start=Left"); // view head from the front
>rename("Head viewed from the front");

>run("Tile");
> ```
{: .solution}
