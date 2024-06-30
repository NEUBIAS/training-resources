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
# - Observe that the 3D rendering does not reflect the real shape
#   of the metaphase chromosomes in this image
Viewer().add_image(image)

# %%
# Napari GUI: 
# - In order to inspect the image from "the side", change the axes order 
#   using the corresponding button; observe that additional data 
#   layers have been added to deal with the voxel_size anisotropy of this image
# - Look at the image in 3-D using the corresponding button; 
#   observe that the overall shape looks correct, thanks to the anisotropic scalings
# - Important: close this viewer before proceeding, not to confuse yourself

# %%
# Open a new napari and and now add the image with its voxel size as a "scale".
# - Note that we are using a new viewer because navigating 
#   both the scaled and unscaled image in the same viewer is tricky
viewer = Viewer()
viewer.add_image(image, scale=voxel_size)


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
points = viewer.layers['Points'].data
print(points)

# %%
# Scale the positions
scale = viewer.layers['Points'].scale
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
