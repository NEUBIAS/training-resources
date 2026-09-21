# %%
# Semantic segmentation comparison using IoU

# %%
# Load segmentation label masks
import numpy as np
from OpenIJTIFF import open_ij_tiff

gt_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1.tif"
low_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_low_threshold.tif"
high_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_high_threshold.tif"

gt_labels, *_ = open_ij_tiff(gt_url)
low_labels, *_ = open_ij_tiff(low_url)
high_labels, *_ = open_ij_tiff(high_url)

# %%
# Convert label masks to binary masks for semantic comparison
# Foreground is any pixel with value > 0.
gt_binary = np.asarray(gt_labels) > 0
low_binary = np.asarray(low_labels) > 0
high_binary = np.asarray(high_labels) > 0

# %%
# Compute intersection-over-union (IoU)
def compute_iou(reference_mask, candidate_mask):
    intersection = np.logical_and(reference_mask, candidate_mask).sum()
    union = np.logical_or(reference_mask, candidate_mask).sum()
    return float(intersection / union) if union > 0 else 0.0


low_iou = compute_iou(gt_binary, low_binary)
high_iou = compute_iou(gt_binary, high_binary)

print(f"IoU (low threshold vs ground truth):  {low_iou:.4f}")
print(f"IoU (high threshold vs ground truth): {high_iou:.4f}")
