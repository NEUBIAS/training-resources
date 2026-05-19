# %% 
# Open a tif image file
# minimal conda env for this module
# conda create -n ImageFileFormats python=3.10
# activate ImageFileFormat
# pip install bioio bioio-tifffile notebook


#%%
# Load a large tif lazily
from bioio import BioImage
image_url = 'https://zenodo.org/records/14857764/files/xyz_uint8__em_platy.tif'
bioimage = BioImage(image_url)
print(bioimage)
print(type(bioimage))

#%%
# Extract pixel size
print(f'Pixel size: {bioimage.physical_pixel_sizes}')
# Inspect image dimension
print(f'Image dimension: {bioimage.dims}')

#%%
# lazy load whole image
bioimage_data = bioimage.dask_data
print(bioimage_data)

#%%
# For actually loading data, first download the data and then load it
from pathlib import Path
image_path = Path().cwd()/'xyz_uint8__em_platy.tif'
bioimage = BioImage(image_path)
# load specific image plane
bioimage_data = bioimage.dask_data[:,:,:,10,:].compute()