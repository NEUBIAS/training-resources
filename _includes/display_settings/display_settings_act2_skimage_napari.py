# %% 
# Show two images with the same LUT settings

# %%
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# %%
# Read the images
from OpenIJTIFF import open_ij_tiff
image_control, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_calibrated_16bit__nuclear_protein_control.tif')
image_treated, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_calibrated_16bit__nuclear_protein_treated.tif')

# %% 
# View the image as grayscale
viewer.add_image(image_control, name='control', colormap='gray')
viewer.add_image(image_treated, name='treated', colormap='gray')

# %%
# Napari: Toggle grid mode on to the see images side by side 
# Napari: Check the contrast limits for the two images

# %%
# Check the contrast limits programatically
print(viewer.layers['control'].contrast_limits)
print(viewer.layers['treated'].contrast_limits)

# %% 
# Apply the same contrast to both images
viewer.layers['control'].contrast_limits=(0, 2500)
viewer.layers['treated'].contrast_limits=(0, 2500)

# %% 
# Close the viewer (CI test requires this)
viewer.close()