# %%
# Explore a 5D image (3D image + channels + time)

# %%
# Imports
from OpenIJTIFF import open_ij_tiff
from napari.viewer import Viewer
import numpy as np

# %%
# Load the image
image, axes, scales, units = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzct_16bit__metaphase_eb3_cenpa.tif")

# %%
# Print image shape & axes
print("Shape:", image.shape)
print("Axes:", axes)
print("Scales:", scales)
print("Units:", units)

# %%
# Display image in napari
viewer = Viewer()
viewer.add_image(image, scale = scales)

# %%
# Napari GUI: Explore different sliders and values in the bottom left part.
# Napari GUI: Show in 3D. Note that the order of axes is not yet correct.
#             Napari expects that the last 3 dimension are ZYX.
# Napari GUI: Delete image.

# %%
# Remove channel from scale
scales_tzyx = scales.copy()
scales_tzyx.pop(2) # remove channel scale
print("Scales TZCYX: ", scales)
print("Scales TZYX: ", scales_tzyx)

# %%
# Add image as separate channels
viewer.add_image(image[:,:,0,:,:], scale = scales_tzyx, name = 'Ch0', colormap = 'magenta')
viewer.add_image(image[:,:,1,:,:], scale = scales_tzyx, name = 'Ch1', colormap = 'green', blending='additive')

# %%
# Napari GUI: Explore different sliders and values in the bottom left part.
# Napari GUI: delete image and try direct loading.

# %%
# View image as separate channels in one step
viewer.add_image(image, channel_axis = 2, scale = scales_tzyx, name = ['Ch0', 'Ch1'])

# %%
# Napari GUI: delete image.

# %%
# Loading with numpy transpose
image_transpose = np.transpose(image, (2, 0, 1, 3, 4))
scales_transpose = [scales[2],scales[0],scales[1],scales[3],scales[4]]
viewer.add_image(image_transpose, scale = scales_transpose)

# %%
# Napari GUI: Right mouse click on image and `split stack`. This will generate visible two channels.

# %% 
# Close the viewer (CI test requires this)
viewer.close()