#%% 
# Practice measure shape

#%%
from OpenIJTIFF import open_ij_tiff
import matplotlib.pyplot as plt
import napari
import numpy as np
from skimage.measure import regionprops, regionprops_table

#%%
# Open image [xy_16bit_labels__nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit_labels__nuclei.tif)
image, axes_image, scales_image, units_image = open_ij_tiff(
    "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit_labels__nuclei.tif"
)

#%%
viewer = napari.Viewer()
label_layer = viewer.add_labels(image, name="eccentricity")

#%%
# Measure object shapes
shape_measurements = regionprops(image)
# Print perimeter and eccentricity of each label
for region in shape_measurements:
    print(region.label, region.perimeter, region.eccentricity)

#%%
# Optional: find the label index of the nucleus with the largest perimeter
perimeters = [region.perimeter for region in shape_measurements]
labels = [region.label for region in shape_measurements]

idx_max_perimeter = np.argmax(perimeters)
label_max_perimeter = labels[idx_max_perimeter]

print('Largest perimeter:',np.max(perimeters))
print('Label with largest perimeter:',label_max_perimeter)

#%%
# Change the pixel size to 0.5 um and repeat the measurements. Why do some parameters change while others don't?
shape_measurements_scaled = regionprops(image, spacing=scales_image)
for region in shape_measurements_scaled:
    print(region.label, region.perimeter, region.eccentricity)

#%%
# Optional: Create an image where each object is colored according to the measured circularity
shape_measurements_table = regionprops_table(image, properties=("label", "eccentricity"))

#%%
colors = plt.cm.viridis(shape_measurements_table["eccentricity"])
label_layer.color_mode = "direct"
label_layer.color = dict(zip(shape_measurements_table["label"], colors))


