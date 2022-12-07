# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# Read a binary image
from skimage.io import imread
binary_2D_image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__nuclei.tif')

viewer.add_image(binary_2D_image)

from skimage import measure
# ?measure.label to get help

# connectivity 1 (aka 2D 4 connectivity) 
labels_2D_conn1_image = measure.label(binary_2D_image, connectivity=1)

viewer.add_labels(labels_2D_conn1_image)

# connectivity 2 (aka 2D 8 connectivity) 
labels_2D_conn2_image = measure.label(binary_2D_image, connectivity=2)

viewer.add_labels(labels_2D_conn2_image)

binary_3D_image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_binary__spots.tif')

# connectivity 1 (aka 3D 6 connectivity) 
labels_3D_conn1_image = measure.label(binary_3D_image, connectivity=1)

viewer.add_labels(labels_3D_conn1_image)

print(np.unique(labels_3D_conn1_image))



