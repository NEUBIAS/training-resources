# %%
# Explore a 3D image

# %%
# Imports
from OpenIJTIFF import open_ij_tiff
from napari.viewer import Viewer

# %%
# Load the image
image, axes, scales, units = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__chromosomes.tif")

# View the image in napari
viewer = Viewer()
viewer.add_image(image)

# [markdown]
# Napari GUI: Explore different sliders and values in the bottom left part.
# Napari GUI: Show in 3D. Note that the scalings are not yet correct.

# %%
# Print image axes metadata
print("Shape: ", image.shape)
print("Axes: ", axes)
print("Scales: ", scales)
print("Units: ", units)

# %%
# Add image with scaling.
viewer.add_image(image, name = "Scaled image", scale = scales)

# %%
# Napari GUI: View scaled image in 3D. Note that the scaling is now correct.

# %% 
# Close the viewer (CI test requires this)
viewer.close()