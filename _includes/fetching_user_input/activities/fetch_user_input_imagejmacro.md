Open macro  [fetch_user_input_median_sizeFilter.ijm](https://github.com/NEUBIAS/training-resources/raw/master/_includes/fetching_user_input/activities/fetch_user_input_median_sizeFilter.ijm)

1. Identify the input parameters to be fetched
2. Write code to create a GUI to fetch these parameters

> ```
>#@ Integer (label="Median filter radius", value=5) medianFilterRadius
>#@ Integer (label="Minimum object size", value=50) minObjectSize
>
>// close all opened windows
>run("Close All");
>
>// open sample blobs image
>run("Blobs (25K)");
>
>// Change to gray lookup table
>run("Grays");
>
>//Apply median filter with radius of your choice
>run("Median...", "radius="+ medianFilterRadius);
>
>// Apply Otsu thresholding to binarize the image
>run("Auto Threshold", "method=Otsu white");
>
>// Run a size filter to discard smaller objects
>run("Size Opening 2D/3D", "min="+minObjectSize);
>
> ```
