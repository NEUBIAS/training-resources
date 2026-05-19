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
# Option 1:
from pathlib import Path
bioimage.save(Path().cwd()/'converted_file.ome.tiff')

# Option 2:
BioImage(image_url).save(Path().cwd()/'direct_conversion.ome.tiff')