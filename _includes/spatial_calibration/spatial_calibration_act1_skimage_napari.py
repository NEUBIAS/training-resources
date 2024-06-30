# %%
# Spatial image calibration
# 
# Requirements:
# - [skimage and napari](https://neubias.github.io/training-resources/tool_installation/index.html#skimage_napari)

# %%
# Import python packages.
from OpenIJTIFF import open_ij_tiff
import numpy as np
from napari.viewer import Viewer

# %%
# Open an image and its axes metadata
image, axes, voxel_size, units = open_ij_tiff(
    "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mitotic_plate_calibrated.tif"
)

# %%
# Inspect the image axes metadata.
print("Shape: ", image.shape)
print("Axes: ", axes)
print("Scale: ", voxel_size)
print("Units: ", units)

# %%
# Open napari and add the image with its voxel size as a "scale".
#
# Notes:
# - In principle it would be very instructive to observe how this compares
#   to the rendering of the image without the "scale" parameter; however in our
#   experience the navigation in napari, due to the different spatial extends 
#   of the images, becomes quite confusing...
napari_viewer = Viewer()
napari_viewer.add_image(image, scale=voxel_size)

# %%
# Napari GUI: 
# - In order to inspect the image from "the side", change the axes order 
#   using the corresponding button; observe that additional data 
#   layers have been added to deal with the voxel_size anisotropy of this image
# - Look at the image in 3-D using the corresponding button; 
#   observe that the overall shape looks correct, thanks to the anisotropic scalings

# %%
# Compute distances between points
# - In the next few steps we will computed distances between 3-D points

# %%
# Napari GUI: 
# - Use the `New points layer button` to create a new points layer
# - Use `Add points` to add two points somewhere on the meta-phase plate

# %%
# Extract point coordinates
# observe that they are in unscaled voxel coordinates
# and thus not suited for measuring distances
points = napari_viewer.layers['Points'].data
print(points)

# %%
# Scale the positions
scale = napari_viewer.layers['Points'].scale
print("Points scale: ", scale)
print("Voxel size: ", voxel_size)

# %%
points_cal = points * scale 
print("Points :\n", points)
print("Calibrated points :\n", points_cal)

# %%
# Compute distance between points in voxel indices
# - Formula: sqrt( (z[1] - z[0])^2 + (y[1] - y[0])^2 + (x[1] - x[0])^2 )
diff_vector = points_cal[1] - points_cal[0]
print("diff_vector: ", diff_vector)

# %%
sqr_diff_vector = diff_vector**2
print("sqr_diff_vector: ", sqr_diff_vector)

# %%
distance = np.sqrt(sqr_diff_vector.sum())
print('distance:', distance)
