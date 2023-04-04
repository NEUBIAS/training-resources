# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# Read the intensity image
from skimage.io import imread
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif')

# View the intensity image
viewer.add_image(image)

# Check the intensity image's datatype
print(image.dtype)

# Inspect the intensity image values in order to identify a threshold
# that segments both cells
# napari GUI: hover with mouse, line profile

# Threshold the image
binary_image_two_nuclei = image > 5

# Overlay the binary image
viewer.add_image(binary_image_two_nuclei, opacity=0.8)

# Inspect data type
print(binary_image_two_nuclei.dtype)

# Inspect value content
import numpy as np
print(np.unique(binary_image_two_nuclei))

# Apply a higher threshold
# to only select the brighter cell
binary_image_one_nuclei = image > 44
viewer.add_image(binary_image_one_nuclei, opacity=0.8)

# Apply two thresholds 
# to only select the boundary of cells
binary_image_boundary = (image < 5) * (image >= 4)
viewer.add_image(binary_image_boundary, opacity=0.8)
