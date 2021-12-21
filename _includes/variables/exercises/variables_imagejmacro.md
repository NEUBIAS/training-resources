
1. Modify the macro code and introduce a variable for the gaussian blur sigma (line 5). Name the variable `sigma1`
2. Extend the macro and add a duplicate image and gaussian blur with a higher `sigma2 = sigma1 + 2`
3. Subtract the two gaussian blurred images (sigma2 - sigma1)


```
run("Close All")
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif");
rename("raw");
run("Duplicate...", "title=sigma1");
run("Gaussian Blur...", "sigma=1");
// This subtracts the blurred image from the raw image, i.e. raw - sigma1
imageCalculator("Subtract create 32-bit", "raw","sigma1");
```

> ## Solution
> ```
> run("Close All")
> sigma1 = 1.0;
> sigma2 = sigma1 + 2;
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif");
> rename("raw");
> run("Duplicate...", "title=sigma1");
> run("Gaussian Blur...", "sigma=&sigma1");
> run("Duplicate...", "title=sigma2");
> run("Gaussian Blur...", "sigma=&sigma2");
> imageCalculator("Subtract create 32-bit", "sigma1","sigma2");
> ```
{: .solution}

