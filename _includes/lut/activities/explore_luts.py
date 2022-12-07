# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# Read the image
from skimage.io import imread
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_calibrated_16bit__nuclear_protein_control.tif')

# Check image type and values
import numpy as np
print(image.dtype, np.min(image), np.max(image))

# View the intensity image as grayscale
viewer.add_image(image, name='image_grayscale', colormap='gray')

# Change brightness and contrast
viewer.layers['image_grayscale'].contrast_limits=(100, 175)

# chaneg colormap
print(list(napari.utils.colormaps.AVAILABLE_COLORMAPS))
viewer.add_image(image, name='image_cyan', colormap='cyan')

# Extract image data from the layers
image_grayscale = viewer.layers['image_grayscale']
image_cyan = viewer.layers['image_cyan']

# Compare raw data
print(image_grayscale.data[:5,:5])
print(image_cyan.data[:5,:5])
print((image_grayscale.data == image_cyan.data).all())

