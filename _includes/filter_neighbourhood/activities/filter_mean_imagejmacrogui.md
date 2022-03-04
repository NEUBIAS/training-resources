## Activity 1
- Apply a mean filter (**[Process > Filters > Mean...]**) to the image such that you can binarise
the image into exactly three disjoint foreground regions (the three nuclei). It is helpful to first duplicate the image
**[Image > Duplicate ...]** or **[Ctrl-Shift-D]**
  - What is the smallest size for the mean filter that does the job?
  - What happens if the filter size increases?


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

## Activity 2
- Hint: Select a filter that would yield equal pixel values i.e. brighter than background


> ## Solution
> ```
> run("Close All");
> // File > Open...
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__one_foreground_pixel.tif")
> // Duplicate the image Image > Duplicate...
> run("Duplicate...", "title=radius2");
> // Maximum filter Process › Filters › Maximum...
> run("Maximum...", "radius=2");
> ```
{: .solution}
