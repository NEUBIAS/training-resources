# %% 
# Nuclei, spots and nuclei boundary segmentation

# %%
# Import libraries and instantiate the viewer
import napari
import numpy as np 
import matplotlib.pyplot as plt
viewer = napari.Viewer()

# %%
# Read the intensity image
from OpenIJTIFF import open_ij_tiff
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif')

# %%
# Check the image's data type and 
# view the image
print(image.dtype)
viewer.add_image(image)

# %% 
# Napari: Inspect the pixel values in order to identify a threshold 

# %%
# Also check the image histogram for a threshold
# Observe that interestingly there are several local minima in the histogram
plt.hist(image.flatten(), bins=np.arange(image.min(), image.max() + 1));
plt.yscale('log')

# %%
# Threshold both nuclei
# check the resulting datatype and content 
# and view the binary image
binary_image_two_nuclei = image > 5
print(binary_image_two_nuclei.dtype)
print(np.unique(binary_image_two_nuclei))
viewer.add_image(binary_image_two_nuclei, opacity=0.8)

# %%
# Apply a higher threshold
# to only segment the brighter nucleus
binary_image_one_nucleus = image > 15
viewer.add_image(binary_image_one_nucleus, opacity=0.8)

# %%
# Apply an even higher threshold
# to only select the intranuclear speckles 
binary_image_speckles = image > 44
viewer.add_image(binary_image_speckles, opacity=0.8)

# %%
# Apply two thresholds (aka "gating") 
# to only select the boundary of cells
binary_image_boundary = (image < 5) & (image >= 4)
viewer.add_image(binary_image_boundary, opacity=0.8)
