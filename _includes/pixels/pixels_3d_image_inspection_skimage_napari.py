# %%
# 3D image inspection using skimage and napari

# %%
# Load an image
from bioio import BioImage
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__mri_head.tif"
img_obj = BioImage(image_url)
img = img_obj.data.squeeze()

# %%
# Inspect the image shape
print(img.shape)

# %%
# Inspect the image axes
print(img_obj.dims)

# %%
# Inspect all image pixel values, and appreciate that this is not useful for larger 3D data
print(img)

# %%
# Create a napari viewer and add the image
from napari.viewer import Viewer
viewer = Viewer()
viewer.add_image(img)

# %%
# Napari: 
# - However with the mouse over the image and observe the pixel indices and values
# - Use the slider to change the position of the 3rd dimension

# %%
# Extract the pixels that belong to the tip of the nose
print(img[1, 9:19, 89:102])

# %%
# Compute the image min and max
print(img.min(), img.max())

# %%
# Compute the image histogram
import matplotlib.pyplot as plt
plt.hist(img.flatten(), bins='auto')
plt.show()

# %% 
# Close the viewer (CI test requires this)
viewer.close()
plt.close('all')
