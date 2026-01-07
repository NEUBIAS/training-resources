# %% 
# Open a VSI image file
# minimal conda env for this module
# conda create -n ImageFileFormats python=3.12
# activate ImageFileFormat
# pip install bioio bioio-bioformats notebook


# %%
# Download the vsi.zip file and unzip it
# - Observe that BioImage chooses the correct reader plugin
from bioio import BioImage
image_path = "~/Downloads/olympus-vsi/prionium_example_29.vsi"
bioimage = BioImage(image_path)
print(bioimage)
print(type(bioimage))

# %%
# Inspect number of images in object
print(bioimage.scenes)

# %%
# Inspecting one image scene
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
