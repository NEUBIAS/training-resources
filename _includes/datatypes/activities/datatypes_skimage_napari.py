# Import modules
from load_from_url import load_from_url
from napari.viewer import Viewer
import numpy as np

# Open napari
viewer = Viewer()

# Open the image
# - Uncomment the image that you want to read
image_url = load_from_url('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif')
#image_url = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_a.tif')
#image_url = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_b.tif')
#image_url = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__two_objects.tif')
#image_url = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif')
#image_url = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif')
print(image_url.dims)
image = image_url.data

# View the image
viewer.add_image(image)

# Check the image's datatype and its value limits
print(np.iinfo(image.dtype))

# Check the image's minimum and maximum intensity
print(np.min(image),np.max(image))
