# %%
# ## Spatial image calibration

# %%
# Import python packages.
import os
from OpenIJTIFF import save_ij_tiff
from bioio import BioImage
from napari.viewer import Viewer

# %%
# Open a 2D image and its axes metadata
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nucleus_calibrated.tif"
img_obj_2D = BioImage(image_url)
img_2D = img_obj_2D.data.squeeze()


# %%
# Inspect the image metadata
print("Shape:", img_2D.shape)
print("Axes:", img_obj_2D.dims)
print("Scale:", img_obj_2D.physical_pixel_sizes)
voxel_size_image_2D = list(img_obj_2D.physical_pixel_sizes)
# Load voxel units from metadata (in this specific case)
import re
unit = re.search(r"^unit=(.*)$", img_obj_2D.metadata, re.M).group(1)  # '\\u00B5m' (literal escape)
unit = unit.encode().decode("unicode_escape")
print("Units:", unit)

# %%
# Open a 3D image and its axes metadata
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__nucleus.tif"
img_obj_3D = BioImage(image_url)
img_3D = img_obj_3D.data.squeeze()

# %%
# Inspect the image axes metadata.
print("Shape:", img_3D.shape)
print("Axes:", img_obj_3D.dims)
print("Scale:", img_obj_3D.physical_pixel_sizes)
voxel_size_image_3D = list(img_obj_3D.physical_pixel_sizes)
# Load voxel units from metadata (in this specific case)
import re
unit = re.search(r"^unit=(.*)$", img_obj_3D.metadata, re.M).group(1)  # '\\u00B5m' (literal escape)
unit = unit.encode().decode("unicode_escape")
print("Units:", unit)

# %%
# Note that the 3D image does not have calibrated metadata.
# Let's add spatial calibration using the x&y voxel_size from the 2D image
# and also add a z scaling
voxel_size_image_3D = [0.52, voxel_size_image_2D[1], voxel_size_image_2D[0]]
units_image_3D = ["um", "um", "um"]

# %%
# Inspect the metadata for the 3D image
print("Shape: ", img_3D.shape)
print("Axes: ", img_obj_3D.dims)
print("Scale: ", voxel_size_image_3D)
print("Units: ", units_image_3D)

# %%
# Open napari and add the 3D image with voxel_size
viewer = Viewer()
viewer.add_image(img_3D, scale=voxel_size_image_3D, name='image_3D')

# %%
# Napari GUI: Use the 3D viewer button to render the image in 3D.

# %%
# Save the 3D image with the calibration metadata
save_ij_tiff(
     # during trainings this Path should be replaced by the user's desktop, e.g. C:/Users/dominik/Desktop
     os.path.join(os.path.expanduser("~"), "image_3D_calibrated.tif"),
     img_3D,
     ['z', 'y', 'x'],
     voxel_size_image_3D,
     units_image_3D
)

# %%
# Open the above file in FIJI and verify image scales were properly saved.

# %%
# Measure the length of the nucleus (as exercise)
# Napari GUI: use the `New points layer button` to create a new points layer.
# Napari GUI: use `Add points` to add two points along the longest axis

# %%
# points = napari_viewer.layers['Points'].data
# scale = napari_viewer.layers['Points'].scale
# points_cal = points * scale
# print("Points :\n", points)
# print("Calibrated points :\n", points_cal)

# %%
# from scipy.spatial import distance
# distance.euclidean(points_cal[0], points_cal[1])

# %%
# Close the viewer (CI test requires this)
viewer.close()