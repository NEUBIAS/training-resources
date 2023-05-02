# %% [markdown]
# #Test python napari skimage install
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# %%
# Read the intensity image
from skimage.io import imread
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif')

# %%
# View the intensity image
viewer.add_image(image)