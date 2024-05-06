# %% [markdown]
# ### Morphological internal gradient of binary
# Activity is part of the teaching module [Morphological filtering](https://neubias.github.io/training-resources/filter_morphological/index.html#gradient)

# %%
from OpenIJTIFF import open_ij_tiff
from napari.viewer import Viewer
from skimage.morphology import square, disk
from skimage.morphology import erosion, dilation

# Create a napari_viewer and visualize image and labels.
napari_viewer = Viewer()

# %%
# Explore internal gradient.
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__h2b.tif"
image, _, _, _ = open_ij_tiff(fpath)

# Internal gradient is the difference between the image and the eroded version of it.
eroded = erosion(image)
internal_gradient = image - eroded

# %%
# Create a napari_viewer and visualize images.
napari_viewer.add_image(image)
napari_viewer.add_labels(eroded)
napari_viewer.add_labels(internal_gradient, name='internal_gradient')

# %% [markdown]
# The internal gradient represents the inner edge of the object.\
# Discuss when and how this can be useful.

# %% [markdown]
# **Learning opportunity**
# * Compute the external gradient (dilation - image)
# * Try different sized structuring elements for the dilation
# * What controls the thickness of the edge?
# * Compute the central gradient (dilation - erosion)
