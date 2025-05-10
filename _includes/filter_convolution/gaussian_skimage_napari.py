import numpy as np
from skimage.filters import gaussian
from scipy.ndimage import convolve
import matplotlib.pyplot as plt

# %%
# Create a delta peak image 
size = 5
image = np.zeros((size, size))
image[size // 2, size // 2] = 1
print(image)

# %%
# Apply a Gaussian blur to the delta image
# in order to see the Gaussian convolution kernel
sigma = 1
kernel = gaussian(image, sigma=sigma)
print(np.round(kernel, 2))

# %%
# Instantiate napari
import napari
viewer = napari.Viewer()

# %%
# Load an example image
# Observe that it is quite noisy
from OpenIJTIFF import open_ij_tiff
image, *_ = open_ij_tiff('/Users/tischer/Documents/training-resources/image_data/xy_8bit__spots_local_background_with_noise.tif')
#image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__spots_local_background_with_noise.tif')
viewer.add_image(image)

# %%
# Use the Gaussian kernel to convolve the image
gaussian_image = convolve(image, kernel)
viewer.add_image(gaussian_image)
print(image.dtype, gaussian_image.dtype)

