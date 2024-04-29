# %%
# 2D image inspection using skimage and napari

# %%
# Load an image
from OpenIJTIFF import open_ij_tiff
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif"
image, *_ = open_ij_tiff(image_url)

# %%
# Inspect all image pixel values
print(image)

# %%
# Inspect the image dimensions
print(image.shape)

# %%
# Create a napari viewer
from napari.viewer import Viewer
napari_viewer = Viewer()

# %%
# Jupyter notebook exercise:
# Code completion: Type `napari_viewer.` and press `TAB`
# Get help: Type `napari_viewer.add_image` and press `SHIFT-TAB` 

# %%
# Add an image to the napari_viewer
napari_viewer.add_image(image)

# %%
# Pixel value inspection in napari: 
# However with the mouse over the image and observe the pixel indices and values

# %%
# Fetch a pixel value from the background
print(image[4, 8])

# %%
# Fetch a pixel value from within an object
print(image[31, 42])

# %%
# Extract a line of pixel values across the objects
print(image[20,:])

# %% 
# Napari:
# Use the plot profile plugin to inspect a line of pixel values
 
# %%
# Extract one object as a square of pixel values
print(image[7:30,10:26])

# %%
# Compute the image min and max
print(image.min(), image.max())

# %%
# Compute the image histogram
import matplotlib.pyplot as plt
import numpy as np
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1));

# %%
# Napari:
# Alternative loading of data
# Remove the currently shown image
# Drag and drop image from browser onto napari
# Rename the layer to: image

# %%
# Fetch the image data from napari and check its shape
image = napari_viewer.layers['image'].data
print(image.shape)
