# %%
# 2D image inspection using skimage and napari

# %%
# Load an image
from OpenIJTIFF import open_ij_tiff
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif"
image, *_ = open_ij_tiff(image_url)

# %%
# Inspect what the image actually is
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
# Pixel value inspection in napari: 
# However with the mouse over the image and observe the pixel indices and values

# %%
# Fetch single pixel values
print(image[4, 8]) # in the background
print(image[31, 42]) # inside a nucleus

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
# Jupyter: Use TAB to find the min and max functions
print(image.min(), image.max())

# %%
# Compute and show the image histogram
import matplotlib.pyplot as plt
import numpy as np
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1))
plt.show() # instead, we could end the above line with ";"

# %%
# Napari:
# Alternative loading of data
# Remove the currently shown image
# Drag and drop image from browser onto napari
# Rename the layer to: image

# %%
# Fetch the image data from napari and check its shape
image = viewer.layers['image'].data
print(image.shape)

# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')