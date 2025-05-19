# %% 
# Explore image data types and value ranges

# %%
# Import libraries and instantiate napari
import napari
import numpy as np
import matplotlib.pyplot as plt
from OpenIJTIFF import open_ij_tiff

viewer = napari.Viewer()

# %%
# Open an image and view it
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_a.tif')
viewer.add_image(image)

# https://forum.image.sc/t/add-hilo-colormap-to-napari/95601

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
print("Number of 0 pixels:", np.sum(image==0)) # How many clipped pixels are there?
print("Number of 255 pixels:", np.sum(image==255))
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1));


#image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__h2b.tif')
#image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif')
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif')

# View the image
viewer.add_image(image)

# %%
# Check the image's datatype and its value limits
print(np.iinfo(image.dtype))

# Check the image's minimum and maximum intensity
print(np.min(image),np.max(image))

# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')