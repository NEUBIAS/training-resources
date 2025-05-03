# %% 
# Check for saturation in a 12 bit image

# %%
# Import libraries and instantiate napari
import napari
import numpy as np
import matplotlib.pyplot as plt
from OpenIJTIFF import open_ij_tiff

# %%
# Open an image and view it in napari
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_12bit__saturated_plant.tif')
viewer = napari.Viewer()
viewer.add_image(image)

# %%
# Napari:
# - Hover with the mouse to look for saturation

# %% 
# Check the image's datatype
print(image.dtype)
print(np.iinfo(image.dtype)) # Useful as it also prints the value range

# %%
# Check for clipping, i.e. pixels values at the limits of the value range
# This is important for many reasons, for example: 
# - Pixel values at the limit of the value range typically cannot be used for intensity quantification 
# - Important algorithms, e.g. for spot detection, do not work well in regions with intensity clipping
print("Min:", image.min()) # Are there any clipped pixels?
print("Max:", image.max()) # Are there any clipped pixels?

# %% 
# Compute the maximal value of various data types,
# and observe that, suspiciously, our image's maximum value 
# matches that of a 12-bit image
print("8 bit max:", 2**8-1)
print("12 bit max:", 2**12-1)
print("16 bit max:", 2**16-1)

# %% 
# Check how many satured pixels we have in the 12 bit image
print("Number of 4095 pixels:", np.sum(image==4095))

# %%
# To double check that this really is a 12 bit image 
# you can try to inspect the image metadata
# - If you open the image in Fiji you can do: Image > Show Info
# - TODO: find out how to do this in python