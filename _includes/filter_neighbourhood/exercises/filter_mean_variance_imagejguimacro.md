## Exercise mean filter

- Apply mean filters with radii: 1, 2, 3, 5
- For each radius find the lowest threshold that yields exactly four connected components (the nuclei).
- For radius 5, what happens to the size of the segmented nuclei?

> ## Solution
> 
> - [ Image › Duplicate... ]
>   - title = mean_1
> - [ Process › Filters › Mean... ]
>   - radius = 1
> - Repeat the above with the other radii
> - Radius 1: Threshold = 
> - Radius 2: Threshold = 
> - Radius 3: Threshold = 
> - Radius 5: Threshold = 
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
