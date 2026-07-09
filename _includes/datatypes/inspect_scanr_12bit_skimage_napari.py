# %% 
# Explore the pixels values of an image acquired with a 12-bit camera 

# %%
# Import libraries and instantiate napari
import napari
import numpy as np
import matplotlib.pyplot as plt
from bioio import BioImage

viewer = napari.Viewer()

# %%
# Open image and view it
img = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif')
img_data = img.data.squeeze()
viewer.add_image(img_data)

# %% 
# Check the image's datatype and value range
# - The intensity values reside "strangely" in the middle of the 16 bit data type range
print(img_data.dtype) 
dtype_min = np.iinfo(img_data.dtype).min
dtype_max = np.iinfo(img_data.dtype).max
print(dtype_min, dtype_max)

print(img_data.min(), img_data.max())

plt.hist(img_data.flatten(), bins=np.arange(dtype_min, dtype_max+1).tolist())
plt.yscale("log")
plt.show()

# %%
# This is a bit advanced/annoying 
# but here's how to shift the image values to be better interpretable
# and then how to check for saturation
image_rescaled = img_data - 2**15  # remove offset due to misinterpretation of the first bit (signed/unsigned)
print(image_rescaled.min(), image_rescaled.max()) 
print(0, 2**12-1) # print uint12 data range, which is the range of the camera the image was acquired with
print(np.sum(image_rescaled == 2**12-1)) # check number of saturated pixels

# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')