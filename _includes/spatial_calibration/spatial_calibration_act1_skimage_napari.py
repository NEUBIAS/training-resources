# %%
# Spatial image calibration

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
# Open napari and add the image with its voxel size.
napari_viewer = Viewer()
napari_viewer.add_image(image, scale=voxel_size)

# %%
# Napari GUI: Change the viewer dimension order using the corresponding button.
# Napari GUI: Use the 3D viewer button to render the image in 3D.

# %%
# Compute distances between points
#
# Napari GUI: use the `New points layer button` to create a new points layer.
# Napari GUI: use `Add points` to add two points somewhere on the meta-phase plate.

# %%
# extract point coordinates
# appreciate that they are in unscaled voxel coordinates
# and thus not suited for measuring distances
points = napari_viewer.layers['Points'].data
print(points)

# %%
# scale the positions
scale = napari_viewer.layers['Points'].scale
print("Points scale: ", scale)
print("Voxel size: ", voxel_size)

# %%
points_cal = points * scale
print("Points :\n", points)
print("Calibrated points :\n", points_cal)

# %%
# compute distance between points in voxel indices
# formula: sqrt( (z[1] - z[0])^2 + (y[1] - y[0])^2 + (x[1] - x[0])^2 )
diff_vector = points_cal[1] - points_cal[0]
print("diff_vector: ", diff_vector)

# %%
sqr_diff_vector = diff_vector**2
print("sqr_diff_vector: ", sqr_diff_vector)

# %%
distance = np.sqrt(sqr_diff_vector.sum())
print('Distance:', distance)
