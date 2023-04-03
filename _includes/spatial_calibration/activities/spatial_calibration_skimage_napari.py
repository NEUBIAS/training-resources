#######################################################
## To follow along you need to complete the tool
## installation activity for skimage napari.
#######################################################

#%%
# Import python packages.
import os, re, requests
from OpenIJTIFF import open_ij_tiff
from skimage.io import imsave
import numpy as np
from napari.viewer import Viewer

#%% ### download and read tif file
# load image from url
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mitotic_plate_calibrated.tif"
image, axes, voxel_size_input, units = open_ij_tiff(fpath)

# visualize metadata
print(axes)
print(voxel_size_input)
print(units)

#%%
# Create a napari_viewer and visualize image
napari_viewer = Viewer()
napari_viewer.add_image(image, scale=voxel_size_input)

#%%
# update voxel size to some other values
# change voxel size
voxel_size_output = [s*2. for s in voxel_size_input]
print('Output voxel size:', voxel_size_output)

# resave the image including all metadata
imsave(
    'resaved_image.tif',
    image,
    imagej=True,
    metadata={
        'spacing':voxel_size_output[0],
        'unit':'um',
        'axes':'ZYX',
    },
    resolution=(1./voxel_size_output[1], 1./voxel_size_output[2])
)

#%%
# Create a new napari_viewer and visualize image
napari_viewer = Viewer()
napari_viewer.add_image(image, scale=voxel_size_output)

# using the horthogonal views button (change order of visible axis), 
# inspect the volume and observe that the voxel size makes sense.
# use 3D viewer button to inspect data in 3D.

#%%
# extract point coordinates
layer_names = [l.name for l in napari_viewer.layers]
points2d = napari_viewer.layers[layer_names.index('points2D')].data
points3d = napari_viewer.layers[layer_names.index('points3D')].data

#%%
# compute distance between points in voxel indices
dist_2d_pxl = np.sqrt(((points2d[1]-points2d[0])**2).sum())
print('Distance in pixels:',dist_2d_pxl)

# calibrate point position
points2d_cal = np.stack([p*voxel_size_input for p in points2d])

# compute distance between points in um using calibrated, appreciate that these are different values!
dist_2d_cal = np.sqrt(((points2d_cal[1]-points2d_cal[0])**2).sum())
print('Distance in um:',dist_2d_cal)

# appreciate that, in this special case, one case use voxel index distance multiplied y XY pxl size:
print('Distance in um:',dist_2d_pxl * voxel_size_input[1])

#%%
# compute distance between points in voxel indices
dist_3d_pxl = np.sqrt(((points3d[1]-points3d[0])**2).sum())
print('Distance in pixels:',dist_3d_pxl)

# Appreciate that this distance doesn't make any physical sense!
# Instead, one should always measure distances between points using calibration!
points3d_cal = np.stack([p*voxel_size_input for p in points3d])

# compute distance between points in um using calibrated, appreciate that in this case it is important to do the calibration!
dist_3d_cal = np.sqrt(((points3d_cal[1]-points3d_cal[0])**2).sum())
print('Distance in um:',dist_3d_cal)