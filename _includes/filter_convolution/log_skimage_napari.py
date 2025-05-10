# %%
# This script demonstrates how to apply a Laplacian of Gaussian
# edge enhancing filter to an image

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
# Apply a Laplacian to enhance spots and edges
# Observe that the resulting image is very noisy
from skimage.filters import laplace
laplacian_image = laplace(image)
viewer.add_image(laplacian_image)

# %%
# To reduce the noise first apply a Gaussian 
# and then the Laplacian.
# This is a very common operation, also called 
# "Laplacian of Gaussian (LoG)"
# Visually inspect the image to determinte
# a sigma for the Gaussian kernel that 
# matches the size of the structures 
# that you want to enhance.
gaussian_sigma = 7 
log_sigma10_image = convolve(gaussian(image, gaussian_sigma), laplacian_kernel)
viewer.add_image(log_sigma10_image)

# %%
# Learning opportunities:
# - Explore how different values for the gaussian_sigma change the result