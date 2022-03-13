- Open the intensity image
[xy_8bit__nup.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nup.tif).
  - The image contains the signal of a single confocal slice of a nuclear pore protein (NUP) on the nuclear membrane. 
- Open the binary image [xy_8bit_binary__nup.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nup.tif)
- Generate a label mask image from the binary image
- Measure the both the mean and sum intensity of the NUP for each nucleus
  - Don't forget to measure and take into account the image background
- Think about the biophysical meaning of the mean and sum intensity.

> ## Solution
>
> |Label|Mean|NumberOfVoxels|BG|Mean_corr|Sum_corr|
> |1|34.3762|2092|25|9.38|19622|
> |2|31.9296|2343|25|6.93|16236|
> |3|32.4747|1342|25|7.47|10024|
>
> - Interpretation of the mean intensity: The label masks seem generally wider than the nuclear envelope, thus an interpreation of the mean intensity as the local NUP density on the membrane is problematic. However, if the width of the label masks is kept constant across the experiment the mean intensity could indeed be a number that is proportional to the NUP density.
> - Interpretation of the sum intensity: The sum intensity is very much affected by the size of the measured region. It could be that in this image the nuclei were optically sectioned at different z-positions, cutting a more or less big region out of the nucleus. The sum intensity seem thus not very useful here.
> - ImageJ GUI workflow
>   - Required update sites
>     - IJPB-Plugins (MorpholibJ)
>   - open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nup.tif");
>   - [ Image > Rename ] "intensity"
>   - open("httpR://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nup.tif");
>   - [ Plugins › MorphoLibJ › Binary Images › Connected Components Labeling ]
>     - connectivity = 4
>      - type = [8 bits]
>   - [ Image > Rename ] "labels"
>   - [ Plugins > MorpholibJ > Analyze > Intensity Measurements 2D/3D ]
>     - input = intensity
>     - labels = labels
>     - [X] mean
>     - [X] numberofvoxels
>   - Measure background intensity by drawing an ROI and [ Analyze > Measure ] 
>   - Measure the corrected mean and sum intensity using the formulas given in the main text of this module
{: .solution}

- Display the label image on top of the intensity image using an Overlay ([Image > Overlay > Add Image...]).
- Based on this overlay, do you think the quantification of the signal of one of the nuclei may be problematic?

> ## Solution
> - The label mask for label 3 also includes regions that are probably not part of the nuclear membrane and all intensity measurements may be affected by this.
{: .solution}
