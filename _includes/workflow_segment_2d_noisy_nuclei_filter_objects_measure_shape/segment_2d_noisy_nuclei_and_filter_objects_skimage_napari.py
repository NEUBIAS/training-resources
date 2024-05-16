# %%
# Import modules
import napari
from OpenIJTIFF import open_ij_tiff, save_ij_tiff
from skimage.filters.rank import mean
from skimage.morphology import disk, remove_small_objects, remove_small_holes
from skimage.measure import label, regionprops_table
from skimage.segmentation import clear_border
import pandas as pd
import os
import numpy as np

# %% [markdown]
# ### Process the first image

# %%
# Instantiate the napari viewer
napari_viewer = napari.Viewer()

# Read and inspect the image:
fpath = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_small.tif'
image, axes_image, scales_image, units_image = open_ij_tiff(fpath)
napari_viewer.add_image(image)

# %%
# Apply local mean filter
radius = 3

disk_radius = disk(radius)
denoised_image = mean(image, disk_radius)
napari_viewer.add_image(denoised_image)

# %%
# Binarize the image:
thr = 25

binary_image = denoised_image > thr
napari_viewer.add_labels(binary_image)

# %%
# Fill small holes
min_size_holes = 100

filled_binary_image = remove_small_holes(binary_image, area_threshold=min_size_holes)
napari_viewer.add_labels(filled_binary_image)

# %%
# Find labels
connectivity = 2

label_mask = label(filled_binary_image, connectivity=connectivity)
napari_viewer.add_labels(label_mask)

# %%
# Remove small regions
min_size_regions = 100

filtered_label_mask = remove_small_objects(label_mask, min_size=min_size_regions)
napari_viewer.add_labels(filtered_label_mask)

# %%
# Remove regions touching the borders
filtered_label_mask_no_borders = clear_border(filtered_label_mask)
napari_viewer.add_labels(filtered_label_mask_no_borders)

# %%
# Print areas for each cell:
properties = pd.DataFrame(regionprops_table(filtered_label_mask_no_borders,
                properties = {'label', 'area'}))
print(properties)

# %%
# Find the basename of the input file from input file path
file_name = os.path.basename(fpath)
base_name = os.path.splitext(file_name)[0]
print(base_name)

# %%
# Save final label mask as tif file
mask_save_name = base_name+"_labelmask.tif"
save_ij_tiff(mask_save_name, filtered_label_mask_no_borders.astype(np.uint8), axes_image, scales_image, units_image)
print(f"The label mask is saved as : {mask_save_name}")

# %%
# Save object properties dataframe as csv file
table_save_name = base_name+"_intensity_measurements.csv"
properties.to_csv(table_save_name, index=False)
print(f"The object properties are saved as : {table_save_name}")
# %%
# Repeat the steps on the second image

# %%
