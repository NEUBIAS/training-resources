# %% [markdown]
# ### Background subtraction using a median filter
# From teaching module [Local background correction](https://neubias.github.io/training-resources/local_background_correction/index.html#bgmedian)

# %%
import numpy as np

# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# Read the intensity image
from OpenIJTIFF import open_ij_tiff
image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__some_spots_with_uneven_bg.tif')

# View the intensity image
viewer.add_image(image, name='original image')

# Inspect image data type and values
print('image type:', image.dtype,'\n',
      'image shape:', image.shape,'\n',
      'intensity min:',   np.min(image),'\n',
      'intensity max:',   np.max(image),'\n'
      )

# %% [markdown]
# Compute background image with the median filter from skimage
# %%
from skimage import filters
from skimage.morphology import disk

# Median filtering with radius 15
# Structuring element - aka footprint is disk
background = filters.median(image, disk(15))
viewer.add_image(background, name='background')

# %% [markdown]
# Compute a foreground image by subtracting the background image from the raw image

# %%
# Convert/cast to signed int16 and subtract. 
# A subtraction can cause negative values and we would like to keep these values
foreground = image.astype('int16') - background.astype('int16')
viewer.add_image(foreground, name='foreground')

# %% [markdown]
# **Napari GUI** \
# Inspect the intensity image values in order to identify a threshold
# that segments cells \
# Hover with mouse, line profile

# %%
# Threshold the image
binary_image_cells = foreground > 8
# Overlay the binary image
viewer.add_image(binary_image_cells, name='segmented image')


# %% [markdown]
# ### Learning opportunity: Effect of radius on local background subtraction
# Modify radius of median filter and compute a new foreground image\
# For example try a radius of 3 and of 50\
# Discuss the different results
