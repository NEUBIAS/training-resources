# %% [markdown]
# ## Explore Max and Sum Projections
#
#

# %%
# Import python packages.
from OpenIJTIFF import open_ij_tiff
import numpy as np
from napari.viewer import Viewer
from skimage.transform import rescale

# %%
# Instantiate the napari viewer
viewer = Viewer()

# %%
# Open a 3D image
image_url = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif'
image, axes, scales, units = open_ij_tiff(image_url)
viewer.add_image(image)

# %%
# Check image dimension
# Axis order is 0=z, 1=x, 2=y
image.shape


# %%
# Maximum projection along z-axis. i.e. axis = 0
max_z_image = np.max(image, axis=0)
viewer.add_image(max_z_image)

# %% [markdown]
# Use *Toggle grid mode (Ctrl + G)* in **Napari-GUI** to view images side by side

# %%
# Sum projection along z-axis
sum_z_image = np.sum(image, axis=0)


# %%
# Appreciate that changing the data type during sum projections is useful
print(np.iinfo(image.dtype)) # range of values that the image's datatype can represent

# %%
# Maximum value that could occur during sum projection 
# is number of slices (image.shape[0]) multiplied by the maximal possible value for each slice
max_possible_value = image.shape[0]*np.iinfo(image.dtype).max
print("Maximum possible pixel value during sum projection %d"  % max_possible_value)

# %%
# luckily numpy changed the data type during projection
print(np.iinfo(sum_z_image.dtype)) # range of values that the new data type can represent

# %%
# Display the image in Napari
viewer.add_image(sum_z_image)

# %%
# BUG - Napari has an issue displaying uint32. 
# Convert to float to properly visualize the image
sum_z_image_float = sum_z_image.astype(float)
viewer.add_image(sum_z_image_float) 

# %%
# Maximum projection along x-axis and y-axis
max_x_image = np.max(image, axis=2)
max_y_image = np.max(image, axis=1)
viewer.add_image(max_x_image)
viewer.add_image(max_y_image)

# %%
# Due to the anisotropic pixel size the x and y projections appear squashed
# We can rescale the image to make it appear physically correct
np.set_printoptions(precision=3)
print(f"Voxel size in micrometer [Z, Y, X]: {np.array(scales)}")

dz = scales[0]
dy = scales[1]
dx = scales[2]

# %%
# The axes of the max_y_image are 0=z,1=x
# The z axes is squashed thus we enlarge it to make the image isotropic
rescaled_max_y_image = rescale(max_y_image, [dz/dy,1])  
viewer.add_image(rescaled_max_y_image)

# %%
# The max_x_image could be rescaled in the same way
rescaled_max_x_image = rescale(max_x_image, [dz/dy,1])  
viewer.add_image(rescaled_max_x_image)

