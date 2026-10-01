# %% 
# Explore Max and Sum Projections

# %%
# Import python packages
from bioio import BioImage
import numpy as np
from napari.viewer import Viewer

# %%
# Open a 3D image and inspect its metadata
import re
img_obj = BioImage("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif")
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
# Create and view a maximum projection along z-axis, i.e. axis = 0
# - Observe how the maximum gives a nice "quick overview" of the data content
# - In order to see it at the same scale as the original image we need to scale in in x&y 
# - Napari: Observe that the image layer context menu also allows one to create projections
# - Napari: *Toggle grid mode (Ctrl + G)* to view images side by side
max_z_image = np.max(img, axis=0)
viewer.add_image(max_z_image, scale=[scales[1], scales[2]])
viewer.layers['max_z_image'].bounding_box.visible=True

# %%
# Compute sum projection along z-axis
# and display it in napari
sum_z_image = np.sum(img, axis=0)
viewer.add_image(sum_z_image, scale=[scales[1], scales[2]])
viewer.layers['sum_z_image'].bounding_box.visible=True

# %%
# Observe that the data type changed during the sum projection
# but not during the maximum projection
# - Understand why this make sense 
print("orig:", img.dtype) 
print("max projection:", max_z_image.dtype)
print("sum projection:", sum_z_image.dtype)

# %%
# Compute the maximum value that could occur during a sum projection of this image 
# and compare this to what it actually is and what would be supported by
# the data type of the sum projection
max_per_slice = np.iinfo(img.dtype).max
num_slices = img.shape[0]
max_sum_value = num_slices * max_per_slice
print("max sum value that could occur for this image:", max_sum_value)
print("actual max sum value in this image:", sum_z_image.max())
print("max sum value supported by projection:", np.iinfo(sum_z_image.dtype).max)

# %%
# Compute maximum projection along x-axis and y-axis
# and show in viewer with correct scaling
max_x_image = np.max(img, axis=2)
max_y_image = np.max(img, axis=1)
viewer.add_image(max_x_image, scale=[scales[0], scales[1]])
viewer.add_image(max_y_image, scale=[scales[0], scales[2]])
viewer.layers['max_x_image'].bounding_box.visible=True
viewer.layers['max_y_image'].bounding_box.visible=True


# %% 
# Close the viewer (CI test requires this)
viewer.close()

