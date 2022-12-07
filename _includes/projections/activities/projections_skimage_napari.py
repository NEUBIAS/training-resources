# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# Open a 3D image
from skimage.io import imread
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif')

viewer.add_image(image)

# Maximum projection along z-axis
import numpy as np
max_z_image = np.max(image, axis=0)

viewer.add_image(max_z_image)

# Sum projection along z-axis
sum_z_image = np.sum(image, axis=0)

# Appreciate that changing the data type during sum projections is useful
print(image.dtype)
print(image.shape)
print(2**16-1) # maximum value that the image's datatype can represent
print(17*(2**16-1)) # maximum value that could occur during sum projection
print(sum_z_image.dtype) # numpy changed the data type during projection!
print(2**64-1) # maximum value that the new data type can represent

# TODO: Projections along the other axes
