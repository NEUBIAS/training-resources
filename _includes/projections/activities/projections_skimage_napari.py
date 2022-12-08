# Import modules
import napari
from skimage.io import imread

# Instantiate the napari viewer
viewer = napari.Viewer()

# Open a 3D image
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit__spots.tif')
viewer.add_image(image)

# Remember the axis order 0=z, 1=x, 2=y

# Maximum projection along z-axis
max_z_image = np.max(image, axis=0)
viewer.add_image(max_z_image)

# Sum projection along z-axis
sum_z_image = np.sum(image, axis=0)
viewer.add_image(sum_z_image)

# Appreciate that changing the data type during sum projections is useful
print(np.iinfo(image.dtype)) # maximum value that the image's datatype can represent
print(image.shape[0]*np.iinfo(image.dtype).max) # maximum value that could occur during sum projection
print(sum_z_image.dtype) # luckily numpy changed the data type during projection
print(np.iinfo(sum_z_image.dtype)) # maximum value that the new data type can represent

# Maximum projection along x-axis and y-axis
max_x_image = np.max(image, axis=2)
max_y_image = np.max(image, axis=1)
viewer.add_image(max_x_image)
viewer.add_image(max_y_image)

# Due to the aniotropic pixel size the x and y projections appear squashed
# We can rescale the image to make it appear physcially correct
dx = 0.0941 # micrometer
dy = 0.0941 # micrometer
dz = 0.4 # micrometer

from skimage.transform import rescale
# The axes of the max_y_image are 0=z,1=x
# The z axes is squashed thus we enlarge it to make the image isotropic
rescaled_max_y_image = rescale(max_y_image, [dz/dy,1])  
viewer.add_image(rescaled_max_y_image)

# The max_x_image could be rescaled in the  same way
