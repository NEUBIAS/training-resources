# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# Read the intensity image
from skimage.io import imread
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif')

# View the intensity image
viewer.add_image(image)

# Check the intensity image's datatype
print(image.dtype)

# Inspect the intensity image values in order to identify a threshold
# that segments both cells
# napari GUI: hover with mouse, line profile

# Threshold the image
binary_image_two_cells = image > 49

# Overlay the binary image
viewer.add_image(binary_image_two_cells, opacity=0.8)

# Inspect data type
print(binary_image_two_cells.dtype)

# Inspect value content
import numpy as np
print(np.unique(binary_image_two_cells))

# Apply a higher threshold
# to only select the brighter cell
binary_image_one_cell = image > 100
viewer.add_image(binary_image_one_cell, opacity=0.8)
