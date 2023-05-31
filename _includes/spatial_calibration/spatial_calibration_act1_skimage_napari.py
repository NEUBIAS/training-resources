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
image, axes, voxel_size, units = open_ij_tiff(
    "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mitotic_plate_calibrated.tif"
)

# %%
# Inspect the image axes metadata.
print(axes)
print(voxel_size)
print(units)

# %%
# Open napari and add the image with its voxel size.
napari_viewer = Viewer()
napari_viewer.add_image(image, scale=voxel_size)

# %% [markdown]
# **Napari GUI**: Change the axes order using the corresponding button. \
# **Napari GUI**: Use the 3D viewer button to render the image in 3D.

# %% [markdown]
# ### Compute distances between points
#
# **Napari GUI** use the `New points layer button` to create a new points layer \
# **Napari GUI** use `Add points` to add two points somewhere on the meta-phase plate \

# %%
# extract point coordinates
points = napari_viewer.layers['Points'].data
print(points)

# %%
# compute distance between points in voxel indices
diff_vector = points[1]-points[0]
print("diff_vector: ", diff_vector)
sqr_diff_vector = diff_vector**2
print("sqr_diff_vector: ", sqr_diff_vector)
dist_pxl = np.sqrt(sqr_diff_vector.sum())
print('Distance in pixels:',dist_pxl)

# %%
# calibrate the positions
points_cal = points * napari_viewer.layers['Points'].scale
print(points_cal)

# %%
# compute calibrated distance between points
dist_cal = np.sqrt(((points_cal[1]-points_cal[0])**2).sum())
print('Distance in um:',dist_cal)

# %%
