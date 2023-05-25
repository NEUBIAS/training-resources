import imageio.v3 as iio
import matplotlib.pyplot as plt
import napari
from skimage.measure import regionprops, regionprops_table

# Open image [xy_16bit_labels__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit_labels__nuclei.tif)
image = iio.imread(
    "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit_labels__nuclei.tif"
)

# Measure object shapes and find the label index of the nucleus with the largest perimeter
shape_measurements = regionprops(image)
for index, region in enumerate(shape_measurements):
    print(index, region.perimeter)

# Change the pixel size to 0.5 um and repeat the measurements. Why do some parameters change while others don't?
spacing = (0.15, 0.15)
shape_measurements_scaled = regionprops(image, spacing=spacing)
for index, region in enumerate(shape_measurements):
    print(index, region.perimeter)


# (Optional) Create an image where each object is colored according to the measured circularity
shape_measurements_table = regionprops_table(image, properties=("label", "eccentricity"))

viewer = napari.Viewer()
label_layer = viewer.add_labels(image, name="eccentricity")

colors = plt.cm.viridis(shape_measurements_table["eccentricity"])
label_layer.color_mode = "direct"
label_layer.color = dict(zip(shape_measurements_table["label"], colors))
