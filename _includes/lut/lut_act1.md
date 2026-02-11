<h4 id="explore"><a href="#explore">Explore LUTs</a></h4>
- Open the image [xy_8bit__nuclei_high_dynamic_range.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif)
- Adjust LUT to highlight certain objects
  1. See only brightest objects & observe pixel values
    - Keep `max` value fixed at highest number
    - Set `min` value to a higher number
  1. Look at dim objects
    - Keep `min` value fixed at lowest number
    - Set `max` value to a lower number until you see dimmest ones
- Avoid certain LUTs  
  1. Do not use multicolor LUTs with no biological meaning
    - Change LUT to some RGB colormap (example 3-3-2 RGB) and observe changes
  1. Do not use red color (some people have color-blindness)
  1. Safe choice is "gray"
- Find extreme pixel values
  - Change to LUT that shows extreme values e.g.,"HiLo" -> shows clipping
- Present LUT adjustments in scientifically correct manner
  - Use inset of LUT color bar in your adjusted image to show what pixel values depict
  - Show `min` and `max` settings using text/value pairs or slider bar screenshot next to image

  <!-- - Open the image [xy_8bit__nuclei_high_dynamic_range.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif)
  - Explore different contrast settings
    - Observe that there are very dim nuclei
  - Observe that LUT settings do not change pixel values
  - Explore various single color LUTs (e.g., gray, green, red, blue)
    - Understand that gray is the recommended default
    - Understand that certain LUTs such as red and blue should be avoided
  - Explore various multi color LUTs, which can be helpful to
    - highlight extreme values
    - render high dynamic range data without "clipping information"
  - Visualize the LUT itself, e.g. as an inset in the image
    - Understand that this is especially important for multi-color LUTs where the mapping from the displayed color to the numeric data is not obvious -->
