- Open [xy_8bit__nuclei_very_noisy.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_very_noisy.tif)
- Apply a mean filter to the image such that you can binarise the image into exactly three disjoint foreground regions (the three nuclei).
  - What is the smallest size for the mean filter that does the job?


> ## Solution
> ```
> run("Close All");
> 
> // File › Open...
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_very_noisy.tif");
> // Process › Filters › Mean...
> run("Mean...", "radius=2");
> // Image › Adjust › Threshold...
> setThreshold(29, 255);
> setOption("BlackBackground", true);
> run("Convert to Mask");
> ```
{: .solution}
