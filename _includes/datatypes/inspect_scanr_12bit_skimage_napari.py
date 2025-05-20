# %% 
# Explore the pixels values of an image acquired with a 12-bit camera 

# %%
# Import libraries and instantiate napari
import napari
import numpy as np
import matplotlib.pyplot as plt
from OpenIJTIFF import open_ij_tiff

viewer = napari.Viewer()

# %%
# Open image and view it
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif')
viewer.add_image(image)

# %% 
# Check the image's datatype and value range
# - The intensity values reside "strangely" in the middle of the 16 bit data type range
print(image.dtype) 
dtype_min = np.iinfo(image.dtype).min
dtype_max = np.iinfo(image.dtype).max
print(dtype_min, dtype_max)

print(image.min(), image.max())

plt.hist(image.flatten(), bins=np.arange(dtype_min, dtype_max+1))
plt.yscale("log")

# %%
# This is a bit advanced/annoying 
# but here's how to shift the image values to be better interpretable
# and then how to check for saturation
image_rescaled = image - 2**15  # remove offset due to misinterpretation of the first bit (signed/unsigned)
print(image_rescaled.min(), image_rescaled.max()) 
print(0, 2**12-1) # print uint12 data range, which is the range of the camera the image was acquired with
print(np.sum(image_rescaled == 2**12-1)) # check number of saturated pixels

# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')