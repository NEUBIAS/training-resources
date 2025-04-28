# %%
# Multi channel images filtering

# %%
# import modules
import napari
import numpy as np
from skimage import filters
from skimage.filters import rank
from skimage.morphology import disk # Structuring element
from OpenIJTIFF import open_ij_tiff

# %%
# Instantiate the napari viewer
viewer = napari.Viewer()

# %%
# Read and view the image
image, ax_names, ax_scales, ax_units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__cell_dna_mts_actin.tif')

# %%
# Note that channel dimension is a slider 
# If you try to adjust range it behaves like a 3D stack
viewer.add_image(image)

# %%
# The channel dimension is the 0th
print(ax_names)

# %%
viewer.layers.clear()
ch_axis = 0
ch_names = ['DNA', 'MTS', 'ACTIN']
viewer.add_image(image, channel_axis = 0, name = ch_names)
# Now the channels render correctly 

# %%
# play with contrast and brightness sliders and find ranges that matches for your eyes
# play with colormap/LUT and find settings that you like
viewer.layers.clear()
viewer.add_image(image, channel_axis = 0, name = ch_names, contrast_limits=
    [[105, 450], [100, 500], [100,5000]], # contrast limits for each channel
    colormap = ['blue', 'green', 'magenta'], # colormaps for each channel
    blending = ['translucent_no_depth', 'additive', 'additive'] # blending mode
)
# %%
# Try an inverted colormap and use minimum blending 
viewer.layers.clear()
viewer.add_image(image, channel_axis = 0, name = ch_names, contrast_limits=
    [[105, 450], [100, 500], [100,5000]], # contrast limits for each channel
    colormap = ['I Forest', 'I Purple','I Blue'], # colormaps for each channel
    blending = ['translucent_no_depth', 'minimum', 'minimum'] # blending mode
)

