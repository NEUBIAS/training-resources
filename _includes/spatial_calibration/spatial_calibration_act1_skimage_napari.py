#######################################################
## To follow along you need to complete the tool
## installation activity for skimage napari.
#######################################################

#%%
# Import python packages.
from OpenIJTIFF import open_ij_tiff, save_ij_tiff
import numpy as np
from napari.viewer import Viewer

#%% 
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
# **Napari GUI** using the orthogonal views button (change order of visible axis) \
# **Napari GUI** inspect the volume and observe that the voxel size makes sense.\
# **Napari GUI** use 3D viewer button to inspect data in 3D.

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

# %%
# Add an image with changed scale. 
# Visualize images side by side in Napari (Orthogonal views)
napari_viewer.add_image(image, scale=voxel_size_output, name = "rescaled")

# %% [markdown]
# **Napari GUI** use the `New points layer button` to create a new point layer and name it `points2D` (double click on the name to rename a layer) \
# **Napari GUI** use `Add points` to create 2 points in the 2D slice \
# **Napari GUI** do the same for points in 3D in a separate layer called `points3D`

#%%
# extract point coordinates
layer_names = [l.name for l in napari_viewer.layers]
points2d = napari_viewer.layers[layer_names.index('points2D')].data
points3d = napari_viewer.layers[layer_names.index('points3D')].data

# %%
# compute distance between 2D points in voxel indices
dist_2d_pxl = np.sqrt(((points2d[1]-points2d[0])**2).sum())
print('Distance in pixels:',dist_2d_pxl)

# %% 
# calibrate point position and compute distance in um 
points2d_cal = np.stack([p*voxel_size_input for p in points2d])
# compute distance between points in um using calibrated point positions, appreciate that these are different values!
dist_2d_cal = np.sqrt(((points2d_cal[1]-points2d_cal[0])**2).sum())
print('Distance in um:',dist_2d_cal)

# appreciate that, in this special case, one can use voxel-distance multiplied by XY pixel size:
print('Distance in um:',dist_2d_pxl * voxel_size_input[1])

# %%
# compute distance between 3D points in voxel indices
dist_3d_pxl = np.sqrt(((points3d[1]-points3d[0])**2).sum())
print('Distance in pixels:',dist_3d_pxl)
# Appreciate that this distance doesn't make any physical sense due to the anisotropy of the image!

# %%
# Instead, one should always measure distances between points using calibration!
points3d_cal = np.stack([p*voxel_size_input for p in points3d])

# %%
# compute distance between points in um using calibrated point positions, appreciate that in this case it is important to do the calibration!
dist_3d_cal = np.sqrt(((points3d_cal[1]-points3d_cal[0])**2).sum())
print('Distance in um:',dist_3d_cal)
