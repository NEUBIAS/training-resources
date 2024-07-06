#%% 
# Measure shapes in 2D

#%%
from OpenIJTIFF import open_ij_tiff
import napari

#%%
# Open a label image with a few objects
labels, axes, scales, units = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__four_objects.tif")

#%%
# Show the label image in napari 
viewer = napari.Viewer()
viewer.add_labels(labels)

#%%
# Perform shape measurements and discuss their meanings
# See: https://scikit-image.org/docs/stable/api/skimage.measure.html#skimage.measure.regionprops
from skimage.measure import regionprops_table
import pandas as pd
properties = [ 'label', 'area', 'perimeter', 'eccentricity', 'major_axis_length', 'minor_axis_length', 'solidity']
table = regionprops_table( labels, properties = properties )
print(type(table))
df = pd.DataFrame(table)
print(type(df))
print(df)

#%%
# Find the object with the biggest area
print(df['area'].max())
print(df['area'].idxmax())
print(df['label'][0]) # i.e. df['label'][df['area'].idxmax()]