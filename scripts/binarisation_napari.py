# Image binarization using napari as a viewer

# Import libraries
import imageio
import napari

# Use only one viewer to show all the images.
# Thus, only create a new one if none exist.
if 'viewer' not in globals():
    viewer = napari.Viewer()

# Load the image
image = imageio.imread('https://github.com/NEUBIAS/training-resources'
                       '/raw/master/image_data/xy_8bit__two_cells.tif')

# Binarise the image and create a new image object
# holding the resulting binary image
binary_image = image > 49

# Show both images
viewer.add_image(image)
viewer.add_image(binary_image)
