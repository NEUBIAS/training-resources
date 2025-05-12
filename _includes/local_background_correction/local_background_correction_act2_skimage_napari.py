# %% 
# Background subtraction using a maximum intensity projection

# %%
import numpy as np
from OpenIJTIFF import open_ij_tiff
import napari
import matplotlib.pyplot as plt

# Read the image
image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyt_8bit_polyp.tif')

# %%
# Appreciate that this is a time-lapse image
print(image.shape, axes)

# %%
# Instantiate the napari viewer
# - Appreciate that one cannot segment the polyp by one simple intensity threshold (two thresholds may work...)
viewer = napari.Viewer()
viewer.add_image(image)

# %%
# Create a background image by a maximum projection along the time axis
# - Remember the axis order 0=t, 1=y, 2=x
# - The background is bright and the object is moving, thus a maximum projection yields the background
background = np.max(image, axis = 0)
viewer.add_image(background)

# %%
# Create foreground image
# - Cast to signed int16 to also allow negative values
foreground = image.astype('int16') - background.astype('int16')
viewer.add_image(foreground)

# %%
# Segment the polyp by simple thresholding of the foreground image
plt.hist(foreground.flatten(), bins=np.arange(foreground.min(), foreground.max() + 1));
plt.yscale('log')
binary_polyp = foreground < -25
viewer.add_image(binary_polyp)

# %% 
# Close the viewer (CI test requires this)
viewer.close()