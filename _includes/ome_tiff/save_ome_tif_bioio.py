# %% 
# Save a ome.tiff image file
# minimal conda env for this module
# conda create -n ImageFileFormats python=3.10
# activate ImageFileFormat
# pip install bioio  notebook

# %%
# Create a random image to save
import numpy as np

image = np.random.rand(512,512)

# %%
# Save as OME Tiff
from bioio.writers import OmeTiffWriter
from pathlib import Path

OmeTiffWriter.save(data=image, # image to save
                   uri=Path().cwd()/'TestImage.ome.tiff', # path to save to
                   dim_order='YX') # dimension order

# %%
# Save two images in one ome tiff
# generate two images
image0 = np.random.rand(3,512,512)
image1 = np.random.rand(256,256)

# add some pixel size data
from bioio_base.types import PhysicalPixelSizes

pixelsize0 = PhysicalPixelSizes(Z=0.3,Y=0.1,X=0.1)
pixelsize1 = PhysicalPixelSizes(Z=None,Y=0.5,X=0.5)

OmeTiffWriter.save(data=[image0,image1],
                   uri=Path().cwd()/'TwoImages.ome.tiff',
                   dim_order=['ZYX','YX'],
                   physical_pixel_sizes=[pixelsize0,pixelsize1])