# %% 
# Inspect and visualise an RBG images

# %%
# Import libraries and instantiate napari
import napari
import numpy as np
from skimage import io # OpenIJTiff cannot open RGB images

viewer = napari.Viewer()

# %%
# Open and inspect the image 
image = io.imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_rgb__cells.tif')
print(image.dtype) # The datatype is uint8 (not rgb)
print(image.shape) # The RGB components are represented as a third dimension

# %%
# View the image

# By default, if the last dimension of an image is of size 3 or 4, 
# napari will interpret the image as an RGB or RGBA image
viewer.add_image(image) 

# If you don't want to treat it as RGB 
# you have to set rgb=False
viewer.add_image(image, rgb=False) 

# After opening the image, use the napari UI 
# to change the axes order such that you can see the image
# There's now a slider below the image to change which color component
# of the RGB image you are looking at

# %% 
# Close the viewer (CI test requires this)
viewer.close()