# TODO: Change the below code to open the VSI dataset

# %% 
# Open a VSI image file
# minimal conda env for this module
# conda create -n ImageFileFormats python=3.10
# activate ImageFileFormat
# pip install bioio bioio-tifffile bioio-lif bioio-czi bioio-ome-tiff bioio-ome-zarr notebook
# Note: for only dealing with .lif just do pip install bioio bioio-lif


# %%
# Load .lif file
# - Observe that BioImage chooses the correct reader plugin
from bioio import BioImage
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_xyc__two_images.lif"
bioimage = BioImage(image_url)
print(bioimage)
print(type(bioimage))

# %%
# Inspect number of images in object
print(bioimage.scenes)

# %%
# Inspect both images in the object
for image in bioimage.scenes:
    print(f'Image name: {image}')
    # Select image:
    bioimage.set_scene(image)
    # Inspect dimension and shape of image
    print(f'Image dimension: {bioimage.dims}')
    print(f'Dimension order is: {bioimage.dims.order}')
    print(f'Image shape: {bioimage.shape}')
    # Extract image data (5D)
    image_data = bioimage.data
    print(f'Image type: {type(image_data)}')
    print(f'Image array shape: {image_data.shape}')
    # Extract specific image part
    image_data = bioimage.get_image_data('YX')
    print(f'Image type: {type(image_data)}')
    print(f'Image array shape: {image_data.shape}')
    # Read pixel size
    print(f'Pixel size: {bioimage.physical_pixel_sizes}')
    # Read metadata
    print(f'Metadata type: {type(bioimage.metadata)}')
    print(f'Metadata: {bioimage.metadata}')
    print('\n')
