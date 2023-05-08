# %% [markdown]
# ## Explore dimensions in a 3D image

# %%
from OpenIJTIFF import open_ij_tiff
# Load the image
# You can also load a local image by providing the path to the file
image, axes, scales, units  = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit__chromosomes.tif")

from napari.viewer import Viewer
# Create a new napari viewer.
napari_viewer = Viewer()

# Add an image to the napari_viewer.
napari_viewer.add_image(image)

# %%
# Print image shape
print(image.shape)

# %%
# Print axes IDs
print(axes)

# %% [markdown]
# **Napari GUI** Explore different sliders and values in the bottom left part \
# **Napari GUI** Show in 3D. Note that the scaling are not yet correct. 

# %%
# compute aspect ratio
print(scales)
aspect_ratio = [s/scales[2] for s in scales]
print(aspect_ratio)

# %%
# Add image. Rationale is to show both images in the same scale
napari_viewer.add_image(image, name = "with aspect ratio", scale = aspect_ratio) 

# %% [markdown]
# **Napari GUI** Show images with blending additive and different LUTs
