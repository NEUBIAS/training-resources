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
image_object = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_a.tif')
image_data = image_object.data.squeeze()
viewer.add_image(image_data)

# https://forum.image.sc/t/add-hilo-colormap-to-napari/95601

# %% 
# Check the image's datatype
print(image_data.dtype)
print(np.iinfo(image_data.dtype)) # Useful as it also prints the value range

# %%
# Check for clipping, i.e. pixels values at the limits of the value range
# This is important for many reasons, for example: 
# - Pixel values at the limit of the value range typically cannot be used for intensity quantification 
# - Important algorithms, e.g. for spot detection, do not work well in regions with intensity clipping
print("Min:", image_data.min()) # Are there any clipped pixels?
print("Max:", image_data.max()) # Are there any clipped pixels?
print("Number of 0 pixels:", np.sum(image_data==0)) # How many clipped pixels are there?
print("Number of 255 pixels:", np.sum(image_data==255))
plt.hist(image_data.flatten(), bins='auto')
plt.show()


# image_object = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__h2b.tif')
# image_data = image_object.data.squeeze()
# image_object = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif')
# image_data = image_object.data.squeeze()
image_object = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif')
image_data = image_object.data.squeeze()

# View the image
viewer.add_image(image_data)

# %%
# Check the image's datatype and its value limits
print(np.iinfo(image_data.dtype))

# Check the image's minimum and maximum intensity
print(np.min(image_data),np.max(image_data))

# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')

# %%
