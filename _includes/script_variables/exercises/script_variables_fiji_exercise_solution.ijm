run("Close All")
sigma1 = 1.0;
sigma2 = 3.0;
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif");
rename("raw");
run("Duplicate...", "title=sigma1");
run("Gaussian Blur...", "sigma=&sigma1");
run("Duplicate...", "title=sigma2");
run("Gaussian Blur...", "sigma=&sigma2");
imageCalculator("Subtract create 32-bit", "sigma1","sigma2");