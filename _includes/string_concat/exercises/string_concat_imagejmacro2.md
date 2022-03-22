Create a macro that applies a gaussian blur with a certain sigma value to an image.

1. Open a sample image: [ File > Open samples > Blobs ]
1. Open the script editor: [ File > New > Script...]
1. Choose the language IJ1 Macro
1. Add the line `run("Gaussian Blur...", "sigma=6");`
  - Tip: In programming copy and paste as much as possible!
1. Run the macro to see the effect on the image
1. Define a variable `blurSigma` with the value `6`
1. Replace the `6` in the `run(...)` command with this variable.

> ## Solution
> ```javascript
> blurSigma = 6;
> run("Gaussian Blur...", "sigma="+blurSigma );
> // Below would also work and is very convenient, but a bit non-standard...
> // run("Gaussian Blur...", "sigma=&blurSigma");
> ```
{: .solution}
