#######################################################
## To follow along you require additional packages.
## Install them into your activated conda environment.
## conda activate skimage-napari-tutorial
## pip install napari-plot-profile
#######################################################

from load_from_url import load_from_url

# Load the image.
# You can also load a local image by providing the path to the file.
image_url = load_from_url("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif")
print(image_url.dims)

image = image_url.data

# Print image shape
print(image.shape)

# Print the image pixel values.
print(image)

# Top left corner is [y, x] = [r, c] = [0, 0]
print(image[0, 0, 0, 0, 0])

# [y, x] = [r, c] = [1, 0]
print(image[0, 0, 0, 1, 0])

# [y, x] = [r, c] = [0, 2]
print(image[0, 0, 0, 0, 2])

from napari.viewer import Viewer
# Create a new napari viewer.
napari_viewer = Viewer()

# Add an image to the napari_viewer.
napari_viewer.add_image(image)

# Explore the napari-plot-profile plugin.

import numpy as np
# Compute min and max.
print(image.min(), image.max())

import matplotlib.pyplot as plt
# Use matplotlib to quickly plot a histogram.
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1));
