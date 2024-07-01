# %% 
# Explore Max and Sum Projections

# %%
# Import python packages
from OpenIJTIFF import open_ij_tiff
import numpy as np
from napari.viewer import Viewer
from skimage.transform import rescale

# %%
# Open a 3D image and inspect its metadata
image, axes, scales, units = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif")
print(image.shape)
print(axes)
print(scales)
print(units)

# %%
# As this is an anisotropic image, we view it scaled
# - Napari: Use 3-D rendering see all the spots
viewer = Viewer()
viewer.add_image(image, scale=scales)

# %%
# Create and view a maximum projection along z-axis, i.e. axis = 0
# - Observe how the maximum gives a nice "quick overview" of the data content
# - In order to see it at the same scale as the original image we need to scale in in x&y 
# - Napari: observe that the image layer context menu also allows one to create projections
# - Napari: *Toggle grid mode (Ctrl + G)* to view images side by side
max_z_image = np.max(image, axis=0)
viewer.add_image(max_z_image, scale=[scales[1], scales[2]])

# %%
# Compute sum projection along z-axis
# and display it in napari
# - Napari: There is an an issue rendering the sum projection pixel values:
#   some high values appear dark. More details and a possible work-around is given at 
#   the end of this script.
sum_z_image = np.sum(image, axis=0)
viewer.add_image(sum_z_image, scale=[scales[1], scales[2]])

# %%
# Observe that the data type changed during the sum projection
# but not during the maximum projection
# - Understand why this make sense 
print("orig:", image.dtype) 
print("max projection:", max_z_image.dtype)
print("sum projection:", sum_z_image.dtype)

# %%
# Compute the maximum value that could occur during sum projection of this image 
# and compare this to what it actually is and what would be supported
max_per_slice = np.iinfo(image.dtype).max
num_slices = image.shape[0]
max_sum_value = num_slices * max_per_slice
print("max sum possible for this image:", max_sum_value)
print("actual max sum in this image:", sum_z_image.max())
print("max sum supported by projection:", np.iinfo(sum_z_image.dtype).max)

# %%
# Compute maximum projection along x-axis and y-axis
# and show in viewer with correct scaling
max_x_image = np.max(image, axis=2)
max_y_image = np.max(image, axis=1)
viewer.add_image(max_x_image, scale=[scales[0], scales[1]])
viewer.add_image(max_y_image, scale=[scales[0], scales[2]])

# %%
# Optional work-around for the above mentioned issue when rendering
# certain data types (https://github.com/NEUBIAS/training-resources/issues/570)
# Convert sum projection to float to properly visualize it
sum_z_image_float = sum_z_image.astype(float)
viewer.add_image(sum_z_image_float, scale=scales[1:3]) 