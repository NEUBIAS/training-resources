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
img_obj = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif')
img = img_obj.data
print(f"Axes order : {img_obj.dims.order}")
print(f"Shape      : {img_obj.dims}")
print(f"Data type  : {img.dtype}")
print(f"Pixel size : {img_obj.physical_pixel_sizes}")
img = img.squeeze()
viewer.add_image(img)

# %% 
# Check the image's datatype and value range
# - The intensity values reside "strangely" in the middle of the 16 bit data type range
print(img.dtype) 
dtype_min = np.iinfo(img.dtype).min
dtype_max = np.iinfo(img.dtype).max
print(dtype_min, dtype_max)

print(img.min(), img.max())

plt.hist(img.flatten(), bins=np.arange(dtype_min, dtype_max+1).tolist())
plt.yscale("log")
plt.show()

# %%
# This is a bit advanced/annoying 
# but here's how to shift the image values to be better interpretable
# and then how to check for saturation
image_rescaled = img - 2**15  # remove offset due to misinterpretation of the first bit (signed/unsigned)
print(image_rescaled.min(), image_rescaled.max()) 
print(0, 2**12-1) # print uint12 data range, which is the range of the camera the image was acquired with
print(np.sum(image_rescaled == 2**12-1)) # check number of saturated pixels

# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')
# %%
