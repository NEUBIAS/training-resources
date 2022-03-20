Hint: You need to modify the code in line 5 and 6 and for example use the `&` operator.

```javascript
run("Close All")
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif");
rename("raw");
run("Duplicate...", "title=sigma1");
run("Gaussian Blur...", "sigma = 1");
run("Duplicate...", "title=sigma2");
run("Gaussian Blur...", "sigma = 1.5");
// This subtracts the blurred image from the raw image, i.e. sigma1 - sigma2
imageCalculator("Subtract create", "sigma1","sigma2");
```

> ## Solution
> ```javascript
> run("Close All")
> sigma1 = 1.0;
> sigma2 = 1.5;
> // For part two
> // sigma2 = 3*sigma1; 
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif");
> rename("raw");
> run("Duplicate...", "title=sigma1");
> run("Gaussian Blur...", "sigma=&sigma1");
> run("Duplicate...", "title=sigma2");
> run("Gaussian Blur...", "sigma=&sigma2");
> // This subtracts the blurred image from the raw image, i.e. sigma1 - sigma2
> imageCalculator("Subtract create", "sigma1","sigma2");
> ```
{: .solution}

