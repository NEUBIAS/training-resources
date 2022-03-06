## Exercise mean filter
- Open image [xy_8bit__noisy_two_nuclei_close.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_very_noisy_close.tif)
- Segment image into foreground/background in order to get a similar result (see this binary image - [xy_8bit_binary__noisy_two_nuclei_close.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei_very_noisy_close.tif))
- Is applying manual thresholding operation possible directly on raw image?
- Apply mean filters with radii: 1, 2, 3, 5
- For each radius find the lowest threshold that yields exactly four connected components (the nuclei).
- For radius 5, what happens to the size of the segmented nuclei?

> ## Solution
> - Applying thresholding on the raw image does not work, as it yields a large number of undesired connected components
> - [ Image › Duplicate... ]
>   - `Title = mean_1`
> - [ Process › Filters › Mean... ]
>   -` Radius = 1 pixel`
> - Repeat the steps above with the other radii
> - Radius 1: lowest threshold level = 38
> - Radius 2: lowest threshold level = 43
> - Radius 3: lowest threshold level = 48
> - Radius 5: lowest threshold level = 57
>
> For radius 5 the segmented nuclei are smaller.
{: .solution}

## Exercise variance filter
- Open image [xy_8bit__em_mitochondria_er.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__em_mitochondria_er.tif)
- Apply a variance filter [ Process > Filter > Variance... ] to segment the cell regions from the background
  - Hints:
    - Convert image to float, because the filter may yield high values [ Image > Type > 32-bit ]
- What is the minimal filter radius that yields a good segmentation?

> ## Solution
>
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
>
> The minimal radius is 5, smaller radii yield holes in the foreground region.
{: .solution}
