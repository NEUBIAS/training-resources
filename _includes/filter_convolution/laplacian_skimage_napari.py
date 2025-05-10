
# %%
# Instantiate napari
import napari
viewer = napari.Viewer()

# %%
# Create a Laplacian kernel
from scipy.ndimage import convolve
laplacian_kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
print(laplacian_kernel)

# %%
# Open a test image with the Laplacian kernel
from OpenIJTIFF import open_ij_tiff
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__laplacian_test_input.tif')
viewer.add_image(image)

# %%
# Convolve the test image with the Laplacian kernel
# Try to exactly understand the output for every pixel
from scipy.ndimage import convolve
laplacian_image = convolve(image, laplacian_kernel)
viewer.add_image(laplacian_image)