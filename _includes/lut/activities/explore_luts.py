# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# Read the image
from skimage.io import imread
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif')

# Check image type and values
import numpy as np
print(image.dtype, np.min(image), np.max(image))

# View the intensity image as grayscale
viewer.add_image(image, name='image_grayscale', colormap='gray')

# Change brightness and contrast
viewer.layers['image_grayscale'].contrast_limits=(100, 175)
# Napari GUI: explore different contrast limits

# Check available colormap
print(list(napari.utils.colormaps.AVAILABLE_COLORMAPS))
# Change colormap
viewer.add_image(image, name='image_turbo', colormap='turbo')
# Napari GUI: visualize images in grid mode and explore the LUTs

# Extract image data from the layers
image_grayscale = viewer.layers['image_grayscale'].data
image_turbo = viewer.layers['image_turbo'].data

# Compare raw data
print(image_grayscale[0:5,0:5])
print(image_turbo[0:5,0:5])
print((image_grayscale == image_turbo).all())
