import napari
import numpy as np
from OpenIJTIFF import open_ij_tiff

# Read the images
image1, axes1, scales1, units1 = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_without_offset.tif')
image2, axes2, scales2, units2 = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_with_offset.tif')

# Inspect image data type and values
print(image1.dtype, image1.shape, np.min(image1), np.max(image1))
print(image2.dtype, image2.shape, np.min(image2), np.max(image2))

# Instantiate the napari viewer
viewer = napari.Viewer()

# Visualize images using matplotlib
viewer.add_image(image1, name='image1')
viewer.add_image(image2, name='image2')

# Explore the histograms
info_type = np.iinfo(image1.dtype)
print('\n', info_type)
min_val = info_type.min
max_val = info_type.max

import matplotlib.pyplot as plt
plt.hist(image1.flatten(), bins=np.arange(max_val+1), log=True);
plt.hist(image2.flatten(), bins=np.arange(max_val+1), log=True);

# Try manual thresholding
thr1 = 25
thr2 = 75

manual1 = image1>thr1
manual2 = image2>thr2

viewer.add_labels(manual1, name='manual_threshold1')
viewer.add_labels(manual2, name='manual_threshold2')
# Identify possible problems with this solution

# Explore auto-thresholding options on:
# https://scikit-image.org/docs/stable/api/skimage.filters.html

# Obtain the thresholding values
from skimage.filters import threshold_mean

thr1 = threshold_mean(image1)
print(thr1)
auto1 = image1>thr1

thr2 = threshold_mean(image2)
print(thr2)
auto2 = image2>thr2

# Visualize auto-thresholded images
viewer.add_labels(auto1, name='mean_threshold1')
viewer.add_labels(auto2, name='mean_threshold2')

# Explore other thresholding options
# Note that there exists a threshold_multiotsu function to handle cases with multi-peaks histograms