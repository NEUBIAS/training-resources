## Exercise mean filter

- The expected result from manual thresholding should be [xy_8bit_binary__noisy_two_nuclei_close.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei_very_noisy_close.tif)
- Is applying manual thresholding operation possible directly on raw image?
- Apply mean filters with radii: 1, 2, 3, 5
- For each radius find the lowest threshold that yields exactly four connected components (the nuclei).
- For radius 5, what happens to the size of the segmented nuclei?

> ## Solution
> No applying manual thresholding on raw images gives a large number of undesired connected components
>
> - [ Image › Duplicate... ]
>   - title = mean_1
> - [ Process › Filters › Mean... ]
>   - radius = 1
> - Repeat the steps above with the other radii
> - Radius 1: Lower Threshold Level = 38
> - Radius 2: Lower Threshold Level = 43
> - Radius 3: Lower Threshold Level = 48
> - Radius 5: Lower Threshold Level = 57
>
> For radius 5 the segmented nuclei are smaller.
{: .solution}

## Exercise variance filter

- Apply a variance filter that segments the cell regions from the background
  - Hints:
    - Convert image to float, because the filter may yield high values [ Image > Type > 32-bit ]
    - [ Process > Filter > Variance... ]
- What is the minimal radius to yields a good segmentation?

> ## Solution
>
> - [ Image › Rename...]
>   - Title = input
> - [ Image › Duplicate... ]
>   - Title = variance_5
> - [ Image > Type > 32-bit ] (since in variance calculation, pixel values can exceed 255 which is current bit depth of input image)
> - [ Process › Filters › Variance... ]
>   - radius = 5
> - [ Image › Adjust › Threshold... ]  
>   - ([x] Dark Background)
>   - Lower threshold level = 80 (other values can also be chosen)
>   - Higher threshold level = 1e30
>   -  Press `Set`
>   - Press `Apply`
>      - Press `Convert to Mask`
> - [ Image › Lookup Tables › Invert LUT ] (Optional: if highest values are darker and lowest brighter)
>
> 5, lesser radii would tend to produce more holes in the segmented region
{: .solution}
