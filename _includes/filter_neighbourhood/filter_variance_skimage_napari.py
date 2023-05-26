# %% [markdown]
# ## Applying variance filters to an image

# %%
# Instantiate the napari viewer
import napari
from OpenIJTIFF import open_ij_tiff
viewer = napari.Viewer()

# %%
# Read the intensity image and add it to napari
image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__em_mitochondria_er.tif')
viewer.add_image(image)

# %%
# Appreciate that one cannot readily segment the sample by a simple intensity threshold
binary_image = image < 230
viewer.add_image(binary_image)

# %% 
# Apply a variance filter 

# Convert to uint16 to be able to accommodate 
# the square of the unit8 image
import numpy as np
print(image.dtype)
uint16_image = image.astype(np.uint16)

# Use ndimage instead of skimage,
# because skimage.filters.rank.mean 
# only works up to unit16, which here specifically
# would have been sufficient. However if the input image 
# would have been uint16 we would have needed unit32
# for the variance.
from scipy import ndimage
sqr_mean_image = ndimage.uniform_filter(uint16_image, (11, 11))**2
mean_sqr_mean = ndimage.uniform_filter(uint16_image**2, (11, 11))
var_image = mean_sqr_mean - sqr_mean_image
viewer.add_image(var_image)

# %%
# Segment the foreground by applying a threshold
# (Note that in this specific case a simple mean filter might have been sufficient
# to achieve the same result, because the sample is on average darker than the background)
binary_var_image = var_image > 100
viewer.add_image(binary_var_image)
