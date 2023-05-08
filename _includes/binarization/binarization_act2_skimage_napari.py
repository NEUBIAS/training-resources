# %% [markdown]
# ## Spots and threshold interval
 
# %%
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# %%
# Read the intensity image
from OpenIJTIFF import open_ij_tiff
image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__PCNA.tif')

# View the intensity image
viewer.add_image(image)

# %%
# Check the intensity image's datatype
print(image.dtype)

# %% [markdown]
# **Napari GUI** Inspect the intensity image values in order to identify a threshold  \
# **Napari GUI** hover with mouse \
# **Napari GUI** make a line profile using the Napari plugin `napari-plot-profile`  (`pip install napari-plot-profile`)

# %%
# Threshold the image
binary_image_two_nuclei = image > 5

# Overlay the binary image
viewer.add_image(binary_image_two_nuclei, opacity=0.8)

# %%
# Inspect data type
print(binary_image_two_nuclei.dtype)

# %%
# Inspect value content
import numpy as np
print(np.unique(binary_image_two_nuclei))

# %%
# Apply a higher threshold
# to only select the brighter dots
binary_image_bright_dots = image > 44
viewer.add_image(binary_image_bright_dots, opacity=0.8)

# %%
# Apply two thresholds 
# to only select the boundary of cells
binary_image_boundary = (image < 5) * (image >= 4)
viewer.add_image(binary_image_boundary, opacity=0.8)
