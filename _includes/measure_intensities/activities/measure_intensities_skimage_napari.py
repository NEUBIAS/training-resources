#######################################################
## To follow along you need to complete the tool
## installation activity for skimage napari.
#######################################################

#%%
# Import python packages.
from OpenIJTIFF import open_ij_tiff, save_ij_tiff
from skimage.io import imsave
import numpy as np
from napari.viewer import Viewer
import pandas as pd

#%% ### download and read tif file
# load image from url
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__h2b.tif"
image, axes_image, voxel_image, units_image = open_ij_tiff(fpath)
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b.tif"
labels, axes_labels, voxel_labels, units_labels = open_ij_tiff(fpath)

#%%
# Create a napari_viewer and visualize image and labels
napari_viewer = Viewer()
napari_viewer.add_image(image)
napari_viewer.add_labels(labels)

#%%
# Measure the mean fluorescence intensity and the object pixel area manually
objects_labels = list(set(labels.flatten()))
objects_labels.sort()
print(objects_labels)
# Observe that there are 3 labels, 0 being the label of the background, 1,2 are the cells

#%%
# Use numpy to compute area and fluorescence intensities of objects
mean_intensities = [None for i in objects_labels]
areas = [None for i in objects_labels]

i = 0
for label in objects_labels:
    
    areas[i] = len(labels[labels==label])
    mean_intensities[i] = np.mean(image[labels==label])
    
    i += 1
    
# Construct human-readable table
df = pd.DataFrame({
    'object_label': objects_labels,
    'area': areas,
    'mean_intensity': mean_intensities
})

#%%
df
