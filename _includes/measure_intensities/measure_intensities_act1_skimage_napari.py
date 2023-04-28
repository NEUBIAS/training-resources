# %% [markdown]
# ### Measure intensities (with background subtraction)

# %%
# Import python packages.
from OpenIJTIFF import open_ij_tiff, save_ij_tiff
from skimage.io import imsave
import numpy as np
from napari.viewer import Viewer
import pandas as pd
from skimage.measure import regionprops_table

# %%
# load image from url
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__h2b.tif"
image, axes_image, voxel_image, units_image = open_ij_tiff(fpath)
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b.tif"
labels, axes_labels, voxel_labels, units_labels = open_ij_tiff(fpath)

# %%
# Create a napari_viewer and visualize image and labels
napari_viewer = Viewer()
napari_viewer.add_image(image, name='image')
napari_viewer.add_labels(labels, name='objects')

# %% [markdown]
# ## Compute the intensities 
# ### Background label  
# We can have an estimation of background intensity with the "0" label.\
# Here, manually create in the Viewer an additional label ("3" in this case)

# %%
objects_labels = np.unique(labels.flatten())
objects_labels.sort()
print(objects_labels)

# %% [markdown]
# Observe that there are 4 values, 0 being the label of the background, 
# 1,2 are the cells and 3 is the manually labeled background.

# %%
# Use the intensity_image option to measure fluorescence intensity of objects
fluo_regionprops = regionprops_table(
        labels,
        intensity_image = image,
        properties = ('label','area','intensity_mean','intensity_max')
)
print(fluo_regionprops)

# %%
# Wrap in a panda dataframe for better visualization nd export
fluo_measures = pd.DataFrame(fluo_regionprops)
fluo_measures.to_csv("object_measurements.csv")
print(fluo_measures)

# %%
# Compute background value
background = fluo_measures[fluo_measures.label==3].intensity_mean.values[0]
print(background)

# %%
# Append the background-corrected values to the table
fluo_measures['intensity_sum'] = fluo_measures.intensity_mean * fluo_measures.area
fluo_measures['mean_corr'] = fluo_measures.intensity_mean - background
fluo_measures['max_corr'] = fluo_measures.intensity_max - background
fluo_measures['sum_corr'] = fluo_measures.mean_corr * fluo_measures.area
print(fluo_measures)

# %%
# Save as table
fluo_measures.to_csv("object_measurements.csv")

# %% [markdown]
# ### Larger labels for intensitiy measures  

# %%
# Load the data
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b_dilate_labels.tif"
dilated_labels, axes_labels, voxel_labels, units_labels = open_ij_tiff(fpath)
objects_labels = np.unique(dilated_labels.flatten())
print(objects_labels)

# %%
# Display the labels 
napari_viewer.add_labels(dilated_labels, name='dilated_objects')

# %%
# Use the intensity_image to compute the fluorescence parameters
fluo_measures_dilated = pd.DataFrame(
    regionprops_table(
        dilated_labels,
        intensity_image = image,
        properties = ('label','area','intensity_mean','intensity_max')
    )
)

# %%
# Append the background-corrected values to the table using the same background
fluo_measures_dilated['intensity_sum'] = fluo_measures_dilated.intensity_mean * fluo_measures_dilated.area
fluo_measures_dilated['mean_corr'] = fluo_measures_dilated.intensity_mean - background
fluo_measures_dilated['max_corr'] = fluo_measures_dilated.intensity_max - background
fluo_measures_dilated['sum_corr'] = fluo_measures_dilated.mean_corr * fluo_measures_dilated.area
# Export the data
fluo_measures_dilated.to_csv("object_measurements_dilated.csv")
print(fluo_measures_dilated)
