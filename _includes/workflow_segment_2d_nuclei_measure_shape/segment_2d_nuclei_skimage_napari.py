# %% [markdown]
# ## Workflow segment 2D nuclei
# This activity is part of [Nuclei segmentation and shape measurement](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html) 

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
# Learning opportunity: change file_path and the name of the image to analyse a different image: https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t70.tif
file_path = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif"
image, axes, scales, units = open_ij_tiff(file_path)
napari_viewer.add_image(image, name='incenp_t1')

# %%
# Binarize the image
# Learning opportunity: explore different threshold values 
image_binary = image > 25
napari_viewer.add_image(image_binary, name='binary', opacity = 0.3)

# %%
# Learning opportunity: explore [automatic thresholding](https://scikit-image.org/docs/stable/api/skimage.filters.html), e.g. `skimage.filters.threshold_li`

# %%
# Perform connected components analysis (i.e create labels)
image_labels = label(image_binary)
napari_viewer.add_labels(image_labels, name='labels')

# %%
# Measure nuclei shapes
properties = regionprops_table(
    image_labels,
    properties = {'label', 'area'}
)

# %%
# Learning opportunity: Try also different measurements. See documentation of [skimage regionsprops](https://scikit-image.org/docs/stable/api/skimage.measure.html#skimage.measure.regionprops)

# %%
# Print areas for each cell
# Learning opportunity: print other measurements
properties_dataframe = pd.DataFrame(properties)
print(properties_dataframe)

# %%
# Learing opportunity: Generalize the workflow for many images
#
# A "for loop*"" allows to extend the workflow to many more images and fully automate it. Here the backbone of code
# ```
# image_paths = ["https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif", "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t70.tif"]
#
# for file_path in image_paths:
#     print(file_path)
#     image, axes, scales, units = open_ij_tiff(file_path)
#     # More code here
# ```
#
# Save the data: Ideally one would like to save the results of each processed image.  For saving the label image you can use [`skimage.io.imsave`](https://scikit-image.org/docs/stable/api/skimage.io.html#skimage.io.imsave) for saving the table you can use e.g. [`pandas.DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html), i.e. `properties_dataframe.to_csv`. You can add these functions within the for loop. 
#
# To save the data one needs unique names. For instance one could extract the name of the image using [`os.path`](https://docs.python.org/3/library/os.path.html) functionality and then add some additional identifiers. 
