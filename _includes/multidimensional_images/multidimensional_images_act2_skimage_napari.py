# %% [markdown]
# ## Explore a 3D multi-channel image

# %%
# Load the image 
from OpenIJTIFF import open_ij_tiff
image, axes, scales, units = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzc_8bit_beads_p_open.tif")

# %%
# Print image shape & axes
print("Shape:", image.shape)
print("Axes:",axes)
print("Scales:",scales)
print("Units:",units)

# %%
# View the image
from napari.viewer import Viewer
napari_viewer = Viewer()
napari_viewer.add_image(image, scale = scales)

# %% [markdown]
# **Napari GUI** Explore different sliders and values in the bottom left part \
# **Napari GUI** Delete the image

# %%
# Create images as separate channels
# Axes order is ZCYX [0,1,2,3]
scale_3D = [scales[0], scales[2], scales[3]]
print("Scale 3D:\n", scale_3D)

# %%
image_ch0 = image[:,0,:,:]
image_ch1 = image[:,1,:,:]
print(image.shape)
print(image_ch0.shape)
print(image_ch1.shape)

# %%
# View images as separate channels
napari_viewer.add_image(image_ch0, name = 'Ch0_ns', colormap = 'magenta')
napari_viewer.add_image(image_ch1, name = 'Ch1_ns', colormap = 'green', blending='additive')

# %% [markdown]
# **Napari GUI** Explore different blending modes and LUTs
