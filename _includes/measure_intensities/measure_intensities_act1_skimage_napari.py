# %% 
#  Measure intensities with background subtraction

# %%
# Import python packages
from OpenIJTIFF import open_ij_tiff, save_ij_tiff
from skimage.io import imsave
import numpy as np
from napari.viewer import Viewer
import pandas as pd
from skimage.measure import regionprops_table, regionprops

# %%
# Load image and segmentation (aka labels)
image, *_ = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__h2b.tif")
labels, *_ = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b.tif")
print("labels", np.unique(labels))

# %%
# Create a napari_viewer and visualize image and labels
viewer = Viewer()
viewer.add_image(image)
viewer.add_labels(labels)

# %% 
# Napari:
# Add a dedicated background label  
# - Intensity measurements require background subtraction, thus one needs a region to measure the background intensity
# - Finding a suitable background region can be challenging, here we do it manually 
# - Using the `layer controls` for the `labels` layer, manually create an additional label ("3" in this case) that specifically measures the background

# %%
# Appreciate that the labels image has been modified "in place"
# as there is now another "3" label
print("labels", np.unique(labels))

# %%
# Check which intensity measurements are available
regionprops?

# %%
# Measure the object intensities 
# - This immediately converts the measurements into a pandas dataframe
df = pd.DataFrame(regionprops_table(
        labels,
        intensity_image = image,
        properties = ('label', 'area', 'intensity_mean', 'intensity_max')
))
print(df)

# %%
# Fetch the mean background intensity value
background = df.intensity_mean[2] 
print(background)

# %%
# Append the sum intensity and 
# background-corrected values to the table
df['intensity_sum'] = df.intensity_mean * df.area
df['intensity_mean_corr'] = df.intensity_mean - background
df['intensity_max_corr'] = df.intensity_max - background
df['intensity_sum_corr'] = df.intensity_mean_corr * df.area
print(df)

# Export the data 
df.to_csv("intensity_measurements.csv")

# %%
# Optional: Repeat the above with "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__h2b_dilate_labels.tif"
# - Discuss how the measurements are affected by the larger object regions

# %% 
# Close the viewer (CI test requires this)
viewer.close()