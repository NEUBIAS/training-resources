# %%
# Statistical filtering

# %%
# Import modules
import napari
import numpy as np
from skimage import io
from skimage.filters import rank
from skimage.morphology import disk
from skimage import img_as_float, img_as_ubyte
from scipy.ndimage import generic_filter
from OpenIJTIFF import open_ij_tiff

# %%
# Instantiate the napari viewer
viewer = napari.Viewer()

# %%
# Read and view the image
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__em_mitochondria_er.tif')
viewer.add_image(image, name="Original")


# %% 
# Apply Variance filter
# - Highlights areas with high intensity variation
variance_filtered = generic_filter(image.astype(float), function=np.var, size=5)
viewer.add_image(variance_filtered, name="Variance (r=5)")

viewer.grid.enabled = True

# %%
# Learning opportunity:
# - Check the output of the variance filter without converting to float datatype
# - Explore how changing the size of the filter kernels affects the output

# - Apply a threshold 
binary = variance_filtered > 90
viewer.add_image(binary, name="binary")

# %% 
# Close the viewer (CI test requires this)
viewer.close()