# %%
# Instance segmentation comparison: object counts and mean object area

# %%
# Load segmentation label masks
import numpy as np
from skimage.measure import label, regionprops_table
from OpenIJTIFF import open_ij_tiff

gt_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1.tif"
low_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_low_threshold.tif"
high_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_high_threshold.tif"

gt_labels, *_ = open_ij_tiff(gt_url)
low_labels, *_ = open_ij_tiff(low_url)
high_labels, *_ = open_ij_tiff(high_url)

# %%
# Convert to connected-component instances and compute summary statistics
def instance_stats(label_like_image):
    binary = np.asarray(label_like_image) > 0
    instance_labels = label(binary)
    object_count = int(instance_labels.max())

    if object_count == 0:
        return object_count, 0.0

    props = regionprops_table(instance_labels, properties=("area",))
    mean_area = float(np.mean(props["area"]))
    return object_count, mean_area


gt_count, gt_mean_area = instance_stats(gt_labels)
low_count, low_mean_area = instance_stats(low_labels)
high_count, high_mean_area = instance_stats(high_labels)

# %%
# Print direct comparison against the reference segmentation
print("Reference (ground truth):")
print(f"  object count   = {gt_count}")
print(f"  mean area      = {gt_mean_area:.2f}")
print()
print("Low-threshold segmentation:")
print(f"  object count   = {low_count} (difference: {low_count - gt_count:+d})")
print(f"  mean area      = {low_mean_area:.2f} (difference: {low_mean_area - gt_mean_area:+.2f})")
print()
print("High-threshold segmentation:")
print(f"  object count   = {high_count} (difference: {high_count - gt_count:+d})")
print(f"  mean area      = {high_mean_area:.2f} (difference: {high_mean_area - gt_mean_area:+.2f})")
