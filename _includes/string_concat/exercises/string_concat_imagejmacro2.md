Create a macro that applies a gaussian blur with a certain sigma value to an image.

1. Open a sample image: [ File > Open samples > Blobs ]
1. Open the script editor: [ File > New > Script...]
1. Choose the language IJ1 Macro
1. Define a variable `blurParamKey` as the string `"sigma"`
1. Define a variable `blurParamValue` as the number `6`
1. Concatenate the variables to get a new string (`blurParams`) with this content: `"sigma=6"`
1. Add the line `Run("Gaussian Blur...", blurParams);`
1. Run the macro to see the effect on the image
1. Change the value of `blurParamValue` (e.g. set it to `12`) and run the macro again to observe the effect

> ## Solution
> ```
> // open sample image
> run("Blobs (25K)"); // optional, you may have the image open already
> // defining variables
> blurParamKey = "sigma";
> blurParamValue = 6;
> // concatenating variables, adding the equal sign in the middle
> blurParams = blurParamKey + "=" + blurParamValue;
> run("Gaussian Blur...", variable3);
> ```
{: .solution}
