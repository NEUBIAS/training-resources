
# %%
# Instantiate napari
import napari
viewer = napari.Viewer()

# %%
# Create a Laplacian kernel
from scipy.ndimage import convolve
import numpy as np
laplacian_kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
print(laplacian_kernel)

# %%
# Open a test input image 
from OpenIJTIFF import open_ij_tiff
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__laplacian_test_input.tif')
viewer.add_image(image)

# %%
# Pick a few (three) interesting locations in the image
# and manually compute the response to the
# Laplacian Kernel.
# Note down the results to compare with the below
# automated analysis.

# %%
# Convolve the test image with the Laplacian kernel
# Try to exactly understand the output for every pixel
from scipy.ndimage import convolve
laplacian_image = convolve(image, laplacian_kernel)
viewer.add_image(laplacian_image)

# %% 
# Close the viewer (CI test requires this)
viewer.close()