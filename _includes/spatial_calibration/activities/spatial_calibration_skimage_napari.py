#######################################################
## To follow along you need to complete the tool
## installation activity for skimage napari.
#######################################################

#%%
# Import python packages.
import os, re, requests, tifffile
from napari.viewer import Viewer
import numpy as np

#%% ### download and read tif file
# download example image
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mitotic_plate_calibrated.tif"
image_fname = image_url.rsplit('/', 1)[1]
r = requests.get(image_url)
with open(os.path.join(image_fname), "wb") as f:
    f.write(r.content)

with tifffile.TiffFile(image_fname) as tif:
    array = tif.asarray()
    meta = tif.pages[0]
    y, x = [1 / item for item in meta.resolution]
    z = float(re.findall('spacing=(\d*\.*\d+)', meta.description)[0])
    voxel_size = [z, y, x]

# visualize metadata
for tag in meta.tags:
    tag_name, tag_value = tag.name, tag.value
    print(tag_name,'---', tag_value)

#%%
# Create a napari_viewer and visualize image
napari_viewer = Viewer()
napari_viewer.add_image(array, scale=voxel_size)

#%%
# update voxel size to some other values
updated_voxel_size = [1.,1.,1.]#2 * item for item in input_resolution]

# resave image
tifffile.imwrite(
    'resaved_image.tif',
    array,
    imagej = True,
    metadata = {
        'spacing':updated_voxel_size[0],
        'unit':'um',
        'axes':'ZYX',
    },
    resolution=(1./updated_voxel_size[1], 1./updated_voxel_size[2])
)

#%%
with tifffile.TiffFile('resaved_image.tif') as tif:
    array = tif.asarray()
    meta = tif.pages[0]
    y, x = [1 / item for item in meta.resolution]
    z = float(re.findall('spacing=(\d*\.*\d+)', meta.description)[0])
    updated_voxel_size = [z, y, x]

for tag in meta.tags:
    tag_name, tag_value = tag.name, tag.value
    print(tag_name,'---', tag_value)

#%%
# Create a new napari_viewer and visualize image
napari_viewer = Viewer()
napari_viewer.add_image(array, scale=updated_voxel_size)

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
points2d_cal = np.stack([p*voxel_size for p in points2d])

# compute distance between points in um using calibrated, appreciate that these are different values!
dist_2d_cal = np.sqrt(((points2d_cal[1]-points2d_cal[0])**2).sum())
print('Distance in um:',dist_2d_cal)

# appreciate that, in this special case, one case use voxel index distance multiplied y XY pxl size:
print('Distance in um:',dist_2d_pxl * voxel_size[1])

#%%
# compute distance between points in voxel indices
dist_3d_pxl = np.sqrt(((points3d[1]-points3d[0])**2).sum())
print('Distance in pixels:',dist_3d_pxl)

# Appreciate that this distance doesn't make any physical sense!
# Instead, one should always measure distances between points using calibration!
points3d_cal = np.stack([p*voxel_size for p in points3d])

# compute distance between points in um using calibrated, appreciate that in this case it is important to do the calibration!
dist_3d_cal = np.sqrt(((points3d_cal[1]-points3d_cal[0])**2).sum())
print('Distance in um:',dist_3d_cal)