#######################################################
## To follow along you require additional packages.
## Install them into your activated conda environment.
## conda activate skimage-napari-tutorial
## pip install napari-plot-profile
## pip install matplotlib
#######################################################

# Import python packages.
from skimage.io import imread
from napari.viewer import Viewer
import matplotlib.pyplot as plt
import numpy as np

# Load the image.
# You can also load a local image by providing the path to the file.
image = imread("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif")

# Print the image pixel values.
print(image)

# Top left corner is [y, x] = [0, 0]
print(image[0, 0])

# [y, x] = [1, 0]
print(image[1, 0])

# [y, x] = [0, 2]
print(image[0, 2])

# Create a new napari viewer.
napari_viewer = Viewer()

# Add an image to the napari_viewer.
napari_viewer.add_image(image)

# Get the image data type
print(image.dtype)

# Use numpy.iinfo to get min and max values of a data type.
np.iinfo(image.dtype)

# Use matplotlib to quickly plot a histogram.
plt.hist(image.flatten(), bins=256);
