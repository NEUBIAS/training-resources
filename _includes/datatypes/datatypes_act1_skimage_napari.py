# Import modules
import napari
import numpy as np

# Open napari
viewer = napari.Viewer()

# Open the image
# - Uncomment the image that you want to read
from skimage.io import imread
image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_noisy_different_intensity.tif')
#image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_a.tif')
#image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_intensity_clipping_issue_b.tif')
#image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__two_objects.tif')
#image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif')
#image = imread('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__scanR_datatype_issue.tif')

# View the image
viewer.add_image(image)

# Check the image's datatype and its value limits
print(np.iinfo(image.dtype))

# Check the image's minimum and maximum intensity
print(np.min(image),np.max(image))
