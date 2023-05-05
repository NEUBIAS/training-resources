# %% [markdown]
# ## Inspect a 3D image XYZ

# %%
from OpenIJTIFF import open_ij_tiff
# Load the image
# You can also load a local image by providing the path to the file
image, axes, scales, units  = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mri_head.tif")

from napari.viewer import Viewer
# Create a new napari viewer.
napari_viewer = Viewer()

# Add an image to the napari_viewer.
napari_viewer.add_image(image)

# %%
# Print image shape
print(image.shape)

# %%
# Print axes IDs
print(axes)

# %% [markdown]
# **Napari GUI** Explore different sliders and values in the bottom left part