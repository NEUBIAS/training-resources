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
img_obj = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_a.tif')
img = img_obj.data
print(f"Axes order : {img_obj.dims.order}")
print(f"Shape      : {img_obj.dims}")
print(f"Data type  : {img.dtype}")
print(f"Pixel size : {img_obj.physical_pixel_sizes}")
img = img.squeeze()
viewer.add_image(img)
viewer.layers[0].colorbar.visible = True

# %% 
# Check the image's datatype
print(img.dtype)
print(np.iinfo(img.dtype)) # Useful as it also prints the value range

# %%
# Check for clipping, i.e. pixels values at the limits of the value range
# This is important for many reasons, for example: 
# - Pixel values at the limit of the value range typically cannot be used for intensity quantification 
# - Important algorithms, e.g. for spot detection, do not work well in regions with intensity clipping
print("Min:", img.min()) # Are there any clipped pixels?
print("Max:", img.max()) # Are there any clipped pixels?
print("Number of 0 pixels:", np.sum(img==0)) # How many clipped pixels are there?
print("Number of 255 pixels:", np.sum(img==255))
plt.hist(img.flatten(), bins='auto')
plt.show()


# img_obj = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__h2b.tif')
# img = img_obj.data
# img_obj = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif')
# img = img_obj.data
img_obj = BioImage('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif')
img = img_obj.data
print(f"Axes order : {img_obj.dims.order}")
print(f"Shape      : {img_obj.dims}")
print(f"Data type  : {img.dtype}")
print(f"Pixel size : {img_obj.physical_pixel_sizes}")
img = img.squeeze()

# View the image
viewer.add_image(img)
viewer.layers[-1].colorbar.visible = True

# %%
# Check the image's datatype and its value limits
print(np.iinfo(img.dtype))

# Check the image's minimum and maximum intensity
print(np.min(img),np.max(img))

# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')

# %%
