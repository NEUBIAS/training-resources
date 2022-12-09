from load_from_url import load_from_url
from napari.viewer import Viewer
import numpy as np

# Read the image
image_url = load_from_url('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif')
print(image_url.dims)
image = image_url.data

# Check image type and values
print(image.dtype, np.min(image), np.max(image))

# Create a new napari viewer.
napari_viewer = Viewer()
# View the intensity image as grayscale
napari_viewer.add_image(image, name='image_grayscale', colormap='gray')

# Change brightness and contrast
napari_viewer.layers['image_grayscale'].contrast_limits=(100, 175)
# Napari GUI: explore different contrast limits

# View the intensity image as grayscale
napari_viewer.add_image(image, name='image_grayscale2', colormap='gray')
# Napari GUI: visualize images side by side
# Napari GUI: change brightness and contrast to visualize dim nuclei

# Check available colormap
print(list(napari.utils.colormaps.AVAILABLE_COLORMAPS))
# Change colormap
napari_viewer.add_image(image, name='image_turbo', colormap='turbo')
# Napari GUI: explore the LUTs

# Extract image data from the layers
image_grayscale = napari_viewer.layers['image_grayscale'].data
image_grayscale2 = napari_viewer.layers['image_grayscale2'].data

# Compare raw data
print(image_grayscale[0:5,0:5])
print(image_grayscale2[0:5,0:5])
print((image_grayscale == image_grayscale2).all())