# %% 
# Thresholding bright and dim cells

# %%
# Instantiate the napari
import napari
from OpenIJTIFF import open_ij_tiff
viewer = napari.Viewer()

# %%
# Load the image
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif')

# %%
# Check the datatype and view the image
print(image.dtype)
viewer.add_image(image)

# %%
# Napari: Inspect the pixel values to identify a threshold that segments both cells 

# %%
# Inspect the image histogram to confirm the above threshold
import matplotlib.pyplot as plt
import numpy as np
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1)); 
plt.yscale('log') # the background peak is so dominat that without the log scale it is hard to see the threshold

# %%
# Threshold the image and inspect the resulting values and data type
binary_image_two_cells = image > 49
import numpy as np
print(np.unique(binary_image_two_cells))
print(binary_image_two_cells.dtype)

# %%
# Overlay the binary image
viewer.add_image(binary_image_two_cells, opacity=0.8)

# %%
# Apply a higher threshold
# to only select the brighter cell
# and also add this to the viewer
binary_image_one_cell = image > 100
viewer.add_image(binary_image_one_cell, opacity=0.8)
