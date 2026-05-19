# %% [markdown]
# # 3D connected component labeling

# %%
# Import modules
import napari
from skimage.measure import label
from OpenIJTIFF import open_ij_tiff
import numpy as np

# %%
# Instantiate the napari viewer
viewer = napari.Viewer()

# %%
# Read a binary 3D image and display it
binary_3D_image, axes_binary_3D_image, scales_binary_3D_image, units_binary_3D_image = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_binary__spots.tif')
viewer.add_image(binary_3D_image)

# %%
# Connected components with connectivity 2 (aka 3D 26 connectivity) 
labels_3D_conn2_image = label(binary_3D_image, connectivity=2)
viewer.add_labels(labels_3D_conn2_image)

# %%
# Interrogate the values in the 3D label image
print(np.unique(labels_3D_conn2_image)) # the object indices
print(len(np.unique(labels_3D_conn2_image))-1) # the number of objects (minus background)
print(np.max(labels_3D_conn2_image)) # the number of objects (minus background) (if the labels are consecutive!)
np.sum(labels_3D_conn2_image==2) # the number of pixels (~volume) in object number 2

# %% 
# Close the viewer (CI test requires this)
viewer.close()
