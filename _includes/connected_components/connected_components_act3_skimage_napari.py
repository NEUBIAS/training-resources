# %% [markdown]
# # Many objects

# %%
# Import modules
import napari
from skimage import measure
from OpenIJTIFF import open_ij_tiff
import numpy as np

# %%
# Instantiate the napari viewer
viewer = napari.Viewer()

# %%
# Read a binary 2D image and display it
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__many_vesicles.tif"
binary_2D_image, axes_binary_2D_image, scales_binary_2D_image, units_binary_2D_image = open_ij_tiff(fpath)
viewer.add_image(binary_2D_image)

# %%
# Connected components with connectivity 1 
labels_2D_conn1_image = measure.label(binary_2D_image, connectivity=1)
viewer.add_labels(labels_2D_conn1_image)

# %%
# Interrogate the values in the 2D label image
print(np.unique(labels_2D_conn1_image)) # the object indices
print(len(np.unique(labels_2D_conn1_image))-1) # the number of objects (minus background)
print(np.max(labels_2D_conn1_image)) # the number of objects (minus background) (if the labels are consecutive!)