# %%
# Thresholding bright and dim cells

import napari
from bioio import BioImage
import matplotlib.pyplot as plt
import numpy as np
# from OpenIJTIFF import open_ij_tiff


# %%
# Load the image
# image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif')
img_obj = BioImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif")
img = img_obj.data

# %%
# Print the order of image dimensions
print(f'Axes order = {img_obj.dims.order}')

# Open Napari Viewer
viewer = napari.Viewer()

# %%
# View the image
viewer.add_image(img)

# Add bounding boxes and colorbars for each channel
viewer.layers[0].bounding_box.visible = True
viewer.layers[0].colorbar.visible = True

# %%
# Napari: Inspect the pixel values to identify a threshold that segments both cells

# %%
# Inspect the image histogram to confirm the above threshold
plt.hist(img.flatten(), bins=np.arange(img.min(), img.max() + 1));
plt.yscale('log') # the background peak is so dominat that without the log scale it is hard to see the threshold

# %%
# Threshold the image and inspect the resulting values and data type
binary_image_two_cells = img > 49

print(np.unique(binary_image_two_cells))
print(binary_image_two_cells.dtype)

# %%
# Overlay the binary image
viewer.add_labels(binary_image_two_cells, opacity=0.8)

# %%
# Apply a higher threshold
# to only select the brighter cell
# and also add this to the viewer
binary_image_one_cell = img > 100
viewer.add_labels(binary_image_one_cell, opacity=0.8)
viewer.layers['binary_image_two_cells'].new_colormap() # to get a new (different) colormap

# %%
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')
