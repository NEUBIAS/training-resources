# %% [markdown]
# ## Spatial image calibration
# #### Requirements
# - [skimage and napari](https://neubias.github.io/training-resources/tool_installation/index.html#skimage_napari)

# %%
# Import python packages.
from OpenIJTIFF import open_ij_tiff, save_ij_tiff
import numpy as np
from napari.viewer import Viewer

# %%
# Open an image and its axes metadata
image_cal, axes_image_cal, voxel_size_image_cal, units_image_cal = open_ij_tiff(
    "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nucleus_calibrated.tif"
)

# %%
# Inspect the image axes metadata.
print("Shape: ", image_cal.shape)
print("Axes: ", axes_image_cal)
print("Scale: ", voxel_size_image_cal)
print("Units: ", units_image_cal)

# %%
# Open an image and its axes metadata
image_nucleus, axes_image_nucleus, voxel_size_image_nucleus, units_image_nucleus = open_ij_tiff(
    "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__nucleus.tif"
)

# %%
# Inspect the image axes metadata.
print("Shape: ", image_nucleus.shape)
print("Axes: ", axes_image_nucleus)
print("Scale: ", voxel_size_image_nucleus)
print("Units: ", units_image_nucleus)

# %%
# Note that this image does not have a calibrated voxel size
# Add spatial calibration using the voxel_size from the first image
voxel_size_image_nucleus = [0.52, *voxel_size_image_cal]
units_image_nucleus = ["um","um","um"]

# %%
# Inspect the new image axes metadata.
print("Shape: ", image_nucleus.shape)
print("Axes: ", axes_image_nucleus)
print("Scale: ", voxel_size_image_nucleus)
print("Units: ", units_image_nucleus)

# %%
# Open napari and add the image with its voxel size.
napari_viewer = Viewer()
napari_viewer.add_image(image_cal, scale=voxel_size_image_cal, name='image_cal')
napari_viewer.add_image(image_nucleus, scale=voxel_size_image_nucleus, name='image_nucleus')

# %% [markdown]
# Napari GUI: Change the axes order using the corresponding button. \
# Napari GUI: Use the 3D viewer button to render the image in 3D.

# %%
# Change the voxel size of the last image.
changed_voxel_size = voxel_size_image_nucleus
changed_voxel_size[0] = changed_voxel_size[0]*2
print('Output voxel size:', changed_voxel_size)

# %%
# Save image
save_ij_tiff(
    'resaved_image.tif',
     image_nucleus,
     axes_image_nucleus,
     changed_voxel_size,
     units_image_nucleus
)

# %%
# Open save tif file in FIJI and verify image scales were properly saved.

# %%
# Visualise an image with changed voxel sizes (scale) in napari. 
# Visualize images side by side in Napari (Orthogonal views)
napari_viewer.add_image(image_nucleus, scale=changed_voxel_size, name = "rescaled")


# %% [markdown]
# - Activate `grid mode`
# - Activate 3D view (`toggle ndisplay` button)
# - Inspect images in 3D.

# %%
