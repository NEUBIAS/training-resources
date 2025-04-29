# %% 
# Apply manual and automated thresholds

# %%
# initial imports
import napari
import numpy as np
from OpenIJTIFF import open_ij_tiff

# %%
# Read two images
image1, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_without_offset.tif')
image2, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_with_offset.tif')

# %%
# Inspect image data type and value range
print(image1.dtype, image1.shape, image1.min(), image1.min())
print(image2.dtype, image2.shape, image2.min(), image2.max())

# %%
# Instantiate the napari viewer and display the images
viewer = napari.Viewer()

# %%
# Add the images
viewer.add_image(image1, name="image1")
viewer.add_image(image2, name="image2")

# %%
# Show the histogram
import matplotlib.pyplot as plt
plt.hist(image1.flatten(), bins=np.arange(image1.max()+1), log=True);
plt.hist(image2.flatten(), bins=np.arange(image2.max()+1), log=True);

# %%
# Try manual thresholding
thr1 = 25
thr2 = 75

manual_thresholded1 = image1>thr1
manual_thresholded2 = image2>thr2

viewer.add_label(manual_thresholded1, name='manual_thresholded1', opacity = 0.4, colormap='magenta')
viewer.add_label(manual_thresholded2, name='manual_thresholded2', opacity = 0.4, colormap='magenta')
# Identify possible problems with this solution

# %% [markdown]
# Explore auto-thresholding options on:
# https://scikit-image.org/docs/stable/api/skimage.filters.html

# %%
# Obtain the thresholding values
from skimage.filters import threshold_mean

thr1 = threshold_mean(image1)
print(thr1)
mean_thresholded1 = image1>thr1

thr2 = threshold_mean(image2)
print(thr2)
mean_thresholded2 = image2>thr2

# %%
# Visualize auto-thresholded images
viewer.add_label(mean_thresholded1, name='mean_thresholded1', opacity = 0.4, colormap='magenta')
viewer.add_label(mean_thresholded2, name='mean_thresholded2', opacity = 0.4, colormap='magenta')

# %% 
# Explore other thresholding options
# Note that there exists a threshold_multiotsu function to handle cases with multi-peaks histograms
