# Import modules
import napari
from skimage.io import imread
from skimage import measure

# Instantiate the napari viewer
viewer = napari.Viewer()

# Read a binary 3D image
binary_3D_image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_binary__spots.tif')

# Connected components with connectivity 2 (aka 3D 26 connectivity) 
labels_3D_conn2_image = measure.label(binary_3D_image, connectivity=2)
viewer.add_labels(labels_3D_conn2_image)

# Interrogate the values in the 3D label image
print(np.unique(labels_3D_conn2_image)) # the object indices
print(len(np.unique(labels_3D_conn2_image))-1) # the number of objects (minus background)
print(np.max(labels_3D_conn2_image)) # the number of objects (minus background) (if the labels are consecutive!)
np.sum(labels_3D_conn2_image==2) # the number of pixels (~volume) in object number 2
