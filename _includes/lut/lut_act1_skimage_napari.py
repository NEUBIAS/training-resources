# %%
# Using different Lookup Tables (LUTs) in napari

# %%
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# %%
# Read an image and its metadata
from OpenIJTIFF import open_ij_tiff
image, axes, scales, units = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif")

# %%
# View the intensity image as grayscale
viewer.add_image(image, name='image_grayscale', colormap='gray')

# %%
# Change contrast programatically
# Jupyter: Use TAB to to practice auto-completion when entering below command
viewer.layers['image_grayscale'].contrast_limits=(100, 175)

# %%
# Napari: Change the contrast in the GUI
# Napari: Right click on "contrast limits" to see the value range 

# %%
# Add the image a second time
viewer.add_image(image, name='image_grayscale2', colormap='gray')

# %%
# Napari: Visualize images side by side by toggling on the "Grid mode"
# Napari: Change contrast in one image to see the dim nuclei

# %%
# Extract image data from the layers
image_grayscale = viewer.layers['image_grayscale'].data
image_grayscale2 = viewer.layers['image_grayscale2'].data

# %%
# Check that changing the LUT did not change the data
print(image_grayscale[0:5,0:5])
print(image_grayscale2[0:5,0:5])

# %%
# Check whether all pixels of the two images are identical
print((image_grayscale == image_grayscale2).all())

# %%
# Check available LUTs (colormaps)
print(list(napari.utils.colormaps.AVAILABLE_COLORMAPS))

# %%
# Add the image again with a multi-color LUT
viewer.add_image(image, name='image_turbo', colormap='turbo')

# %% 
# Napari: Explore different LUTs using the GUI
