# %% 
# Open a tif image file
# minimal conda env for this module
# conda create -n ImageFileFormats python=3.10
# activate ImageFileFormat
# pip install bioio bioio-tifffile bioio-lif bioio-czi bioio-ome-tiff bioio-ome-zarr notebook
# Note: for only dealing with .tif just do pip install bioio bioio-tifffile


# %%
# Load .tif file
# - Observe that BioImage chooses the correct reader plugin
from bioio import BioImage
image_url = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_PLK1_control.tif'
bioimage = BioImage(image_url)
print(bioimage)
print(type(bioimage))

# %%
# Inspect dimension and shape of image
print(f'Image dimension: {bioimage.dims}')
print(f'Dimension order is: {bioimage.dims.order}')
print(f'Image shape: {bioimage.shape}')

# %%
# Extract image data (5D)
image_data = bioimage.data
print(f'Image type: {type(image_data)}')
print(f'Image array shape: {image_data.shape}')
# Extract specific image part
image_data = bioimage.get_image_data('YX')
print(f'Image type: {type(image_data)}')
print(f'Image array shape: {image_data.shape}')

# %%
# Read pixel size
print(f'Pixel size: {bioimage.physical_pixel_sizes}')
# Read metadata
print(f'Metadata type: {type(bioimage.metadata)}')
print(f'Metadata: {bioimage.metadata}')

# %%
# Load .tif file with extensive metadata
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__collagen.md.tif"
bioimage = BioImage(image_url)

# %%
# Read pixel size
print(f'Pixel size: {bioimage.physical_pixel_sizes}')
# Read metadata
print(f'Metadata type: {type(bioimage.metadata)}')
print(f'Metadata: {bioimage.metadata}')