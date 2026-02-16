<h4 id="explore"><a href="#explore">Learn about important lookup tables</a></h4>

To visualize an image there are several lookup tables to choose from.
Depending upon the use-case, one can be more appropriate than another.
In this activity, we will look at commonly used LUTs and discuss how and when to use them.



- Open the image [xy_8bit__nuclei_high_dynamic_range.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif)
- Adjust contrast settings to highlight certain objects
  1. See only brightest objects & observe pixel values
    - Keep `max` value fixed at highest number
    - Set `min` value to a higher number
  1. Look at dim objects
    - Keep `min` value fixed at lowest number
    - Set `max` value to a lower number until you see dimmest ones
- Select appropriate color map
  1. Single color
    - Do not use red/blue color (hard to see/some people have color-blindness)    
    - Safe choice is "gray"
  1. Multicolor
    - Do not select LUTs with no biological meaning (??)

  1.
- Display extreme pixel values using a single colormap
  - Change to multicolor map that shows extreme values e.g.,"HiLo" -> shows clipping
