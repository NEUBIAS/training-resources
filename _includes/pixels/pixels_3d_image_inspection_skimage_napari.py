# %%
# 3D image inspection using skimage and napari

# %%
# Load an image
from OpenIJTIFF import open_ij_tiff
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mri_head.tif"
image, axes, *_ = open_ij_tiff(image_url)

# %%
# Inspect the image shape
print(image.shape)

# %%
# Inspect the image axes
print(axes)

# %%
# Inspect all image pixel values, and appreciate that this is not useful for larger 3D data
print(image)

# %%
# Create a napari viewer and add the image
from napari.viewer import Viewer
napari_viewer = Viewer()
napari_viewer.add_image(image)

# %%
# Napari: 
# - However with the mouse over the image and observe the pixel indices and values
# - Use the slider to change the position of the 3rd dimension

# %%
# Extract the pixels that belong to the tip of the nose
print(image[1, 9:19, 89:102])

# %%
# Compute the image min and max
print(image.min(), image.max())

# %%
# Compute the image histogram
import matplotlib.pyplot as plt
import numpy as np
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1));
