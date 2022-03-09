> ## Solution
> ```
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__few_separate_nuclei.tif");
> run("Invert");
> run("Gaussian Blur...", "sigma=5");
> run("Classic Watershed", "input=xy_8bit__few_separate_nuclei-watershed.tif mask=None use min=0 max=255");
> ```
{: .solution}
