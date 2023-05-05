#######################################################
## To follow along you require a napari plugin.
## Install napari-plot-profile in your course activated conda environment.
## conda activate skimage-napari-tutorial
## pip install napari-plot-profile
#######################################################

from OpenIJTIFF import open_ij_tiff
# Load the image
# You can also load a local image by providing the path to the file
image, axes, scales, units  = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif")

from napari.viewer import Viewer
# Create a new napari viewer.
napari_viewer = Viewer()

# Add an image to the napari_viewer.
napari_viewer.add_image(image)

# Napari GUI:  drag and drop and rename the layer (alternative for loading data)
# napari_viewer.layers[0].name = 'image'     #Change name of layer for convenience
# image = napari_viewer.layers['image'].data #Get the data as numpy array

# Print image shape
print(image.shape)

# Print the image pixel values.
print(image)

# Top left corner is [y, x] = [r, c] = [0, 0]
print(image[0, 0])

# [y, x] = [r, c] = [1, 0]
print(image[1, 0])

# [y, x] = [r, c] = [0, 2]
print(image[0, 2])

# Explore the napari-plot-profile plugin (optional)

import numpy as np
# Compute min and max.
print(image.min(), image.max())

import matplotlib.pyplot as plt
# Use matplotlib to quickly plot a histogram.
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1));

# Most frequent pixel value (the mode)
from scipy.stats import mode
mode(image, axis = None, keepdims = True)