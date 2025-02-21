# %% 
# Open a BDV image file
# conda env for this module
# conda create -n bio_io_bdv python=3.10
# activate bio_io_bdv
# pip install bioio bioio-tifffile

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