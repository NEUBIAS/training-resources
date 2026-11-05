# %%
# Spatial image calibration

# %%
# Import python packages
from bioio import BioImage
from napari.viewer import Viewer

# %%
# Open a 3-D image of metaphase chromosomes and inspect the metadata
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mitotic_plate_calibrated.tif"
img_obj = BioImage(image_url)
img = img_obj.data.squeeze()
print("Shape:", img.shape)
print("Axes:", img_obj.dims)
print("Scale:", img_obj.physical_pixel_sizes)
voxel_size = list(img_obj.physical_pixel_sizes)
# Load voxel units from metadata (in this specific case)
import re
unit = re.search(r"^unit=(.*)$", img_obj.metadata, re.M).group(1)  # '\\u00B5m' (literal escape)
unit = unit.encode().decode("unicode_escape")
print("Units:", unit)

# %%
# View the image in napari
viewer = Viewer()
viewer.add_image(img)

# Napari: 
# - Change the axes order to look at the image "from the side" using the corresponding button
# - Look at the image in 3-D using the corresponding button
# - Conclude that the physical shape does not look correct
# - Important: close this viewer before proceeding, not to confuse yourself

# %%
# Close the image in napari
viewer.close()

# %%
# Open napari and add the image with its voxel size.
viewer = Viewer()
viewer.add_image(img, scale=voxel_size)

# %%
# Napari GUI: Change the viewer dimension order using the corresponding button.
# Napari GUI: Use the 3D viewer button to render the image in 3D.

# %%
# Compute distances between points
#
# Napari GUI: use the `New points layer button` to create a new points layer.
# Napari GUI: use `Add points` to add two points somewhere on the meta-phase plate.

# %%
# Napari: 
# - Again look at the image from the side and in 3-D
# - Observe that, thanks to the "scale", the 3-D physical shape looks correct now
# - Observe that napari added interpolated data to make the image appear scaled

# %%
# In the following, we will compute distances between 3-D points
# This is interesting, as you will learn:
# - How to use drawing layers in napari
# - How to use image scaling (voxel_size) information for physical measurements


# %%
# Extract the point coordinates
points = viewer.layers['Points'].data
print(points) # unscaled => not very useful for physical measurements

# %%
# Scale the points
scale = viewer.layers['Points'].scale # same as voxel_size
print("Points scale: ", scale)
print("Voxel size: ", voxel_size)
points_cal = points * scale 
print("Points:\n", points)
print("Calibrated points:\n", points_cal)

# %%
# Compute the distance between the first and second point
print("First point:" , points_cal[0])
print("Second point:" , points_cal[1])
from scipy.spatial import distance
distance.euclidean(points_cal[0], points_cal[1])

# %%
# Close the viewer (CI test requires this)
viewer.close()