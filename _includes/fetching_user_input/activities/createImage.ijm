// Define input parameters here to be fetched
#@ File (label = "Select image file", style="file") imageFile
#@ Integer (label="Gaussian filter radius", min=0, max=10, value=5) filterRadius
#@ Integer (label="Size of opening SE", style="slider", min=1, max=15, stepSize=2) openingSESize
#@ String (choices={"Median", "Mean"}, style="listBox", description="Filter type") preprocessingFilterType
#@ String (choices={"channel 1", "channel 2"}, style="radioButtonHorizontal") segmentChannel
#@ File (label = "Select folder to save segmented image", style="directory") outputDirFile
#@ Boolean (label = "Show image/label mask overlay") makeOverlay


// CODE goes here

open(imageFile);
run("Gaussian Blur...", "sigma="+filterRadius);
.
.
.
.
//