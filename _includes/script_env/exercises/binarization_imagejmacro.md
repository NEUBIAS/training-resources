Open image [xy_8bit__PCNA.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif) and 
1. Find a threshold value so that there are 2 foreground nuclei.
2. Find a threshold value so that only the bright dots remain
3. Find threshold interval so that only the boundary of the nuclei remains.

> ## Solution
> ```
> open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif")
> selectWindow("xy_8bit__PCNA.tif");
> run("Duplicate...", "title=[2 nuclei]");
> selectWindow("xy_8bit__PCNA.tif");
> run("Duplicate...", "title=[boundary]");
> selectWindow("xy_8bit__PCNA.tif");
> run("Duplicate...", "title=[dots]");
> selectWindow("2 nuclei");
> setThreshold(5, 255);
> setOption("BlackBackground", true);
> run("Convert to Mask");
> selectWindow("boundary");
> setThreshold(4, 4);
> setOption("BlackBackground", true);
> run("Convert to Mask");
> selectWindow("dots");
> setThreshold(44, 255);
> setOption("BlackBackground", true);
> run("Convert to Mask");
> ```
{: .solution}
