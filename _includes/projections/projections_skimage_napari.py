#######################################################
## To follow along you need to complete the tool
## installation activity for skimage napari.
#######################################################

#%%
# Import python packages.
from OpenIJTIFF import open_ij_tiff
import numpy as np
from napari.viewer import Viewer
from skimage.transform import rescale

#%%
# Instantiate the napari viewer
viewer = Viewer()

#%%
# Open a 3D image
image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif')
viewer.add_image(image)

#%%
# Remember the axis order 0=z, 1=x, 2=y
# Maximum projection along z-axis
max_z_image = np.max(image, axis=0)
viewer.add_image(max_z_image)

#%%
# Sum projection along z-axis
sum_z_image = np.sum(image, axis=0)
viewer.add_image(sum_z_image)

#%%
# Appreciate that changing the data type during sum projections is useful
print(np.iinfo(image.dtype)) # maximum value that the image's datatype can represent
print(image.shape[0]*np.iinfo(image.dtype).max) # maximum value that could occur during sum projection
print(sum_z_image.dtype) # luckily numpy changed the data type during projection
print(np.iinfo(sum_z_image.dtype)) # maximum value that the new data type can represent

#%%
# Maximum projection along x-axis and y-axis
max_x_image = np.max(image, axis=2)
max_y_image = np.max(image, axis=1)
viewer.add_image(max_x_image)
viewer.add_image(max_y_image)

#%%
# Due to the aniotropic pixel size the x and y projections appear squashed
# We can rescale the image to make it appear physcially correct
np.set_printoptions(precision=3)
print(f"Voxel size in micrometer [Z, Y, X]: {np.array(scales)}")

dz = scales[0]
dy = scales[1]
dx = scales[2]

#%%
# The axes of the max_y_image are 0=z,1=x
# The z axes is squashed thus we enlarge it to make the image isotropic
rescaled_max_y_image = rescale(max_y_image, [dz/dy,1])  
viewer.add_image(rescaled_max_y_image)

# The max_x_image could be rescaled in the  same way
