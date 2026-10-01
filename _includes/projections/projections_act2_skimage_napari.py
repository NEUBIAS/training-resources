# %%
# Explore Max and Sum Projections

# %%
# Import python packages
from bioio import BioImage
import numpy as np
from napari.viewer import Viewer
import matplotlib.pyplot as plt

# %%
# Open a 3D image and inspect its metadata
import re
img_obj = BioImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_calibrated_16bit__golgi_bfa.tif")
img = img_obj.data
print(f"Axes order : {img_obj.dims.order}")
print(f"Shape      : {img_obj.dims}")
print(f"Data type  : {img.dtype}")
print(f"Pixel size : {img_obj.physical_pixel_sizes}")
img = img.squeeze()
scales = list(img_obj.physical_pixel_sizes)
print(scales)
match = re.search(r'unit=(.+)', img_obj.metadata)
unit = match.group(1).encode().decode('unicode_escape')
print(unit)

# %%
# As this is an anisotropic image, we view it scaled
# - Napari: Use 3-D rendering see all the spots
viewer = Viewer()
viewer.add_image(img, scale=scales)
viewer.layers['img'].bounding_box.visible=True

# %%
sum_z_image_float = np.sum(img, axis=0).astype(float)
viewer.add_image(sum_z_image_float, scale=scales[1:3]) 
viewer.layers['sum_z_image_float'].bounding_box.visible=True

# %%
#plot histogram of the sum projection and find the highest value
plt.hist(sum_z_image_float.ravel(), bins=256, log=True)
max_z_value = np.max(sum_z_image_float)
print(f'Max value in sum projection: {max_z_value}')
plt.axvline(max_z_value, color='r', linestyle='dashed', linewidth=1)


# %%
sum_y_image_float = np.sum(img, axis=1).astype(float)
viewer.add_image(sum_y_image_float, scale=[scales[0], scales[2]])
viewer.layers['sum_y_image_float'].bounding_box.visible=True

# %%
#plot histogram of the sum projection and find the highest value
plt.hist(sum_y_image_float.ravel(), bins=256, log=True)
max_y_value = np.max(sum_y_image_float)
print(f'Max value in sum projection: {max_y_value}')
plt.axvline(max_y_value, color='r', linestyle='dashed', linewidth=1)


# %%
max_z_image_float = np.max(img, axis=0).astype(float)
viewer.add_image(max_z_image_float, scale=scales[1:3]) 
viewer.layers['max_z_image_float'].bounding_box.visible=True

# %%
max_z_value_2 = np.max(max_z_image_float)
print(f'Max value in sum projection: {max_z_value_2}')

# %%
max_y_image_float = np.max(img, axis=1).astype(float)
viewer.add_image(max_y_image_float, scale=[scales[0], scales[2]]) 
viewer.layers['max_y_image_float'].bounding_box.visible=True

# %%
max_y_value_2 = np.max(max_y_image_float)
print(f'Max value in sum projection: {max_y_value_2}')

# %%
plt.close('all')
viewer.close()

# %%
