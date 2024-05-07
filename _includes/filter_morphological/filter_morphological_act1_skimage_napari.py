# %% 
# Dilation and erosion of a binary image

# %%
# Import python packages.
from OpenIJTIFF import open_ij_tiff
from napari.viewer import Viewer
from skimage.morphology import square, disk
from skimage.morphology import erosion, dilation

# %%
# Create a napari_viewer 
napari_viewer = Viewer()

# %%
# Open and view image
image, *_ = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__three_spots_different_size.tif")
napari_viewer.add_image(image)

# %%
# Check datatype and pixel values to ensure that this is a binary image
print(image.dtype)
print(np.unique(image))

# %%
# Perform [erosion](https://scikit-image.org/docs/stable/api/skimage.morphology.html#skimage.morphology.erosion) and [dilation](https://scikit-image.org/docs/stable/api/skimage.morphology.html#skimage.morphology.dilation) using default setting
#

# %%
# Perform erosion and dilation with default structuring element (cross-shaped - disk(1))
# 0 1 0
# 1 1 1
# 0 1 0
# This element has connectivity = 1
eroded = erosion(image, footprint = disk(1))
dilated = dilation(image, footprint = disk(1))

# Add resulting images to napari
napari_viewer.add_labels(eroded)
napari_viewer.add_labels(dilated)

# %%
# Appreciate that the single pixel disappeared with erosion
# Appreciate that the single pixel became a cross with dilation. This is in fact the form of the structuring element

# %%
# Now try with a structuring element with connectivity 2 (3x3 square).
square3 = square(3)
print(square3)
eroded_square3 = erosion(image, footprint = square3)
dilated_square3 = dilation(image, footprint = square3)

napari_viewer.add_labels(eroded_square3)
napari_viewer.add_labels(dilated_square3)

# %%
# Learning opportunity:
# Try with a bigger square (e.g. `square(5)`)\
# or a different structuring element (e.g. disk(1))\
# Also refer to https://scikit-image.org/docs/stable/api/skimage.morphology.html
