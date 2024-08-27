<h4 id="explore"><a href="#explore">Explore LUTs</a></h4>

  - Open the image [xy_8bit__nuclei_high_dynamic_range.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif)
  - Explore different contrast settings
    - Observe that there are very dim nuclei
  - Observe that LUT settings do not change pixel values
  - Explore various single color LUTs (e.g., gray, green, red, blue)
    - Understand that gray is the recommended default
    - Understand that certain LUTs such as red and blue should be avoided
  - Explore various multi color LUTs, which can be helpful to 
    - highlight extreme values
    - render high dynamic range data without "clipping information"
  - Visualise the LUT itself, e.g. as an inset in the image
    - Understand that this is especially important for multi-color LUTs where the mapping from the displayed color to the numeric data is not obvious
