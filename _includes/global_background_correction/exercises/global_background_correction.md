Open image 
[xy_16bit__nuclei_with_background.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__nuclei_with_background.tif)
1. Measure the background 
2. Subtract the background from the image 
3. Is the mean intensity in the background region close to 0 (<<1)? If not which image conversion have you forgotten?
3. Verify that the histogram has not been clipped by the background subtraction operation.

> ## Solution
> In order to obtain a correct result the background subtraction should be performed with an image that 
> has been converted to a float (in ImageJ 32-bit). This avoid clipping of the data for the low values. 
>
> ```
> run("Close All");
> roiManager("reset");
> run("Clear Results");
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__nuclei_with_background.tif");
> rename("intenisty")
> // 1. Measure the background
> // Draw a rectangle 
> makeRectangle(19, 16, 70, 52);
>
> //Add to RoiManager using key t
> roiManager("Add");
> // Measure intensity
> run("Measure");
> // Disable current ROI (select the whole image or click on it)
> run("Select All");
>
> // 2. Subtract the background without conversion  and check mean in background region
> // Process › Math › Subtract...
> run("Subtract...", "value=104.182");
> rename("bg subtracted 16bit")
> setMinAndMax("0.00", "100");
> run("Enhance Contrast", "saturated=0.35");
> // Measure the intensity in background region
> roiManager("Select", 0);
> run("Measure");
> run("Histogram");
> 
> // 3. Subtract the background with prior conversion
> // Open the image again
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__nuclei_with_background.tif");
> // Subtract the background with prior conversion to float (32-bit)
> // Image > Type > 32-bit
> run("32-bit");
> //  Process › Math › Subtract...
> run("Subtract...", "value=104.182");
> run("Enhance Contrast", "saturated=0.35");
> rename("bg subtracted 32bit")
> // Measure the intensity in background region
> roiManager("Select", 0);
> run("Measure");
> setMinAndMax("0.00", "100");
> run("Histogram", "bins=256 use x_min=-10 x_max=100.0 y_max=Auto");
> ```
{: .solution}


Can you think of a way of automatically computing a global background?  
> ## Solution
> For this exercise we just compute the mean intensity in the space that is not the nuclei.  We can use
> thresholding but with different low and upper values. 
>
> ```
> /**
> * Required update sites: 
> *   - IJPB-Plugins (MorpholibJ)
> **/
>
> //File> Open...
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__nuclei_with_background.tif")
> // Image > Duplicate...
> run("Duplicate...", "binary");
> // Image > Adjust > Threshold ...
> setThreshold(0, 117);
> setOption("BlackBackground", true);
> run("Convert to Mask");
>
> // Plugins › MorphoLibJ › Binary Images › Connected Components Labeling
> run("Connected Components Labeling", "connectivity=4 type=[16 bits]");
> rename("labels");
> // Plugins › MorphoLibJ › Analyze › Intensity Measurements 2D/3D
> run("Intensity Measurements 2D/3D", "input=intensity labels=labels mean max numberofvoxels");
> ```
{: .solution}
