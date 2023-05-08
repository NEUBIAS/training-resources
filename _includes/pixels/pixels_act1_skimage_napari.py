# %% [markdown]
# ## Inspect a 2D image
# To follow along for the plot profile you require a napari plugin. \
# Install napari-plot-profile in your course activated conda environment.\
# `conda activate skimage-napari-tutorial` \
# `pip install napari-plot-profile` 

# %%
# Load the image
# You can also load a local image by providing the path to the file
from OpenIJTIFF import open_ij_tiff
image, axes, scales, units  = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif")

# %%
# Create a new napari viewer.
from napari.viewer import Viewer
napari_viewer = Viewer()

# %%
# Add an image to the napari_viewer.
napari_viewer.add_image(image)

# %% [markdown]
# Alternative loading of data\
# **Napari GUI** drag and drop image from browser \ 
# rename the layer for convenience \
# `napari_viewer.layers[0].name = 'image'` \     
# Get the data as numpy array \
# `image = napari_viewer.layers['image'].data` 

# %%
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

# %% [markdown]
# **Napari GUI** Explore the napari-plot-profile plugin (optional)

# %%
import numpy as np
# Compute min and max.
print(image.min(), image.max())

# %%
import matplotlib.pyplot as plt
# Use matplotlib to quickly plot a histogram.
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1));

# %%
# Most frequent pixel value (the mode)
from scipy.stats import mode
mode(image, axis = None, keepdims = True)