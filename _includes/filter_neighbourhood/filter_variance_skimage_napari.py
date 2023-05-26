# %% [markdown]
# ## Applying variance filters to an image

# %%
# Instantiate the napari viewer
import napari
from OpenIJTIFF import open_ij_tiff
viewer = napari.Viewer()

# %%
# Read the intensity image and add it to napari
image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__em_mitochondria_er.tif')
viewer.add_image(image)

# %%
# Appreciate that one cannot readily segment the sample by a simple intensity threshold
binary_image = image < 230
viewer.add_image(binary_image)

# %% 
# Apply a variance filter 
from skimage.filters.rank import mean
from skimage.morphology import disk
import numpy as np
int_image = image.astype(np.int32)
mean_image = mean(int_image, disk(11))
squared_diff_image = (int_image  - mean_image)**2
mean_squared_diff_image = mean(squared_diff_image, disk(11))
viewer.add_image(mean_squared_diff_image)

# %%
# Segment the foreground by applying a threshold
# (TBH in this specific case a simple mean filter might have been sufficient
# to achieve the same result, because the sample is on average darker than the background)
binary_variance_image = mean_squared_diff_image > 100
viewer.add_image(binary_variance_image)

# %%
