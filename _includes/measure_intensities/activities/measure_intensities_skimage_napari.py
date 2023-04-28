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
napari_viewer.add_image(image, name='image')
napari_viewer.add_labels(labels, name='objects')

#%%
# Extract object labels
objects_labels = np.unique(labels.flatten())
objects_labels.sort()
print(objects_labels)

# Observe that there are 3 labels, 0 being the label of the background, 1,2 are the cells
objects_labels = np.delete(objects_labels,0) # remove the background from the object labels
print(objects_labels)

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
    'area (pixels)': areas,
    'mean_intensity': mean_intensities
})

df.to_csv("object_measurements.csv")

#%%
df

#%%
# Even though we could have an estimation of background intensity with the "0" label,
# use the napari viewer to manually create an additional label (3 in this case)
# and compute the background.
# Append the background to the table

new_labels = napari_viewer.layers[1].data
background = np.mean(image[new_labels==3])

df['background'] = background

#%%
df

#%%
# compute mean, max, sum intensity corrected by the background
areas = [None for i in objects_labels]
mean_intensities = [None for i in objects_labels]
max_intensities = [None for i in objects_labels]
sum_intensities = [None for i in objects_labels]

i = 0
for label in objects_labels:
    
    areas[i] = len(labels[labels==label])
    mean_intensities[i] = np.mean(image[labels==label]) - background
    max_intensities[i] = np.max(image[labels==label]) - background
    sum_intensities[i] = np.sum(image[labels==label]) - background*areas[i]
    
    i += 1
    
df = pd.DataFrame({
    'object_label': objects_labels,
    'area (pixels)': areas,
    'mean_corrected': mean_intensities,
    'max_corrected': max_intensities,
    'sum_corrected': sum_intensities,
    'background': background,
})

#%%
df

#%%
### Perform the same analysis using slightly different labels
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b_dilate_labels.tif"
large_labels, axes_labels, voxel_labels, units_labels = open_ij_tiff(fpath)

# Add the new labels to the napari viewer
napari_viewer.add_labels(large_labels, name='large_objects')

# extract object labels
objects_labels = np.unique(large_labels.flatten())
objects_labels.sort()
objects_labels = np.delete(objects_labels,0) # remove the background from the object labels

# compute mean, max, sum intensity corrected by the background
areas = [None for i in objects_labels]
mean_intensities = [None for i in objects_labels]
max_intensities = [None for i in objects_labels]
sum_intensities = [None for i in objects_labels]

i = 0
for label in objects_labels:
    
    areas[i] = len(large_labels[large_labels==label])
    mean_intensities[i] = np.mean(image[large_labels==label]) - background
    max_intensities[i] = np.max(image[large_labels==label]) - background
    sum_intensities[i] = np.sum(image[large_labels==label]) - background*areas[i]
    
    i += 1
    
# Construct human-readable table
df_large = pd.DataFrame({
    'object_label': objects_labels,
    'area (pixels)': areas,
    'mean_corrected': mean_intensities,
    'max_corrected': max_intensities,
    'sum_corrected': sum_intensities,
    'background': background,
})

df_large

# Observe that the quantification has changed. Discuss how and why.

#%%
# Try quantifying fluorescence inetnsity for a challenging image
# load image from url
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyc_16bit__embryo_transmission_fluorescence.tif"
image, axes_image, voxel_image, units_image = open_ij_tiff(fpath)
print(axes_image)
print(voxel_image)

# Create a napari_viewer and visualize image and labels
napari_viewer1 = Viewer()
napari_viewer1.add_image(image[0], name='brightfield')
napari_viewer1.add_image(image[1], name='fluo', colormap='magenta', opacity=0.5)

# Appreciate the low SNR and the inhomogeneous background, which makes quantification challenging.
