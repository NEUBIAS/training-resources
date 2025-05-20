# %%
# 2D image inspection using skimage and napari

# %%
# Load an image
from OpenIJTIFF import open_ij_tiff
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif"
image, *_ = open_ij_tiff(image_url)

# %%
# Inspect what the image actually is
# - numpy arrays are generally used in python to represent arrays of numbers
print(type(image))

# %%
# Inspect the pixel values
print(image)

# %%
# Inspect the image dimensions
print(image.shape)

# %%
# Create a napari viewer for looking at the image
from napari.viewer import Viewer
viewer = Viewer()

# %%
# Jupyter notebook exercise:
# Code completion: Type `napari_viewer.` and press `TAB`
# Get help: Type `napari_viewer.add_image` and press `SHIFT-TAB` 

# %%
# Add the image the viewer 
viewer.add_image(image)

# %%
# Napari: 
# However with the mouse over the image and observe the pixel indices and values

# %%
# Fetch single pixel values
print(image[4, 8]) # in the background
print(image[31, 42]) # inside a nucleus

# %%
# Extract a line of pixel values across the objects
# Observe how the pixel values go: low(bg) .. high(nucleus) .. low(bg) .. high(nucleus)
print(image[20,:])

# %%
# Napari:
# Identify the boundaries (top left, bottom right) of a region of one nucleus
# Remember those numbers and use them below

# %%
# Extract the pixel values of one object using the above manually found coordinates
print(image[7:30,10:26])

# %%
# Compute the image min and max
# Jupyter: Use TAB to find the min and max functions
print(image.min(), image.max())

# %%
# Get a handle on the image array from napari 
# and check whether it is the same that we originally added
image_from_napari = viewer.layers['image'].data
print(image_from_napari is image) # it is the same object, not just a copy

# %% 
# Close the viewer (CI test requires this)
viewer.close()

# %%
# Compute and show the image histogram
# (there's many things happening here, no need to understand everything right now)
import matplotlib.pyplot as plt
import numpy as np
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1))
plt.show() # instead, we could end the above line with ";"