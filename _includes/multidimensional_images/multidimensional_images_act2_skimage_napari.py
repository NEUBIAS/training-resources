# %% [markdown]
# ## Explore dimensions in a 4D image (3D + channels)

# %%
from OpenIJTIFF import open_ij_tiff
# Load the image
# You can also load a local image by providing the path to the file
image, axes, scales, units  = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif")

from napari.viewer import Viewer
# Create a new napari viewer.
napari_viewer = Viewer()

# %%
# Print image shape
print(image.shape)

# %%
# Print axes IDs
print(axes)

# %%
# Print scaling
print(scales)

# %%
# Add an image to the napari_viewer.
napari_viewer.add_image(image, scale = scales)

# %% [markdown]
# **Napari GUI** Explore different sliders and values in the bottom left part \
# **Napari GUI** Show in 3D. Realize that Z and C axis are swapped
# **Napari GUI** Delete the image

# %%
# Load image with correct channel order
scale_3D = [scales[0], scales[2], scales[3]] # We have one dimension less
napari_viewer.add_image(image[:,0,:,:],  name = 'Ch1', colormap = 'magenta', scale = scale_3D)
napari_viewer.add_image(image[:,1,:,:],  name = 'Ch2', colormap = 'green', blending='additive', scale = scale_3D)
