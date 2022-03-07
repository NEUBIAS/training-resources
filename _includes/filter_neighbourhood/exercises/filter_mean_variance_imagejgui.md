## Exercise mean filter
- Open image [xy_8bit__noisy_two_nuclei_close.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_very_noisy_close.tif)
- The aim is to segment the image into foreground/background in order to get a similar result to [xy_8bit_binary__noisy_two_nuclei_close.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei_very_noisy_close.tif)
- To achive this aim, try thresholding the image after applying a mean filter with different radii.
  - Try thresholding
    - Without a mean filter
    - After applying a mean filter of radius: 1, 2, 3, or 5
  - For each filter setting find the lowest threshold that yields exactly four connected components (the nuclei).
    - Is this even possible without applying a mean filter?
    - For radius 5, what happens to the size of the segmented nuclei?

> ## Solution
> - [ Image › Duplicate... ]
> - [ Process › Filters › Mean... ]
>   - Radius = 1,2,3,5 pixel
> - [ Image > Adjust > Threshold... ]
>   - Radius 1: threshold = 38
>   - Radius 2: threshold = 43
>   - Radius 3: threshold = 48
>   - Radius 5: threshold = 57
 - Only segmenting the four nuclei in unfiltered image does not work, as it yields a large number of undesired connected components (noise).
> - Radius 1 yields a reasonable segmentation.
> - For radius 5 one has to choose a rather high threshold to still separate some of the nuclei and thus the segmented nuclei become very small.
{: .solution}

## Exercise variance filter
- Open image [xy_8bit__em_mitochondria_er.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__em_mitochondria_er.tif)
- Apply a variance filter [ Process > Filter > Variance... ] to segment the cell regions from the background
  - Hints:
    - Convert image to float, because the filter may yield high values [ Image > Type > 32-bit ]
- What is the minimal filter radius that yields a good segmentation?

> ## Solution
> - [ Image › Rename...]
>   - Title = input
> - [ Image › Duplicate... ]
>   - Title = variance_5
> - [ Image > Type > 32-bit ]
>   - In variance calculation, pixel values can exceed 255 which is the maximum value that can be achieved in current bit depth (unsigned 8-bit) of input image.
> - [ Process › Filters › Variance... ]
>   - `Radius = 5 pixels`
> - [ Image › Adjust › Threshold... ]  
>   - `([x] Dark Background)`
>   - `Lower threshold level = 80` (other values can also be chosen)
>   - `Higher threshold level = 1e30`
>   -  Press `Set`
>   - Press `Apply`
>      - Press `Convert to Mask`
> - [ Image › Lookup Tables › Invert LUT ] (Optional: if highest values are darker and lowest brighter)
> - The minimal radius is 5, smaller radii yield holes in the foreground region.
{: .solution}
