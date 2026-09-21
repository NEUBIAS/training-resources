<h4 id="instance_comparison_imagejgui"><a href="#instance_comparison_imagejgui">Instance comparison using object count and mean object area</a></h4>

 - Open [xy_8bit_labels__mitocheck_incenp_t1.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1.tif) as reference
 - Open [xy_8bit_labels__mitocheck_incenp_t1_low_threshold.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_low_threshold.tif)
 - Open [xy_8bit_labels__mitocheck_incenp_t1_high_threshold.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_high_threshold.tif)

For each image:
 - If needed, convert to binary mask using **[Image > Adjust > Threshold...]** and `Apply`
 - Set measurements using **[Analyze > Set Measurements...]**
   - Select `Area`
   - Select `Display Label`
 - Run connected components and measurements using **[Analyze > Analyze Particles...]**
   - `Size`: `0-Infinity`
   - `Circularity`: `0.00-1.00`
   - Select `Display results` and `Summarize`
 - Record from the `Summary` table:
   - `Count`
   - `Average Size`

Compare `Count` and `Average Size` for low-threshold and high-threshold segmentations against the reference.
