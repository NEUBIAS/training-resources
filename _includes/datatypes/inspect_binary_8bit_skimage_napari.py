# %% 
# Open and inspect a binary image 

# %%
# Import libraries and instantiate napari
import napari
import numpy as np
import matplotlib.pyplot as plt
from OpenIJTIFF import open_ij_tiff

viewer = napari.Viewer()

# %%
# Open image and view it
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__h2b.tif')
viewer.add_image(image)

# %% 
# Check the image's datatype and values
# - From the datatype alone we cannot tell that this is a binary image (aka a mask)
# - But the fact that it only has two values suggests that it in fact is a binary image
print(np.iinfo(image.dtype)) 
print("Min:", image.min())
print("Max:", image.max()) 
print(np.unique(image))

# %%
# Convert to a boolean binary image
# - For working with this mask in python it will be probably more convenient to convert it to a boolean type image
# - The issue is that boolean type images cannot be saved as such on disk, because e.g. TIFF does not support this datatype
binary_image = ( image == 255 ) 
print(image.shape, binary_image.shape) # ensure we did not mess up the shape
# np.iinfo is not implemented for bool
print(binary_image.dtype)
print(np.unique(binary_image))
