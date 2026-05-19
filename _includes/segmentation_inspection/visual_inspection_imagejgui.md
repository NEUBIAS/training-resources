<h4 id="visual_inspection_imagejgui"><a href="#visual_inspection_imagejgui">Visual inspection by overlaying segmentations on the raw image</a></h4>

 - Open [xy_8bit__mitocheck_incenp_t1.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif)
 - Open [xy_8bit_labels__mitocheck_incenp_t1.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1.tif)
 - Open [xy_8bit_labels__mitocheck_incenp_t1_low_threshold.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_low_threshold.tif)
 - Open [xy_8bit_labels__mitocheck_incenp_t1_high_threshold.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_high_threshold.tif)
 - For each label image, create an overlay on the raw image:
   - Select the label image and add the raw image as overlay using **[Image > Overlay > Add Image...]**
     - Opacity: 50 % 
 - Compare overlays and discuss visible error types:
   - Missing foreground
   - Extra foreground
   - Merged objects
   - Split objects
