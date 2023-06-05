# %% [markdown]
# ## Inspect a 3D time-lapse image

# %%
# Add folder with functions to path
import sys
sys.path.append("/Users/tischer/Documents/training-resources/functions")

# %%
# Load the image
from OpenIJTIFF import open_ij_tiff
image, axes, scales, units = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzt_8bit__starfish_chromosomes.tif")

# %%
# Explore image shape & axes
print("Shape:", image.shape)
print("Axes:", axes)
print("Scales:", scales)
print("Units:", units)

# %%
# View the image
from napari.viewer import Viewer
napari_viewer = Viewer()
napari_viewer.add_image(image, scale = scales)

# %% [markdown]
# **Napari GUI** Explore different axes sliders and values in the bottom left part \
# **Napari GUI** Show in 3D. 
