# %% [markdown]
# ## Explore a 3D multi-channel image

# %%
# Load the image 
from OpenIJTIFF import open_ij_tiff
image, axes, scales, units  = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif")

# %%
# Print image shape & axes
print("Shape:", image.shape)
print("Axes:",axes)
print("Scales:",scales)
print("Units:",units)

# %%
# View the image with its scales
from napari.viewer import Viewer
napari_viewer = Viewer()
napari_viewer.add_image(image, scale = scales)

# %% [markdown]
# **Napari GUI** Explore different sliders and values in the bottom left part \
# **Napari GUI** Delete the image
 
# %%
# View image as separate channels
scale_3D = [scales[0], scales[2], scales[3]] # We have one dimension less
napari_viewer.add_image(image[:,0,:,:],  name = 'Ch1', colormap = 'magenta', scale = scale_3D)
napari_viewer.add_image(image[:,1,:,:],  name = 'Ch2', colormap = 'green', blending='additive', scale = scale_3D)
