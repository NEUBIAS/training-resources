# %%
# Nuclei, spots and nuclei boundary segmentation


import napari
import numpy as np
import matplotlib.pyplot as plt
# from OpenIJTIFF import open_ij_tiff
from bioio import BioImage


# %%
# Read the intensity image
# image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif')
img_obj = BioImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif")
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
# Napari: Inspect the pixel values in order to identify a threshold

# %%
# Also check the image histogram for a threshold
# Observe that interestingly there are several local minima in the histogram
plt.hist(img.flatten(), bins=np.arange(img.min(), img.max() + 1));
plt.yscale('log')

# %%
# Threshold both nuclei
# check the resulting datatype and content
# and view the binary image
binary_image_two_nuclei = img > 5
print(binary_image_two_nuclei.dtype)
print(np.unique(binary_image_two_nuclei))
viewer.add_labels(binary_image_two_nuclei, opacity=0.8)
viewer.layers['binary_image_two_nuclei']

# %%
# Apply a higher threshold
# to only segment the brighter nucleus
binary_image_one_nucleus = img > 15
viewer.add_labels(binary_image_one_nucleus, opacity=0.8)
viewer.layers['binary_image_one_nucleus'].new_colormap() # to get a new (different) colormap

# %%
# Apply an even higher threshold
# to only select the intranuclear speckles
binary_image_speckles = img > 44
viewer.add_labels(binary_image_speckles, opacity=0.8)
viewer.layers['binary_image_speckles'].new_colormap() # to get a new (different) colormap

# %%
# Apply two thresholds (aka "gating")
# to only select the boundary of cells
binary_image_boundary = (img < 5) & (img >= 4)
viewer.add_labels(binary_image_boundary, opacity=0.8)
viewer.layers['binary_image_boundary'].new_colormap() # to get a new (different) colormap

# %%
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')
