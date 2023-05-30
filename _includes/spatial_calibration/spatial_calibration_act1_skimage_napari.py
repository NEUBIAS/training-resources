# %%
#######################################################
## To follow along you need to complete the tool
## installation activity for skimage napari.
#######################################################

# %%
# Import python packages.
from OpenIJTIFF import open_ij_tiff, save_ij_tiff
import numpy as np
from napari.viewer import Viewer

# %%
# download and read tif file
# load image from url
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mitotic_plate_calibrated.tif"
image, axes, voxel_size_input, units = open_ij_tiff(fpath)

# visualize metadata
print(axes)
print(voxel_size_input)
print(units)

# %%
# Create a napari_viewer and visualize image
napari_viewer = Viewer()
napari_viewer.add_image(image, scale=voxel_size_input)

# %% [markdown]
# - **Napari GUI** using the orthogonal views button (`Change order of visible axes`)
# - **Napari GUI** inspect the volume and observe that the voxel size makes sense.
# - **Napari GUI** use 3D viewer button to inspect data in 3D (`Toggle ndisplay`).

# %%
# update voxel size to some other values
# change voxel size and resave
voxel_size_output = voxel_size_input
voxel_size_output[0] = voxel_size_output[0]*2
print('Output voxel size:', voxel_size_output)

save_ij_tiff(
    'resaved_image.tif',
     image,
     axes,
     voxel_size_output,
     units
)

# %% [markdown]
# - Add an image with changed scale.
# - Visualize images side by side in Napari (`toggle grid mode`)

# %%
napari_viewer.add_image(image, scale=voxel_size_output, name = "rescaled")

# %% [markdown]
# - **Napari GUI** use the `New points layer button` to create a new point layer
# - **Napari GUI** use `Add points` to create 2 points (in the same plane or in different planes)

# %%
# extract point coordinates
points = napari_viewer.layers['Points'].data

# %%
# compute distance between points in voxel indices
dist_pxl = np.sqrt(((points[1]-points[0])**2).sum())
print('Distance in pixels:',dist_pxl)

# %%
# extract point calibrated positions
points_cal = napari_viewer.layers['Points'].data * napari_viewer.layers['Points'].scale

# %%
# compute distance between points in um using calibrated point positions
dist_cal = np.sqrt(((points_cal[1]-points_cal[0])**2).sum())
print('Distance in um:',dist_cal)

# %% [markdown]
# - discuss why dist_pxl differs from dist_cal
# - appreciate that one needs to use spatial calibration to obtain distances in physical units

# %%
