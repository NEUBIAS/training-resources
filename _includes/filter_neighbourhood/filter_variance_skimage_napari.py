# %% 
# Apply variance filters to an EM image to aid foreground background segmentation

# %%
# Import libraries and
# instantiate the napari viewer
import numpy as np
import napari
import matplotlib.pyplot as plt
from OpenIJTIFF import open_ij_tiff
viewer = napari.Viewer()

# %%
# Read the image and add it to napari
# - Try to find an intensity threshold that separates the intracellular region from the bright background
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__em_mitochondria_er.tif')
viewer.add_image(image)

# %% 
# Plot an intensity histogram as another way to find a threshold
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1))

# %%
# Appreciate that a simple threshold does not suffice to distinguish the cytoplasm from the bright background outside the cell
binary_image = image < 230
viewer.add_image(binary_image)

# %% 
# Apply a variance filter to separate the two regions
# - The idea is to make use of the fact that the background had less local intensity variations than the cytoplasm
# - Note that a mean filter might also work here (please try), but we want to learn something new

# %%
# Convert to uint16 to be able to accommodate 
# the square of the unit8 image, which is needed to represent the variance
# - Appreciate that such datatype issues are common applying any kind of "image math"
print(image.dtype)
uint16_image = image.astype(np.uint16)
print(uint16_image.dtype)

# %% 
# View the uint16 image in napari and check whether the datatype conversion changed the pixel values
# - Going from a lower bit-depth to a higher bit-depth should normally not change the values
viewer.add_image(uint16_image)

# %%
# We could not find a function to directly compute the local variance of an image,
# thus we introduce a, very useful, generic approach to compute any kind of local neighborhood
# filter

# import the function
from scipy.ndimage import generic_filter

# define a function that computes one value from an array of data
def local_variance(data):
  value = np.var(data)
  return value

# apply this function locally to image
var_image = generic_filter(uint16_image, function=local_variance, size=11)

# %%
# View the variance filtered the image to napari
# Look for a threshold that separates the cell from the background
viewer.add_image(var_image)

# %%
# Also inspect the histogram to find a threshold
# - It is interesting to compare the histograms of the variance images computed
#   with different filter widths, to see how well there are two populations of intensity values
plt.hist(var_image.flatten(), bins=np.arange(var_image.min(), var_image.max() + 1))
plt.yscale('log')

# %%
# Segment the cellular region by applying a threshold to the variance filtered image
# - It can be interesting to also try some auto-threshold method here
binary_var_image = var_image > 100
viewer.add_image(binary_var_image)
