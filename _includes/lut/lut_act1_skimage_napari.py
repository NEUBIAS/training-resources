# %%
# Using different Lookup Tables (LUTs) in napari

# %%
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# %%
# Read an image and its metadata
from OpenIJTIFF import open_ij_tiff
image, *_ = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif")

# %%
# Add the image
viewer.add_image(image)

# %%
# Napari: 
# Right click on "contrast limits" and adjust to see the dim nuclei
# Set "colormap" to "turbo" and change the contrast limits back to 0, 255
# Appreciate the such a multi-color LUT can be useful to see dim and bright objects

# %%
# Programatically show the image several times with different LUT settings 
viewer.layers.clear() # remove all layers
viewer.add_image(image, name="image_turbo", colormap="turbo", contrast_limits=[0,255])
viewer.add_image(image, name="image_gray_1", colormap="gray", contrast_limits=[0,100])
viewer.add_image(image, name="image_gray_2", colormap="gray", contrast_limits=[0,255])
viewer.grid.enabled = True # turn on the grid mode to see the images side by side

# %% 
# Close the viewer (CI test requires this)
viewer.close()