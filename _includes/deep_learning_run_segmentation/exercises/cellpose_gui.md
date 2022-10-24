- Download [this two-channel image](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_8bit__membranes_nuclei_big.tif).
- Open the image in `Cellpose`
  - `cell diameter: 60`
  - `chan to segment: 1 red` (membranes)
  - `chan2 (optional): 0 none`
  - Run the `cyto` model

Do you have a different opinion on the segmentation, if yes, can you locate regions where you think `cellpose` may have segmented differently?

> ## Solution
> Hint: Use `MASKS ON [x]` and `outlines on [Z]` to view the problematic areas in much intuitive way. Use arrow keys up and down to switch between channels and different display modes. Increase contrast if necessary.
>     The problematic segmented areas are shown here: ![problematic areas](/figures/cellpose_exercise_problematic_areas.png)
{: .solution}

Play with `Cell diameter`, `chan to segment` and `chan2(optional)` and find parameter values to improve the segmentation from the preceding step

> ## Solution
> One way to do this is to use nuclear channel information by setting `chan2 (optional): 2 green` and run `cyto` model again. Another way to make results better is to use a lower `Cell diameter = 40`
{: .solution}
