#######################################################
## To follow along you need to complete the tool
## installation activity for skimage napari.
#######################################################

# Import python packages
from load_from_url import load_from_url
from napari.viewer import Viewer

# Read image with AICSImage
image_url = load_from_url("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mitotic_plate_calibrated.tif")
image = image_url.data

# Display information about dimensions
print(image_url.dims)
print(image.shape)
# Note that dims of image_url gives the same info as numpy array shape

# Display physical pixel size read from the metadata
print(image_url.physical_pixel_sizes)

# Create a new napari_viewer
napari_viewer = Viewer()

# Add image with scaling to the viewer
napari_viewer.add_image(image.data, scale=image.physical_pixel_sizes)
# Napari GUI: Change order of visible axes
# Napari GUI: Explor 3D visualization

# Note: As of now napari lacks funcitonality to easily measure distances between points in an open image
# Currently, no orthogonal view plugin exists for napari.
