# %%
# Save a multichannel image

# %%
# Initial imports
import numpy as np
from skimage import filters
from skimage.filters import rank
from skimage.morphology import disk # Structuring element
from OpenIJTIFF import open_ij_tiff
import napari
# %%
# Instantiate the napari viewer
viewer = napari.Viewer()

# %%
# Load the image and check axis names
image, ax_names, ax_scales, ax_units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__cell_dna_mts_actin.tif')
print(f"axis names {ax_names}")

# %%
# Display the image
viewer.layers.clear()
ch_axis = 0
ch_names = ['DNA', 'MTS', 'ACTIN']
viewer.layers.clear()
viewer.add_image(image, channel_axis = ch_axis, name = ch_names, contrast_limits=
    [[105, 450], [100, 500], [100,5000]], # contrast limits for each channel
    colormap = ['blue', 'green', 'magenta'], # colormaps for each channel
    blending = ['translucent_no_depth', 'additive', 'additive'] # blending mode
)

viewer.grid.enabled = False # Make sure we are not in grid mode

# %%
# Export image composite image
export_path = './' # Change it as needed
composite = viewer.export_figure(export_path + 'composite.png', scale_factor = 1) # 1 ~ full dimension of image


# %%
# Shape checks
print(f'original image shape {image.shape} type {image.dtype}') 
print(f'composite image shape {composite.shape} type {composite.dtype}') 
# Note the change of dimension order and type
# The image we save is a RGB image 
# The XYC, where the channels are Red, Green, Blue and Transparency


# %%
# Advanced 
# Create a montage with the 3 channels and the composite
viewer.layers.clear()
viewer.layers.clear()
viewer.add_image(image, channel_axis = ch_axis, name = ch_names, contrast_limits=
    [[105, 450], [100, 500], [100,5000]], # contrast limits for each channel
    colormap = ['gray', 'gray', 'gray'], # colormaps for each channel
    blending = ['translucent_no_depth', 'translucent_no_depth', 'translucent_no_depth'] # blending mode
)
viewer.add_image(composite)
viewer.grid.enabled = True
viewer.grid.stride = -1 # ensure order of images Ch1, Ch2, Ch3
viewer.grid.shape = (1,4)
viewer.reset_view()


# %%
# Export the image
composite_montage = viewer.export_figure(export_path + 'composite_montage.png', scale_factor = 1) 
print(composite_montage.shape)
# Obtained shape is (350,350,4)
# Expected shape should be ~ (350*4, 350, 4)
# Note that as for version Napari 0.5.6 the output size as the same XY shape as the original image. 
# This is a bug and should hopefuly be fixed


# %%
# Alternative make a montage using matplotlib
import matplotlib.pyplot as plt
nC = image.shape[0] #  number of channels
# Create a 1xchannels + 1  grid of subplots
fig, axes = plt.subplots(1, image.shape[0] + 1 , figsize=(12, 3)) # Adjust figsize for better aspect ratio
axes = axes.ravel()  # Flatten the 1x4 array of axes

# Display the grayscale images
for iC in range(image.shape[0]):
    axes[iC].imshow(image[iC,:,:], cmap='gray' )
    #axes[iC].imshow(image[iC,:,:], cmap='gray', vmin = 100,vmax = 500) # You can also adjust the contrast
    axes[iC].set_title(ch_names[iC])
    axes[iC].axis('off')

# Display the RGB image
axes[nC].imshow(composite)
axes[nC].set_title('Merge')
axes[nC].axis('off')

# Adjust layout
plt.subplots_adjust(wspace=0.01, hspace=0.1)
# save data
plt.savefig(export_path + 'montage_plt.png', format = 'png', bbox_inches='tight', pad_inches=0)
# show the montage
plt.show()


# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')