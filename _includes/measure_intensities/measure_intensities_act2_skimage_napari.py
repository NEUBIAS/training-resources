# %% [markdown]
# ### Difficult quantification
# %%
# Import python packages.
from OpenIJTIFF import open_ij_tiff, save_ij_tiff
from skimage.io import imsave
import numpy as np
from napari.viewer import Viewer
import pandas as pd
from skimage.measure import regionprops_table

# %%
# load image from url
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__embryo_transmission_fluorescence.tif"
image, axes_image, voxel_image, units_image = open_ij_tiff(fpath)
print(axes_image)
print(voxel_image)

# Create a napari_viewer and visualize image and labels
viewer = Viewer()
viewer.add_image(image[0], name='brightfield')
viewer.add_image(image[1], name='fluo', colormap='magenta', opacity=0.5)

# %% 
# Close the viewer (CI test requires this)
viewer.close()
