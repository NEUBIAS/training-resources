# %% 
# Open a BDV image file
# conda env for this module
# conda create -n bio_io_bdv python=3.10
# activate bio_io_bdv
# pip install bioio bioio-bioformats

# %%
# Load BDV file
# - Observe that BioImage chooses the correct reader plugin
from bioio import BioImage
from pathlib import Path
bioimage = BioImage(Path().cwd()/'xyz_uint8__em_platy__3d_chunk_multires.xml')
print(bioimage)
print(type(bioimage))

# %%
# load whole data
image_data = bioimage.data

# %%
# lazy load data
image_data = bioimage.dask_data
print(image_data)

#%%
# lazy load a specific image plane
bioimage_data = bioimage.dask_data[:,:,:,10,:].compute()

#%%
# Checkout different resolution levels
# The way it should be implemented and according to docs
# Get current resolution level
print(bioimage.current_resolution_level)
# See all resolution levels
print(bioimage.resolution_levels)
# Set resolution level
bioimage.set_resolution_level(0)

# The way how it is actually working for this type of image:
# Get current resolution level
print(bioimage.current_scene) # Prints string as combination of image name and resolution level
# See all resolution levels
print(bioimage.scenes)
# Set resolution level
bioimage.set_scene(0) # or for scene in bioimage.scenes: bioimage.set_scene(scene)