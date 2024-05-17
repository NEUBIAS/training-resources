# %% 
# Detect saturated pixels in an uint8 image

# %%
# Import libraries and instantiate napari
import napari
import numpy as np
import matplotlib.pyplot as plt
from OpenIJTIFF import open_ij_tiff

viewer = napari.Viewer()

# %%
# Open image and view it
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_a.tif')
viewer.add_image(image)

# TODO: https://forum.image.sc/t/add-hilo-colormap-to-napari/95601

# %% 
# Check the image's datatype, possible value range, and used value range
print(image.dtype)
print(np.iinfo(image.dtype)) # Useful as it also prints the value range
print("Min:", image.min())
print("Max:", image.max()) 

# %%
# Check for clipping, i.e. pixels values at the limits of the value range
# This is important for many reasons: 
# - Pixel values at the limit of the value range typically cannot be used for intensity quantification 
# - Spot detection algorithms may not work well in regions with saturated values 
# - Automated thresholding algorithsm may not work well if the background is just plain zeros (it is better to have some noise there)
print("Number of 0 pixels:", np.sum(image==0)) # How many pixels are plain zeros?
print("Number of 255 pixels:", np.sum(image==255)) # How many pixels are saturated?
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1));

