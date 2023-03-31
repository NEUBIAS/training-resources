# Import modules
import napari
from skimage.io import imread

# Instantiate the napari viewer
viewer = napari.Viewer()

# Read a binary 2D image
binary_2D_image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei.tif')
viewer.add_image(binary_2D_image)

# Connected components with connectivity 1 (aka 2D 4 connectivity) 
from skimage import measure
labels_2D_conn1_image = measure.label(binary_2D_image, connectivity=1)
viewer.add_labels(labels_2D_conn1_image)

# Connected components with connectivity 2 (aka 2D 8 connectivity) 
labels_2D_conn2_image = measure.label(binary_2D_image, connectivity=2)
viewer.add_labels(labels_2D_conn2_image)

