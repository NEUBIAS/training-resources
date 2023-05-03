#####
# test_installation_skimage_napari.py
# If you have the package jupytext installed (pip install jupytext). 
# Cells will be automatically generated.   
#####

# %% [markdown]
# # Test python napari skimage install

# %%
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# %%
# Read the intensity image
from skimage.io import imread
fpath = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__two_cells.tif'
image = imread(fpath)

# %%
# View the intensity image
viewer.add_image(image)

# %% 
# Read via OpenIJTIFF (OpenIJTiff.py must be in the same folder as the notebook path)
from OpenIJTIFF import open_ij_tiff
image_opentiff, axes, scales, units = open_ij_tiff(fpath)
# View the intensity image
viewer.add_image(image_opentiff)
