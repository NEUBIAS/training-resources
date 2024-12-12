# %% 
# Open a ome.tiff image file
# minimal conda env for this module
# conda create -n ImageFileFormats python=3.10
# activate ImageFileFormat
# pip install bioio bioio-tifffile bioio-lif bioio-czi bioio-ome-tiff bioio-ome-zarr notebook
# Note: for only dealing with ome.tif just do pip install bioio bioio-ome-tiff

# %%
# Load .lif file
from bioio import BioImage
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_xyc__two_images.lif"
bioimage = BioImage(image_url)

# %%
# Option 1: Direct conversion
from pathlib import Path
bioimage.save(Path().cwd()/'converted_file.ome.tiff')

# Alternative
BioImage(image_url).save(Path().cwd()/'direct_conversion.ome.tiff')

# %%
# Option 2: Indirect conversion
# Single image to OME Tiff
from bioio.writers import OmeTiffWriter

# Extract image and pixel info
bioimage.set_scene(0)
image1 = bioimage.data.squeeze()
pixel_info1 = bioimage.physical_pixel_sizes

# Perform some modification/analysis/...

# Save as OME Tiff
OmeTiffWriter.save(data=image1, # image to save
                   uri=Path().cwd()/'ConvertSingleImage.ome.tiff', # path to save to
                   physical_pixel_sizes = pixel_info1, 
                   dim_order='CYX') # dimension order

# %%
# Two images
# Extract image and pixel info
bioimage.set_scene(1)
image2 = bioimage.data.squeeze()
pixel_info2 = bioimage.physical_pixel_sizes

# Perform some modification/analysis/...

# Save as OME Tiff
OmeTiffWriter.save(data=[image1,image2],
                   uri=Path().cwd()/'ConvertTwoImages.ome.tiff',
                   dim_order=['CYX','YX'],
                   physical_pixel_sizes=[pixel_info1,pixel_info2])