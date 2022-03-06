
## Difference of Gaussians
1. Modify the macro code and replace the hard-coded sigma value of  the gaussian blur (line 5 and 7) with 2 variables, 
`sigma1` and `sigma2` respectively
2. Make `sigma2` three times larger than `sigma1` 

```
run("Close All")
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif");
rename("raw");
run("Duplicate...", "title=sigma1");
run("Gaussian Blur...", "sigma=1");
run("Duplicate...", "title=sigma2");
run("Gaussian Blur...", "sigma=2");
// This subtracts the blurred image from the raw image, i.e. sigma2 - sigma1
imageCalculator("Subtract create 32-bit", "sigma2","sigma1");
```

> ## Solution
> ```
> run("Close All")
> sigma1 = 1.0;
> sigma2 = 3*sigma1;
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif");
> rename("raw");
> run("Duplicate...", "title=sigma1");
> run("Gaussian Blur...", "sigma=&sigma1");
> run("Duplicate...", "title=sigma2");
> run("Gaussian Blur...", "sigma=&sigma2");
> imageCalculator("Subtract create 32-bit", "sigma1","sigma2");
> ```
{: .solution}

