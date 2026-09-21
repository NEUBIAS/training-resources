<h4 id="semantic_comparison_imagejgui"><a href="#semantic_comparison_imagejgui">Semantic comparison with IoU in ImageJ GUI</a></h4>

 - Open [xy_8bit_labels__mitocheck_incenp_t1.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1.tif) as reference
 - Open [xy_8bit_labels__mitocheck_incenp_t1_low_threshold.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_low_threshold.tif)
 - Open [xy_8bit_labels__mitocheck_incenp_t1_high_threshold.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_high_threshold.tif)

### Prepare binary masks (foreground > 0)

For each image (reference and candidate):
 - Convert to 8-bit using **[Image > Type > 8-bit]** if needed
 - Set threshold using **[Image > Adjust > Threshold...]**
   - Lower threshold: `1`
   - Upper threshold: maximal value
 - Press `Apply` to create a binary image

### Compute IoU for one candidate mask

Let `Ref_bin` be the reference binary image and `Cand_bin` be one candidate binary image.

 - Compute intersection with **[Process > Image Calculator...]**
   - Operation: `AND`
   - Image1: `Ref_bin`
   - Image2: `Cand_bin`
 - Compute union with **[Process > Image Calculator...]**
   - Operation: `OR`
   - Image1: `Ref_bin`
   - Image2: `Cand_bin`
 - Count foreground pixels (value `255`) in both images using **[Analyze > Histogram]**
   - `N_intersection`: count at value 255 in the AND image
   - `N_union`: count at value 255 in the OR image
 - Compute IoU:
   - `IoU = N_intersection / N_union`

Repeat this for both low-threshold and high-threshold candidates and compare their IoU values.
