# %%
# Spatial image calibration
# 
# Requirements:
# - https://neubias.github.io/training-resources/tool_installation/index.html#skimage_napari

# %%
# Import python packages
from OpenIJTIFF import open_ij_tiff
import numpy as np
from napari.viewer import Viewer

# %%
# Open an image of metaphase chromosomes and inspect the metadata
# - Observe that the xy and z voxel sizes are different (= anisotropic)
image, axes, voxel_size, units = open_ij_tiff(
    "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mitotic_plate_calibrated.tif"
)
print("Shape: ", image.shape)
print("Axes: ", axes)
print("Scale: ", voxel_size)
print("Units: ", units)

# %%
# View the image in napari
Viewer().add_image(image)

# %%
# Napari GUI: 
# - Change the axes order to look at the image from the side using the corresponding button
# - Look at the image in 3-D using the corresponding button
# - Conclude that the physical shape does not look correct
# - Important: close this viewer before proceeding, not to confuse yourself

# %%
# Open a new napari and and now add the image with its voxel size as a "scale".
# - Note that we are using a new viewer because navigating both the scaled and unscaled image in the same viewer is tricky
# - Again look at the image from the side and in 3-D
# - Observe that napari added interpolated data to make the image appear scaled
viewer = Viewer()
viewer.add_image(image, scale=voxel_size)

# %%
# In the next few steps we will compute distances between 3-D points

# %%
# Napari GUI: 
# - Use the `New points layer button` to create a new points layer
# - Use `Add points` to add two points somewhere on the meta-phase plate

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
# Compute distance between points in voxel indices
# - Pythagoras: sqrt( (z1-z0)^2 + (y1-y0)^2 + (x1-x0)^2 )
diff_vector = points_cal[1] - points_cal[0]
print("diff_vector:", diff_vector)

# %%
sqr_diff_vector = diff_vector**2
print("sqr_diff_vector:", sqr_diff_vector)

# %%
distance = np.sqrt(sqr_diff_vector.sum())
print("distance:", distance)
