## Exercise 1
- Choose a radius for the SE of mean filter that would give good segmentation
- Discuss the effect of choosing different radius for SE on objects close to each other


> ## Solution
> ```
> // File > Close All
> run("Close All");
>
> // Image › Rename...
> rename("input");
>
> // Image › Duplicate...
> run("Duplicate...", "title=mean_1" );
>
> // Process › Filters › Mean...
> run("Mean...", "radius=1");
>
> selectWindow("input");
> // Image > Duplicate...
> run("Duplicate...", "title=mean_2" );
>
> // Process › Filters › Mean...
> run("Mean...", "radius=2");
>
> selectWindow("input");
> // Image > Duplicate...
> run("Duplicate...", "title=mean_5" );
>
> // Process › Filters › Mean...
> run("Mean...", "radius=5");
>
> selectWindow("input");
> // Image > Duplicate...
> run("Duplicate...", "title=mean_7" );
>
> // Process › Filters › Mean...
> run("Mean...", "radius=7");
>
> // Window > Tile
> run("Tile");
> ```
{: .solution}

## Exercise 2
- Choose a radius for the SE of variance filter that would give good segmentation
- Discuss about the resulting pixel values and the image data type
- Discuss the effect of choosing different radius for SE on segmentation


> ## Solution
> ```
> // File > Close All
> run("Close All");
>
> // Image › Rename...
> rename("input");
>
> // Image › Duplicate...
> run("Duplicate...", "title=variance_5");
>
> // Image > Type > 16-bit (since in variance calculation, pixel values can exceed 255 which is current bit depth of input image)
> run("16-bit");
>
> // Process › Filters › Variance...
> run("Variance...", "radius=5");
> selectWindow("variance_5");
>
> Image › Adjust › Threshold...   ([x] Dark Background)
> setAutoThreshold("Default dark");
>
> // Press `Set` button (example upper and lower threshold values are (113, 255))
> setThreshold(113, 255);
>
> // Press `Apply` button
> run("Convert to Mask");
>
> // Image › Lookup Tables › InvertLUT... (Optional: if highest values are darker and lowest brighter)
> run("Invert LUT");
> ```
{: .solution}
