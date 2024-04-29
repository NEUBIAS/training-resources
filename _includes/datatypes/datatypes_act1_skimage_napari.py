# %% [markdown]
# ## Explore image data types and value ranges

# %%
# Import modules
import napari
import numpy as np
from OpenIJTIFF import open_ij_tiff
viewer = napari.Viewer()


# %%
# Open the image
# Execute one of the cells 
#image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif')
#image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_a.tif')
#image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_b.tif')
#image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__h2b.tif')
#image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif')
image, *_ = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif')

# View the image
viewer.add_image(image)

# %%
# Check the image's datatype and its value limits
print(np.iinfo(image.dtype))

# Check the image's minimum and maximum intensity
print(np.min(image),np.max(image))

# %%

# %%
