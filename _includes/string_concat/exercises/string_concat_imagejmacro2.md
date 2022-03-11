Create a macro that applies a gaussian blur with a certain sigma value to an image.

1. Open a sample image: [ File > Open samples > Blobs ]
1. Open the script editor: [ File > New > Script...]
1. Choose the language IJ1 Macro
1. Define `variable1` as the string `"sigma"`
1. Define `variable2` as the number `6`
1. Concatenate the variables to get a new string (`variable3`), looking like this: `"sigma=6"`
1. Add the line `Run("Gaussian Blur...", variable3);`
1. Run the macro to see the effect on the image
1. Change the value of `variable2` (e.g. set it to `12`) and run the macro again to observe the effect

> ## Solution
> ```
> // defining variables
> variable1 = "sigma";
> variable2 = 6;
> // concatenating variables, adding the equal sign in the middle
> variable3 = variable1 + "=" + variable2;
> run("Gaussian Blur...", variable3);
> ```
{: .solution}
