- Open the input image, and invert it using  **[Edit > Invert]** or **[Ctrl+Shift+I]**
- Apply watershed transform on inverted image using **[Plugins > MorpholibJ > Segmentation > Classic Watershed]**
     - `Input = xy_8bit__touching_objects.tif`
     - `Mask = none`
     - `[X] use diagonal connectivity`
     - `Min h = 0`
     - `Max h = 255`
- Create mask
  - Duplicate the input image using **[Image > Duplicate]** `Title = mask`
  - Find/apply threshold using **[Image >Adjust > Threshold...]** (e.g. `Lower Threshold Level = 9`) and press `Apply`
- Apply watershed transform on inverted image and selecting mask using **[Plugins > MorpholibJ > Segmentation > Classic Watershed]**
     - `Input = xy_8bit__touching_objects.tif`
     - `Mask = mask`
     - `[X] use diagonal connectivity`
     - `Min h = 0`
     - `Max h = 255`