# Image binarization for napari terminal window
import imageio
image = imageio.imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif')

# binarise
binary_image = image > 49

# show images
viewer.add_image(image)
viewer.add_image(binary_image)