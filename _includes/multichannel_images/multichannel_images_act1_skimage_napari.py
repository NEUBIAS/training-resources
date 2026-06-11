# %%
# Display a multichannel image

# %%
# import modules
import napari
import numpy as np
from skimage import filters
from skimage.filters import rank
from skimage.morphology import disk # Structuring element
# from OpenIJTIFF import open_ij_tiff
from bioio import BioImage

# %%
# Instantiate the napari viewer
viewer = napari.Viewer()

# %%
# Read the image
#image, ax_names, ax_scales, ax_units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__cell_dna_mts_actin.tif')
img = BioImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__cell_dna_mts_actin.tif")
image = img.get_image_data()

# Open Napari Viewer
viewer = napari.Viewer()

# %%
# View the image
viewer.add_image(image)
# Note that channel dimension is a slider
# If you try to adjust range it behaves like a 3D stack

# %%
# Print the order of image dimensions
print(img.dims.order)

# Print the names of channels
print(img.channel_names)
# NOTE: The channel names have not been saved in the metadata.
# Therefore, we will name channels manually
ch_names = ['DNA', 'MTS', 'ACTIN']


# %%
viewer.layers.clear()
# Find the channel axis index automatically
ch_axis = img.dims.order.find("C")
viewer.add_image(image, channel_axis = ch_axis, name = ch_names)

# Add bounding boxes and colorbars for each channel
viewer.layers['DNA'].bounding_box.visible = True
viewer.layers['DNA'].colorbar.visible = True
viewer.layers['MTS'].bounding_box.visible = True
viewer.layers['MTS'].colorbar.visible = True
viewer.layers['ACTIN'].bounding_box.visible = True
viewer.layers['ACTIN'].colorbar.visible = True

# Now the channels render correctly

# %%
# play with contrast and brightness sliders and find ranges that matches for your eyes
# play with colormap/LUT and find settings that you like
viewer.layers.clear()
viewer.add_image(image, channel_axis = ch_axis, name = ch_names, contrast_limits=
    [[105, 450], [100, 500], [100,5000]], # contrast limits for each channel
    colormap = ['blue', 'green', 'magenta'], # colormaps for each channel
    blending = ['translucent_no_depth', 'additive', 'additive'] # blending mode
)
viewer.layers['DNA'].bounding_box.visible = True
viewer.layers['DNA'].colorbar.visible = True
viewer.layers['MTS'].bounding_box.visible = True
viewer.layers['MTS'].colorbar.visible = True
viewer.layers['ACTIN'].bounding_box.visible = True
viewer.layers['ACTIN'].colorbar.visible = True

# %%
# Try an inverted colormap and use minimum blending
viewer.layers.clear()
viewer.add_image(image, channel_axis = ch_axis, name = ch_names, contrast_limits=
    [[105, 450], [100, 500], [100,5000]], # contrast limits for each channel
    colormap = ['I Forest', 'I Purple','I Blue'], # colormaps for each channel
    blending = ['translucent_no_depth', 'minimum', 'minimum'] # blending mode
)
viewer.layers['DNA'].bounding_box.visible = True
viewer.layers['DNA'].colorbar.visible = True
viewer.layers['MTS'].bounding_box.visible = True
viewer.layers['MTS'].colorbar.visible = True
viewer.layers['ACTIN'].bounding_box.visible = True
viewer.layers['ACTIN'].colorbar.visible = True

# %%
# Close the viewer (CI test requires this)
viewer.close()
