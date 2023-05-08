# %% [markdown]
# ## Inspect a 3D image + time

# %%
from OpenIJTIFF import open_ij_tiff
# Load the image
# You can also load a local image by providing the path to the file
image, axes, scales, units  = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzt_8bit__starfish_chromosomes.tif")

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
# **Napari GUI** Explore different sliders and values in the bottom left part \
# **Napari GUI** Show in 3D. Note that the scaling are not yet correct. See `spatial calibration` module on how to fix it!

# %%
# Change order of axis (swap T and Z)
napari_viewer.dims.order = (1, 0, 2, 3)

# %%
# Return to the correct order
napari_viewer.dims.order = (0, 1, 2, 3)
