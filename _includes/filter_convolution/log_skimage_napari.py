# %%
# This script demonstrates how to apply a Laplacian of Gaussian
# edge enhancing filter to an image

import napari
from OpenIJTIFF import open_ij_tiff
from skimage.filters import laplace, gaussian

# %%
# Instantiate napari
viewer = napari.Viewer()

# %%
# Load an example image
# Observe that it is quite noisy
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__spots_local_background_with_noise.tif')
viewer.add_image(image)

# %%
# Apply a Laplacian to enhance spots and edges
# Observe that the resulting image is very noisy
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
log_image = laplace(gaussian(image, gaussian_sigma))
viewer.add_image(log_image)

# %%
# Learning opportunities:
# - Explore how different values for the gaussian_sigma change the result

# %% 
# Close the viewer (CI test requires this)
viewer.close()