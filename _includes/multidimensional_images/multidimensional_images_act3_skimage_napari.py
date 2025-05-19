# %%
# Inspect a 3D time-lapse image

# %%
# Imports
from OpenIJTIFF import open_ij_tiff
from napari.viewer import Viewer

# %%
# Load the image
image, axes, scales, units = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyzt_8bit__starfish_chromosomes.tif")

# %%
# Explore image shape & axes
print("Shape:", image.shape)
print("Axes:", axes)
print("Scales:", scales)
print("Units:", units)

# %%
# View the image
viewer = Viewer()
viewer.add_image(image, scale = scales)

# %%
# Napari GUI: Explore different axes sliders and values in the bottom left part.
# Napari GUI: Show in 3D.

# %% 
# Close the viewer (CI test requires this)
viewer.close()