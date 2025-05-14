# %% 
# Open a TIFF series
# minimal conda env for this module
# conda create -n ImageFileFormats python=3.10
# activate ImageFileFormat
# pip install bioio bioio-tifffile bioio-lif bioio-czi bioio-ome-tiff bioio-ome-zarr notebook
# Note: for only dealing with .tif just do pip install bioio bioio-tifffile


# %%
# create list of image file names and order them
from pathlib import Path
path_to_files = Path('/Users/fschneider/Training/training-resources/image_data/xyz_8bit__em_volume_tiff_series')
tiff_files = [file for file in path_to_files.glob("*.tif")]
# order files
tiff_files.sort()
print(tiff_files)

# %%
# Open each image with BioIO
from bioio import BioImage
bioimages = [BioImage(file) for file in tiff_files]

# Print pixel sizes
for bioimage in bioimages:
    print(bioimage.physical_pixel_sizes)

# %%
# Concatenate in 3D volume
em_volume = [bioimage.data.squeeze() for bioimage in bioimages]
# make numpy array
import numpy as np
em_volume = np.stack(em_volume,axis=0)
print(em_volume.shape)

# %%
# Lazy load
import dask.array as da
em_volume = [bioimage.dask_data[0,0,:,:,:] for bioimage in bioimages]
em_volume = da.stack(em_volume,axis=0)
print(em_volume.shape)