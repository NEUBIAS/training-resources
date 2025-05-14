# %%
# Median filtering

# %%
# import modules
import napari
import numpy as np
from skimage import filters
from skimage.filters import rank
from skimage.morphology import disk # Structuring element
from OpenIJTIFF import open_ij_tiff

# %%
# Instantiate the napari viewer
viewer = napari.Viewer()

# %%
# Read and view the image
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_noisy_squares_different_size.tif')
viewer.add_image(image)

# %% 
# Compare small median and mean filter
# - Appreciate that the median filter better preserves the edges
median_1 = filters.median(image, disk(1))
viewer.add_image(median_1)
mean_1 = rank.mean(image, disk(1))
viewer.add_image(mean_1)

# %% 
# Compare a larger median and mean filter
# - Appreciate that a median filter eliminates the small square entirely
median_3 = filters.median(image, disk(3))
viewer.add_image(median_3)
mean_3 = rank.mean(image, disk(3))
viewer.add_image(mean_3)


###########  New image: nucleare speckles #############

# %%
# Clear the napari viewer
viewer.layers.clear()

# %%
# Load image
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif')

# %%
# View the image and find the radius of the intra-nuclear speckles
viewer.add_image(image)

# %%
# Remove small intra-nuclear structures 
# - Appreciate that a median filter removes the intra-nuclear speckles while keeping the nuclear shape intact
# - This can be helpful in many ways, e.g. some deep learning nuclear segmentation tools get confused by intra-nuclear speckles
# - Another application is to subtract the filtered image from the original image to only have the speckles; this will be used in the 
#   "local background subtraction" training module
image_without_speckles = filters.median(image, disk(radius=15))
viewer.add_image(image_without_speckles)

# %% 
# Close the viewer (CI test requires this)
viewer.close()