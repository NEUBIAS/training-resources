## Exercise variance filter
- Open image [xy_8bit__em_mitochondria_er.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__em_mitochondria_er.tif) or 
[xy_16bit__embryo_transmission.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__embryo_transmission.tif)
- Apply a variance filter [ Process > Filter > Variance... ] to segment the cell regions from the background
  - Hints:
    - Convert image to float or 16 bit, because the filter may yield high values [ Image > Type > 32-bit ]
- What filter radius and threshold yield a good segmentation?

> ## Solution
> - [ Image › Rename...]
>   - Title = input
> - [ Image › Duplicate... ]
>   - Title = variance_5
> - [ Image > Type > 32-bit ]
>   - In variance calculation, pixel values can exceed 255 which is the maximum value that can be achieved in current bit depth (unsigned 8-bit) of input image.
> - [ Process › Filters › Variance... ]
>   - `Radius = 15 pixels`
> - [ Image › Adjust › Threshold... ]  
>   - `([x] Dark Background)`
>   - `Lower threshold level = 90 (1.5 for second example)`
>   - `Higher threshold level = 1e30`
>   -  Press `Set`
>   - Press `Apply`
>      - Press `Convert to Mask`
{: .solution}
