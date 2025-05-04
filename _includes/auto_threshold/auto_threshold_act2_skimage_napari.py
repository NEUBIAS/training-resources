# %% [markdown]
# ## Apply automated thresholds in 3D


# %%
# initial imports
import numpy as np
import napari
from OpenIJTIFF import open_ij_tiff

# %%
# Read the images
image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__nuclei_autothresh.tif')

# %%
scales

# %%
# Inspect image data type and values
print(f'Type: {image.dtype} \nShape: {image.shape} \nMin: {np.min(image)} \nMax: {np.max(image)}')

# %%
# Instantiate the napari viewer and display the image
viewer = napari.Viewer()
viewer.add_image(image, name='image', scale=scales)

# %%
# Obtain threshold value using Otsu's algorithm
from skimage.filters import threshold_otsu
thresholded_otsu = image > threshold_otsu(image)

viewer.add_labels(thresholded_otsu, name='otsu',  colormap = {None: None, 1: 'green'},  scale=scales)

# %% [markdown]
# **Napari GUI** Explore the results in the napari viewer. For 3D data one can change the order 
# of visible axes (bottom left in napari viewer window). If not satisfied by the
# results, we can explore other threshold algorithms

# %%
# Additional threshold methods
from skimage.filters import threshold_li
thresholded_li = image > threshold_li(image)
viewer.add_labels(thresholded_li, name='li', colormap = {None: None, 1: 'orange'}, scale=scales)

# %%
