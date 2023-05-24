# %% [markdown]
# ## Explore dimensions in a 5D image (3D image + channels + time)

# %%
from OpenIJTIFF import open_ij_tiff
# Load the image
# You can also load a local image by providing the path to the file
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzct_8bit_blobs.tif"
image, axes, scales, units  = open_ij_tiff(fpath)

# %%
# Print image shape
print(image.shape)

# %%
# Print axes IDs
print(axes)

# %%
# Print scales
print(scales)

# %%
# Display image in napari
from napari.viewer import Viewer
# Create a new napari viewer.
napari_viewer = Viewer()

# Add an image to the napari_viewer.
napari_viewer.add_image(image)

# %% [markdown]
# **Napari GUI** Explore different sliders and values in the bottom left part \
# **Napari GUI** Show in 3D. Note that the order of axes is not yet correct. Napari expects that the last 3 dimension are ZYX\
# **Napari GUI** Delete image 
#

# %%
# Load image with correct channel order
napari_viewer.add_image(image[:,:,0,:,:],  name = 'Ch1', colormap = 'magenta')
napari_viewer.add_image(image[:,:,1,:,:],  name = 'Ch2', colormap = 'green', blending='additive')

# %% [markdown]
# **Napari GUI** Explore different sliders and values in the bottom left part \
# **Napari GUI** delete image and try direct loading


# %%
# Load image with correct channel axes in one step
napari_viewer.add_image(image, channel_axis = 2, name = ['Ch1', 'Ch2'])

# %% [markdown]
# **Napari GUI** delete image 

# %%
# Loading with numpy transpose
import numpy as np
image_transpose = np.transpose(image, (2, 0, 1, 3, 4))
napari_viewer.add_image(image_transpose)


# %% [markdown]
# **Napari GUI** Right mouse click on image and `split track`. This will generate visible two channels
