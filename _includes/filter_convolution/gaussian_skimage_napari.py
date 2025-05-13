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
# Apply a Gaussian blur with sigma 1 to the delta peak image
# in order to see the values of the Gaussian convolution kernel
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
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__spots_local_background_with_noise.tif')
viewer.add_image(image)

# %%
# Use the Gaussian kernel to convolve the image
# - Observe that the smoothing did not really work for this image
# - Observe that the output of the convolve function has differnt datatype than the input
gaussian_image = convolve(image, kernel)
viewer.add_image(gaussian_image)
print(image.dtype, gaussian_image.dtype)  

# %%
# Use a Gaussian kernel with a larger sigma 
# to better smooth the image.
# This time, for simplicity, 
# we directly use the gaussian function.
gaussian_sigma7_image = gaussian(image, sigma=7)
viewer.add_image(gaussian_sigma7_image)

# %%
# Learning opportunities
# - Inspect the values of the gaussian kernel with sigma 7,
#   using again the trick to apply it to a delta peak image 

# %% 
# Close the viewer (CI test requires this)
viewer.close()