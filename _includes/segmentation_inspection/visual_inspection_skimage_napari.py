# %%
# Visual inspection of segmentation overlays

# %%
# Create a napari viewer
import napari

viewer = napari.Viewer()

# %%
# Load raw and segmentation images
from OpenIJTIFF import open_ij_tiff

raw_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif"
gt_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1.tif"
low_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_low_threshold.tif"
high_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__mitocheck_incenp_t1_high_threshold.tif"

raw, *_ = open_ij_tiff(raw_url)
gt_labels, *_ = open_ij_tiff(gt_url)
low_labels, *_ = open_ij_tiff(low_url)
high_labels, *_ = open_ij_tiff(high_url)

# %%
# Overlay all segmentations on top of the raw image
viewer.add_image(raw, name="raw")
viewer.add_labels(gt_labels, name="ground_truth", opacity=0.45)
viewer.add_labels(low_labels, name="low_threshold", opacity=0.45)
viewer.add_labels(high_labels, name="high_threshold", opacity=0.45)

# %%
# Close viewer at the end so the script can run in automated tests
viewer.close()
