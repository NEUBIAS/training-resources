import imageio.v3 as iio
import napari

# Read and display the label-image from https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__four_objects.tif
image = iio.imread("xy_8bit_labels__four_objects.tif")
viewer = napari.Viewer()
viewer.add_labels(image)

# Perform shape measurements and discuss their meanings
from skimage.measure import regionprops

shape_measurements = regionprops(image)

# how many regions are in the image
print(len(shape_measurements))

# what measurements do you get?
# see also https://scikit-image.org/docs/stable/api/skimage.measure.html#regionprops
list(shape_measurements[0])

# print some features of the first region
print(shape_measurements[0].area, shape_measurements[0].eccentricity)

# print the area and of each region
for index, region in enumerate(shape_measurements):
    print(index, region.area)

# - Add a calibration of 2 micrometer to the image and check which shape measurements are affected.
# requires skimage>=0.20.0
spacing = (2, 2)
shape_measurements = regionprops(image, spacing=spacing)
# print some features of first object
print(shape_measurements[0].area, shape_measurements[0].eccentricity)


# Perform a shape analysis for 3D image
# Read https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_labels__spindle_spots.tif
image = iio.imread(
    "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_labels__spindle_spots.tif"
)

viewer.add_labels(image)

# Perform shape measurements and discuss their meanings
shape_measurements = regionprops(image)

# how many regions are in the image
print(len(shape_measurements))

# what measurements do you get?
# see also https://scikit-image.org/docs/stable/api/skimage.measure.html#regionprops
list(shape_measurements[0])

# print some features of the first region
print(shape_measurements[0].area, shape_measurements[0].eccentricity)

# print the area and of each region
for index, region in enumerate(shape_measurements):
    print(index, region.area)

# read calibration from the image metadata and perform measurements using this information.
# check which shape measurements are affected.
# requires skimage>=0.20.0
metadata = iio.immeta(
    "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_labels__spindle_spots.tif"
)
# TODO: spacing = ???
shape_measurements = regionprops(image, spacing=spacing)
# print some features of first object
print(shape_measurements[0].area, shape_measurements[0].eccentricity)
