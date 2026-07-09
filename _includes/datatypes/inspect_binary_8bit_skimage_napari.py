# %% 
# Open and inspect a binary image 

# %%
# Import libraries and instantiate napari
import napari
import numpy as np
import matplotlib.pyplot as plt
from bioio import BioImage

viewer = napari.Viewer()

# %%
# Open image and view it
image_object = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__h2b.tif')
image_data = image_object.data.squeeze()
viewer.add_image(image_data)

# %% 
# Check the image's datatype and values
# - From the datatype alone we cannot tell that this is a binary image (aka a mask)
# - But the fact that it only has two values suggests that it in fact is a binary image
print(np.iinfo(image_data.dtype)) 
print("Min:", image_data.min())
print("Max:", image_data.max()) 
print(np.unique(image_data))

# %%
# Convert to a boolean binary image
# - For working with this mask in python it will be probably more convenient to convert it to a boolean type image
# - The issue is that boolean type images cannot be saved as such on disk, because e.g. TIFF does not support this datatype
binary_image = ( image_data == 255 ) 
print(image_data.shape, binary_image.shape) # ensure we did not mess up the shape
# np.iinfo is not implemented for bool
print(binary_image.dtype)
print(np.unique(binary_image))

# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')
# %%
