# %% 
# Explore image data types and value ranges

# %%
# Import libraries and instantiate napari
import napari
import numpy as np
import matplotlib.pyplot as plt
from bioio import BioImage

viewer = napari.Viewer()

# %%
# Open an image and view it
img = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_a.tif')
img_data = img.data.squeeze()
viewer.add_image(img_data)

# https://forum.image.sc/t/add-hilo-colormap-to-napari/95601

# %% 
# Check the image's datatype
print(img_data.dtype)
print(np.iinfo(img_data.dtype)) # Useful as it also prints the value range

# %%
# Check for clipping, i.e. pixels values at the limits of the value range
# This is important for many reasons, for example: 
# - Pixel values at the limit of the value range typically cannot be used for intensity quantification 
# - Important algorithms, e.g. for spot detection, do not work well in regions with intensity clipping
print("Min:", img_data.min()) # Are there any clipped pixels?
print("Max:", img_data.max()) # Are there any clipped pixels?
print("Number of 0 pixels:", np.sum(img_data==0)) # How many clipped pixels are there?
print("Number of 255 pixels:", np.sum(img_data==255))
plt.hist(img_data.flatten(), bins='auto')
plt.show()


# img = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__h2b.tif')
# img_data = img.data.squeeze()
# img = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif')
# img_data = img.data.squeeze()
img = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif')
img_data = img.data.squeeze()

# View the image
viewer.add_image(img_data)

# %%
# Check the image's datatype and its value limits
print(np.iinfo(img_data.dtype))

# Check the image's minimum and maximum intensity
print(np.min(img_data),np.max(img_data))

# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')

# %%
