#######################################################
## To follow along you need to complete the tool
## installation activity for skimage napari.
#######################################################

# Import python packages.
from napari.viewer import Viewer

from load_from_url import load_from_url
# Read image with AICSImage.
image = load_from_url("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mitotic_plate_calibrated.tif")

# Display information about dimensions.
print(image.dims)

# Display physical pixel size read from the metadata.
print(image.physical_pixel_sizes)

# Create a new napari_viewer
napari_viewer = Viewer()

# Add image with scaling to the viewer.
napari_viewer.add_image(image.data, scale=image.physical_pixel_sizes)
# Napari GUI: Change order of visible axes.
# Napari GUI: Explor 3D visualization.

# Note: As of now napari lacks funcitonality to easily measure distances between points in an open image.
# Currently, no orthogonal view plugin exists for napari.
