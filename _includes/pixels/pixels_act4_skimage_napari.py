# %% [markdown]
# ## Inspect a 3D image + time + multiple channels

# %%
from OpenIJTIFF import open_ij_tiff
# Load the image
# You can also load a local image by providing the path to the file
image, axes, scales, units  = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzct_16bit__mitosis.tif")

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
# **Napari GUI** Show in 3D. Note that the order of axes is not yet correct

# %%
# Load image with correct channel order
napari_viewer.add_image(image[:,:,0,:,:],  name = 'dna', colormap = 'magenta')
napari_viewer.add_image(image[:,:,1,:,:],  name = 'microtubules', colormap = 'green', blending='additive')

# %% [markdown]
# **Napari GUI** Explore different sliders and values in the bottom left part \
# **Napari GUI** Correct axes. Scaling in 3D is not yet correct see `spatial calibration` module


# %%
# Load image with correct channel axes in one step
napari_viewer.add_image(image, channel_axis = 2, name = ['dna', 'microtubules'])
