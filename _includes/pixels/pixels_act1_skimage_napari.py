# %%
# 2D image inspection using skimage and napari

# %%
# Load an image
from bioio import BioImage
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif"
img_obj = BioImage(image_url)
img = img_obj.data.squeeze()

# %%
# Inspect what the image actually is
# - numpy arrays are generally used in python to represent arrays of numbers
print(type(img))

# %%
# Inspect the pixel values
print(img)

# %%
# Inspect the image dimensions
print(img.shape)

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
viewer.add_image(img)

# %%
# Napari: 
# However with the mouse over the image and observe the pixel indices and values

# %%
# Fetch single pixel values
print(img[4, 8]) # in the background
print(img[31, 42]) # inside a nucleus

# %%
# Extract a line of pixel values across the objects
# Observe how the pixel values go: low(bg) .. high(nucleus) .. low(bg) .. high(nucleus)
line = img[20,:]
print(line.shape)
print(line) 

# %%
# Napari:
# Identify the boundaries (top left, bottom right) of a region of one nucleus
# Remember those numbers and use them below

# %%
# Extract the pixel values of one object using the above manually found coordinates
crop = img[7:30,10:26]
print(crop.shape)
print(crop)

# %%
# Compute the image min and max
# Jupyter: Use TAB to find the min and max functions
print(img.min(), img.max())

# %%
# Get a handle on the image array from napari 
# and check whether it is the same that we originally added
image_from_napari = viewer.layers['img'].data
import numpy as np
print(np.array_equal(image_from_napari, img)) # the two images have identical entries
print(image_from_napari is img) # they are even the same object, not just a copy

# %%
# Compute and show the image histogram
# (there's many things happening here, no need to understand everything right now)
import matplotlib.pyplot as plt
plt.hist(img.flatten(), bins='auto')
plt.show()

# %% 
# Close (CI test requires this)
viewer.close()
plt.close('all')
