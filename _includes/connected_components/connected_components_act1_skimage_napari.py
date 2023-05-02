# %% [markdown]
# # 2D connected component labeling

# %%
# Import modules
import napari
from OpenIJTIFF import open_ij_tiff

# %%
# Instantiate the napari viewer
viewer = napari.Viewer()

# %%
# Read a binary 2D image and display it
binary_2D_image, axes_binary_2D_image, scales_binary_2D_image, units_binary_2D_image = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei.tif')
viewer.add_image(binary_2D_image)

# %%
# Connected components with connectivity 1 (aka 2D 4 connectivity) 
from skimage import measure
labels_2D_conn1_image = measure.label(binary_2D_image, connectivity=1)
viewer.add_labels(labels_2D_conn1_image)

# %%
# Connected components with connectivity 2 (aka 2D 8 connectivity) 
labels_2D_conn2_image = measure.label(binary_2D_image, connectivity=2)
viewer.add_labels(labels_2D_conn2_image)

