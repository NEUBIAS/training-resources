# %% 
# Background subtraction using a median filter

# %%
# import modules
import numpy as np
import napari
from OpenIJTIFF import open_ij_tiff
from skimage import filters
from skimage.morphology import disk

# %%
# Instantiate the napari viewer
viewer = napari.Viewer()

# %%
# Read the image
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__some_spots_with_uneven_bg.tif')

# %%
# View the image
# - Appreciate that due to the strong uneven background it is impossible to segment the spots with a simple threshold
viewer.add_image(image)

# %% 
# Compute background image using a large median filter to remove the small foreground objects
background = filters.median(image, disk(15))
viewer.add_image(background)

# %%
# Compute a foreground image by subtracting the background image from the raw image
# - Convert to signed int16, because a subtraction can cause negative values, which we would like to keep
print(image.dtype, image.min(), image.max())
foreground = image.astype('int16') - background.astype('int16')
print(foreground.dtype, foreground.min(), foreground.max())

# %% 
# Add the image to napari and 
# inspect the intensity image values in order to identify a threshold
# that segments the foreground dots
viewer.add_image(foreground)

# %%
# Threshold the foreground image
binary_image_spots = foreground > 8
# Overlay the binary image
viewer.add_image(binary_image_spots)

