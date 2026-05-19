# Distance transform with skimage using napari as a viewer

import imageio.v3 as imageio
from OpenIJTIFF import open_ij_tiff
import napari
from scipy import ndimage

if 'viewer' not in globals():
    viewer = napari.Viewer()

image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources'
                       '/raw/master/image_data/xy_8bit_labels__four_objects.tif')
print(image.dtype)

distance_map = ndimage.distance_transform_edt(image)
print(distance_map.dtype)

viewer.add_image(image)
viewer.add_image(distance_map)

# %% 
# Close the viewer (CI test requires this)
viewer.close()