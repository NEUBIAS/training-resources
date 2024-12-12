# %% 
# Open a ome.tiff image file
# minimal conda env for this module
# conda create -n ImageFileFormats python=3.10
# activate ImageFileFormat
# pip install bioio bioio-tifffile bioio-lif bioio-czi bioio-ome-tiff bioio-ome-zarr notebook
# Note: for only dealing with ome.tif just do pip install bioio bioio-ome-tiff


# %%
# Load .ome.tiff file
# Please download the image from 'https://github.com/NEUBIAS/training-resources/blob/master/image_data/xy_xyc__two_images.ome.tiff'
# save image in your current directory in a folder called ExampleImages
# - Observe that BioImage chooses the correct reader plugin
from bioio import BioImage
from pathlib import Path
bioimage = BioImage(Path().cwd()/'ExampleImages/xy_xyc__two_images.ome.tiff')
print(bioimage)
print(type(bioimage))

# %%
# Inspect the number of images in the file
print(f'Number of Images: {bioimage.scenes}')

# %%
# Inspect dimension and shape of the first image
bioimage.set_scene(0)
print(f'Image dimension: {bioimage.dims}')
print(f'Dimension order is: {bioimage.dims.order}')
print(f'Image shape: {bioimage.shape}')

# %%
# Extract image data (5D)
image_data = bioimage.data
print(f'Image type: {type(image_data)}')
print(f'Image array shape: {image_data.shape}')
# Extract specific image part
image_data = bioimage.get_image_data('YX',C=1)
print(f'Image type: {type(image_data)}')
print(f'Image array shape: {image_data.shape}')

# %%
# Read pixel size
print(f'Pixel size: {bioimage.physical_pixel_sizes}')
# Read metadata
print(f'Metadata type: {type(bioimage.metadata)}')
# print(f'Metadata: {bioimage.metadata}')

# %%
# Inspect dimension and shape of the second image
bioimage.set_scene(1)
print(f'Image dimension: {bioimage.dims}')
print(f'Dimension order is: {bioimage.dims.order}')
print(f'Image shape: {bioimage.shape}')

# %%
# Extract image data (5D)
image_data = bioimage.data
print(f'Image type: {type(image_data)}')
print(f'Image array shape: {image_data.shape}')

# %%
# Read pixel size
print(f'Pixel size: {bioimage.physical_pixel_sizes}')
# Read metadata
print(f'Metadata type: {type(bioimage.metadata)}')
# print(f'Metadata: {bioimage.metadata}')