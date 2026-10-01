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
img_obj = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__h2b.tif')
img = img_obj.data
print(f"Axes order : {img_obj.dims.order}")
print(f"Shape      : {img_obj.dims}")
print(f"Data type  : {img.dtype}")
print(f"Pixel size : {img_obj.physical_pixel_sizes}")
img = img.squeeze()
viewer.add_image(img)

# %% 
# Check the image's datatype and values
# - From the datatype alone we cannot tell that this is a binary image (aka a mask)
# - But the fact that it only has two values suggests that it in fact is a binary image
print(np.iinfo(img.dtype)) 
print("Min:", img.min())
print("Max:", img.max()) 
print(np.unique(img))

# %%
# Convert to a boolean binary image
# - For working with this mask in python it will be probably more convenient to convert it to a boolean type image
# - The issue is that boolean type images cannot be saved as such on disk, because e.g. TIFF does not support this datatype
binary_image = ( img == 255 ) 
print(img.shape, binary_image.shape) # ensure we did not mess up the shape
# np.iinfo is not implemented for bool
print(binary_image.dtype)
print(np.unique(binary_image))

# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')
# %%
