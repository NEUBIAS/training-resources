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
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__statistical_filter_test_input.tif')
viewer.add_image(image, name="Original")

# %%
# Manual activity:
# Choose one interesting 5x5 region in the image and manually compute
# the statistical filters. Compare later with the below automated results.

# %% 
# Apply Minimum filter
# - Removes bright details smaller than the structuring element
minimum_filtered = rank.minimum(image, disk(2))
viewer.add_image(minimum_filtered, name="Minimum (r=2)")

# %% 
# Apply Maximum filter
# - Removes dark details smaller than the structuring element
maximum_filtered = rank.maximum(image, disk(2))
viewer.add_image(maximum_filtered, name="Maximum (r=2)")

# %% 
# Apply Mean filter
# - Smooths the image by averaging pixels within the structuring element
mean_filtered = rank.mean(image, disk(2))
viewer.add_image(mean_filtered, name="Mean (r=2)")

# %% 
# Apply Median filter
# - Removes noise while preserving edges
median_filtered = rank.median(image, disk(2))
viewer.add_image(median_filtered, name="Median (r=2)")

# %% 
# Apply Variance filter
# - Highlights areas with high intensity variation
variance_filtered = generic_filter(image.astype(float), function=np.var, size=2)
viewer.add_image(variance_filtered, name="Variance (r=2)")

viewer.grid.enabled = True

# %%
# Learning opportunity:
# - Check the output of the variance filter without converting to float datatype
# - Explore how changing the size of the filter kernels affects the output

# %% 
# Close the viewer (CI test requires this)
viewer.close()