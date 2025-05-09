# - Create an inspect a LoG kernel
# - Apply it to an image, e.g. for enhancement of spots
# - Show that it is important to choose a good sigma 
#   that matches the spots (or edges) in the image

# %% 
# Thresholding bright and dim cells

# %%
# Instantiate napari
import napari
viewer = napari.Viewer()

# %%
# Load an example image
# Observe that it is quite noisy
from OpenIJTIFF import open_ij_tiff
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__spots_local_background_with_noise.tif'))
viewer.add_image(image)

# %%
# Apply a Laplacian to enhance spots and edges
# Observe that the resulting image is very noisy
from skimage.filters import laplace
laplacian_image = laplace(image)
viewer.add_image(laplacian_image)

# %%
# Apply a Gaussian first to reduce noise 
# and then a Laplacian.
# This is a very common operation, also called 
# "Laplacian of Gaussian (LoG)"
from scipy.ndimage import convolve
from skimage.filters import gaussian
import numpy as np

laplacian_kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

log_image = convolve(gaussian(image), laplacian_kernel)
viewer.add_image(log_image) # still quite noisy

# Let's adapt the Gaussian kernel size to better
# match the size of the structures of interest
log_sigma10_image = convolve(gaussian(image, 10), laplacian_kernel)
viewer.add_image(log_sigma10_image) # better :)





