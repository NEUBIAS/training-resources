# %% 
# Open a CZI image file
# minimal conda env for this module
# conda create -n ImageFileFormats python=3.10
# activate ImageFileFormat
# pip install bioio bioio-tifffile bioio-lif bioio-czi bioio-ome-tiff bioio-ome-zarr notebook
# Note: for only dealing with .czi just do pip install bioio bioio-czi


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
# load specific image plane
bioimage_data = bioimage.dask_data[:,:,:,10,:].compute()