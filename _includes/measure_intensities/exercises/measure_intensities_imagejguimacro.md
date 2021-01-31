Open the intensity image 
[xy_8bit__nup_bgsubtracted.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nup_bgsubtracted.tif). The image
shows the intensity of a nuclear pore protein (NUP) on the nuclear membrane. Open the label image [xy_8bit_labels__nup.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__nup.tif)

- Compute the mean intensity for each nucleus.
- Calculate the total intensity of the NUP for each nucleus.


> ## Solution
> The total intensity can be computed by multiplying the number of pixels with the mean intensity.
> ```
> /**
>  * Required update sites: 
>  *   - IJPB-Plugins (MorpholibJ)
>  */
>
>  run("Close All");
>  // File > Open
>  open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nup_bgsubtracted.tif");
>  // Image > Adjust > Brightness/Contrast... Auto
>  run("Enhance Contrast", "saturated=0.35");
>  // File > Open
>  open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__nup.tif");
>
>  // Measure intensities
>  //Plugins > MorpholibJ > Analyze > Intensity Measurements 2D/3D
>  run("Intensity Measurements 2D/3D", "input=xy_8bit__nup_bgsubtracted labels=xy_8bit_labels__nup mean max min median numberofvoxels");
> ```
{: .solution}

 - Display the label image on top of the intensity image using an Overlay (**[Image > Overlay > Add Image...]**). 
Which measurement could be problematic?

> ## Solution
> The label mask for label 3 also includes parts that are probably not part of the nuclear membrane. 
> ```
>  run("Close All");
>  // File > Open
>  open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nup_bgsubtracted.tif");
>  // Image > Adjust > Brightness/Contrast... Auto
>  run("Enhance Contrast", "saturated=0.35");
>  // File > Open
>  open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__nup.tif");
>  // Check if label mask fit our expected rim
>  // Image > Overlay > Add Image...
>  selectWindow("xy_8bit__nup_bgsubtracted.tif");
>  run("Add Image...", "image=xy_8bit_labels__nup.tif x=0 y=0 opacity=50");
>  run("Tile")
>```
{: .solution}
