# %% [markdown]
# ### Dilation and erosion of binary
#
# Part of teaching module [Morphological filtering](https://neubias.github.io/training-resources/filter_morphological/#dilateerode)

# %%
# Import python packages.
from OpenIJTIFF import open_ij_tiff
from napari.viewer import Viewer
from skimage.morphology import square, disk
from skimage.morphology import erosion, dilation
from skimage.morphology import opening, closing

# Create a napari_viewer and visualize image and labels.
napari_viewer = Viewer()

# %%
# download and read tif file
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__three_spots_different_size.tif"
image, _, _, _ = open_ij_tiff(fpath)

napari_viewer.add_image(image, name='image')

# %% [markdown]
# Perform [erosion](https://scikit-image.org/docs/stable/api/skimage.morphology.html#skimage.morphology.erosion) and [dilation](https://scikit-image.org/docs/stable/api/skimage.morphology.html#skimage.morphology.dilation) using defaults
#

# %%
# Perform erosion and dilation with default structuring element (cross-shaped)
# 0 1 0 
# 1 1 1
# 0 1 0
# This element has connectivity = 1
eroded = erosion(image)
dilated = dilation(image)

# Add to napari
napari_viewer.add_image(eroded, name='eroded1', colormap='magenta', opacity = 0.7)
napari_viewer.add_image(dilated, name='dilated1', colormap = 'green', opacity = 0.7)

# %% [markdown]
# Appreciate that the single pixel disappeared with erosion.\
# Appreciate that the single pixel became a cross with dilation. This is in fact the form of the structuring element

# %%
# Now try with a structuring element with connectivity 2 (3x3 square).
square3 = square(3)
print(square3)
eroded_square3 = erosion(image, footprsquare3)
dilated_square3 = dilation(image, square3)

napari_viewer.add_image(eroded_square3, name='eroded3', colormap='magenta', opacity = 0.5)
napari_viewer.add_image(dilated_square3, name='dilated3', colormap='green', opacity = 0.5)

# %%
# add images to the viewer and inspect the results
napari_viewer.add_image(eroded, name='eroded1')
napari_viewer.add_image(dilated, name='dilated1')
napari_viewer.add_image(eroded_square3, name='eroded3')
napari_viewer.add_image(dilated_square3, name='dilated3')

# %% [markdown]
# **Learning opportunity**\
# Try with a bigger square (e.g. `square(5)`)\
# or a different structuring element (e.g. disk(1))\
# Also refer to https://scikit-image.org/docs/stable/api/skimage.morphology.html

# %%
