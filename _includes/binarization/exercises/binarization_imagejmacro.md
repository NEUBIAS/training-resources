Use imageJMacro to create 3 binary images from *xy_8bit_PCNA.tif* where 
1. 2 foreground nuclei.
2. only the boundary of the 2 nuclei
3. only the bright dots remain

> ## Solution
> ```
> // duplicate the image
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
