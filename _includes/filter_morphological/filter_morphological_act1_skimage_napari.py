# %% 
# Dilation and erosion of a binary image

# %%
# Import python packages.
from OpenIJTIFF import open_ij_tiff
from napari.viewer import Viewer
from skimage.morphology import square, disk
from skimage.morphology import erosion, dilation
import numpy as np

# %%
# Create a napari_viewer 
napari_viewer = Viewer()

# %%
# Open and view image
image, *_ = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__three_spots_different_size.tif")
napari_viewer.add_image(image)

# %%
# Check datatype and pixel values 
# - Ensure that this is a binary image
# - Check how the binary values are encoded (could be in principle: true, false, 0, 1, 255)
print(image.dtype)
print(np.unique(image))

# %%
# Perform [erosion](https://scikit-image.org/docs/stable/api/skimage.morphology.html#skimage.morphology.erosion) and [dilation](https://scikit-image.org/docs/stable/api/skimage.morphology.html#skimage.morphology.dilation) using default setting
#

# %%
# Perform erosion and dilation with a cross-shaped / disk(1) structural element
# This element has connectivity = 1
#
print(disk(1))
eroded = erosion(image, footprint = disk(1))
dilated = dilation(image, footprint = disk(1))

# Add images to napari and observe:
# - The single pixel disappeared with erosion
# - The single pixel became a cross with dilation. This is in fact the form of the structuring element
# - For the dilation no pixels have been added (diagonally) at corners, because the disk(1) has only horizontal and vertical "1" connectivity
napari_viewer.add_labels(eroded)
napari_viewer.add_labels(dilated)

# %%
# Now try with a structuring element with connectivity 2 (3x3 square).
print(square(3))
eroded_square3 = erosion(image, footprint = square(3))
dilated_square3 = dilation(image, footprint = square(3))

# %%
# View images in napari
#
napari_viewer.add_labels(eroded_square3)
napari_viewer.add_labels(dilated_square3)

# %%
# Learning opportunity:
# Try with a bigger square (e.g. square(5))
# or a different structuring element (e.g. disk(1))
# Also refer to https://scikit-image.org/docs/stable/api/skimage.morphology.html
