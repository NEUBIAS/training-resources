# %% 
# Explore Max and Sum Projections

# %%
# Import python packages
from OpenIJTIFF import open_ij_tiff
import numpy as np
from napari.viewer import Viewer
from skimage.transform import rescale
import matplotlib.pyplot as plt

# %%
image, axes, scales, units = open_ij_tiff("xyz_calibrated_16bit__golgi_bfa.tif")
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
sum_z_image_float = np.sum(image, axis=0).astype(float)
viewer.add_image(sum_z_image_float, scale=scales[1:3]) 


# %%
#plot histogram of the sum projection and find the highest value
plt.hist(sum_z_image_float.ravel(), bins=256, log=True)
max_z_value = np.max(sum_z_image_float)
print(f'Max value in sum projection: {max_z_value}')
plt.axvline(max_z_value, color='r', linestyle='dashed', linewidth=1)
plt.show()

# %%
sum_y_image_float = np.sum(image, axis=1).astype(float)
viewer.add_image(sum_y_image_float, scale=[scales[0], scales[2]])

# %%
#plot histogram of the sum projection and find the highest value
plt.hist(sum_y_image_float.ravel(), bins=256, log=True)
max_y_value = np.max(sum_y_image_float)
print(f'Max value in sum projection: {max_y_value}')
plt.axvline(max_y_value, color='r', linestyle='dashed', linewidth=1)
plt.show()

# %%
max_z_image_float = np.max(image, axis=0).astype(float)
viewer.add_image(max_z_image_float, scale=scales[1:3]) 

# %%
max_z_value_2 = np.max(max_z_image_float)
print(f'Max value in sum projection: {max_z_value_2}')

# %%
max_y_image_float = np.max(image, axis=1).astype(float)
viewer.add_image(max_y_image_float, scale=[scales[0], scales[2]]) 

# %%
max_y_value_2 = np.max(max_y_image_float)
print(f'Max value in sum projection: {max_y_value_2}')

# %%
viewer.close()