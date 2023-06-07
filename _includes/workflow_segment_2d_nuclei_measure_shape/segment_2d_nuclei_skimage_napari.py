# %%
# Import modules
import napari
from OpenIJTIFF import open_ij_tiff
from skimage.measure import label, regionprops_table
import pandas as pd

# %%
# Instantiate the napari viewer
napari_viewer = napari.Viewer()

# %%
# Open and inspect the image
# Learning opportunity: 
# - change file_path and image name to analyse a different image
#   - https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t70.tif
file_path = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif"
image, axes, scales, units = open_ij_tiff(file_path)
napari_viewer.add_image(image, name='incenp_t1')

# %%
# Binarize the image
image = image > 25
viewer.add_labels(image, name='binary')

# %%
# Perform connected components analysis (i.e create labels)
img_labels = label(image)
viewer.add_labels(img_labels, name='labels')

# %%
# Measure nuclei shapes
# Learning opportunity: 
# - add other measurements (Hint: google: skimage regionprops)
properties = regionprops_table(
    img_labels,
    properties = {'label', 'area'}
)

# %%
# Print areas for each cell
# Learning opportunity: 
# - print other measurements
areas = pd.DataFrame(properties)
print(areas)